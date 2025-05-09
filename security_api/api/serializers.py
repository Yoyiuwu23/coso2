from rest_framework import serializers

class ScanRequestSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=200)