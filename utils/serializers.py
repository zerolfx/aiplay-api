from rest_framework import serializers


class MdSerializer(serializers.Serializer):
    content = serializers.CharField()