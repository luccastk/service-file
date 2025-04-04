from rest_framework.views import APIView
from .error_presenter import error_response
from .data_presenter import success_response

class BaseApiView(APIView):
    def sucess(self, data):
        return success_response(data)
    
    def error(self, message):
        return error_response(message)