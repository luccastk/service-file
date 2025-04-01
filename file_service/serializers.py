from rest_framework import serializers
from datetime import datetime
class StockSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
class BatchSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    validity = serializers.DateField(required=False, allow_null=True)
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    stock = StockSerializer()
    batch = BatchSerializer(many=True)

class ResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    timeStamp = serializers.DateTimeField()
    data = ProductSerializer(many=True)
 
class ErrorResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    message = serializers.CharField()