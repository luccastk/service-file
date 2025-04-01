from .presenters.presenters_view import BaseApiView
from rest_framework.parsers import MultiPartParser
from .serializers import ProductSerializer
from .mappers.csv_mapper import ProductCsvMapper
from .validators.validation import CSVFileValidator
from .services.convert_csv_service import CSVToDataFrame

class UploadCSVFile(BaseApiView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        try:
            file = request.FILES.get('file')
            file = CSVFileValidator(file).validate()

            df = CSVToDataFrame(file).parse()

            validated_products = []
            for index, row in df.iterrows():
                mapped_data = ProductCsvMapper(row=row).to_nested_dict()
                serializer = ProductSerializer(data=mapped_data)
                if serializer.is_valid():
                    validated_products.append(serializer.validated_data) 
                else:
                    return self.error(f'[ERRO line {index+2}]\n{serializer.errors}')
            return self.sucess(data=sorted(validated_products, key=lambda x: x['name']))
        
        except ValueError as e:
            return self.error(str(e))