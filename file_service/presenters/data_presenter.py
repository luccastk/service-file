from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ResponseSerializer

def success_response(data, code=status.HTTP_200_OK):
    payload = {
        "code": code,
        "timeStamp": datetime.now(),
        "data": data
    }
    serializer = ResponseSerializer(payload)
    return Response(serializer.data, status=code)