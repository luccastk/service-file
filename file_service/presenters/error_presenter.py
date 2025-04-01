from rest_framework.response import Response
from rest_framework import status
from ..serializers import ErrorResponseSerializer

def error_response(message, code=status.HTTP_400_BAD_REQUEST):
    payload = {
        "code": code,
        "message": message
    }
    serializer = ErrorResponseSerializer(payload)
    return Response(serializer.data, status=code)