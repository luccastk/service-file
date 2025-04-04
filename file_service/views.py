import uuid
import os
from .presenters.presenters_view import BaseApiView
from rest_framework.parsers import MultiPartParser
from .validators.validation import CSVFileValidator
from django.core.files.storage import default_storage
from .services.kafka_producer import KafkaProducerService
from django.http import FileResponse

producer = KafkaProducerService()
class UploadCSVFile(BaseApiView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            file = request.FILES.get('file')
            CSVFileValidator(file).validate()
    
            request_id = str(uuid.uuid4())

            file_path = default_storage.save(f"upload/{request_id}_{file.name}", file)
        
            producer.send(
                topic='file.upload',
                value={
                    "request_id": request_id,
                    "file_path": file_path
                },
                key=request_id
            )

            payload = {
                "message": "File receive and Process.",
                "request_id": request_id
            }

            return self.sucess(payload)

        except ValueError as e:
            return self.error(str(e))
        

class DownloadFilesView(BaseApiView):
    def get(self, request, request_id):
        directory = "upload/"
        try:
            filename = next(f for f in os.listdir(directory) if f.startswith(request_id))
        except StopIteration:
            return self.error("File not found.")
        
        file_path = os.path.join(directory, filename)
        if not os.path.exists(file_path):
            raise self.error("File not found.")
        
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)