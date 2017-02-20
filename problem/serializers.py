from rest_framework import serializers
from .models import Problem, Tag


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
    tags = serializers.SerializerMethodField()

    def get_tags(self, obj):
        tags_qs = Tag.objects.filter(problem=obj)
        tags = TagSerializer(tags_qs, many=True).data
        return tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
