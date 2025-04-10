import uuid
import os
from .presenters.presenters_view import BaseApiView
from rest_framework.parsers import MultiPartParser
from .validators.validation import CSVFileValidator
from django.core.files.storage import default_storage
from .services.kafka_producer import KafkaProducerService
from django.http import FileResponse

class UploadCSVFile(BaseApiView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            file = request.FILES.get('file')
            storeId = request.POST.get('storeId')

            if not storeId:
                raise ValueError('Id da loja obrigatório.')

            CSVFileValidator(file).validate()
    
            request_id = str(uuid.uuid4())
            filename = f"{request_id}_{file.name}"
            file_path = os.path.join("upload", filename)

            with default_storage.open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        
            KafkaProducerService().send(
                topic='file.upload',
                value={
                    "request_id": request_id,
                    "storeId": storeId
                },
                key=request_id
            )

            payload = {
                "File receive and Process."
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
    
