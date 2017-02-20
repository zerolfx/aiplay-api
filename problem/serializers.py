from rest_framework import serializers
from .models import Problem
from tagging.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"
    # tags = serializers.CharField(many=True)
    tags = TagSerializer(many=True)


