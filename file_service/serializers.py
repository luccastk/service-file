from rest_framework import serializers

class ResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    timeStamp = serializers.DateTimeField()
    data = serializers.CharField()
 
class ErrorResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    message = serializers.CharField()