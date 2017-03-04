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
        fields = '__all__'
    tags = serializers.SerializerMethodField(required=False, read_only=False)

    def get_tags(self, obj):
        return list(obj.tags.all().values_list('name', flat=True))

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        print(validated_data)
        problem = super(ProblemSerializer, self).create(validated_data)
        problem.tags = tags_data
        print(tags_data)
        return problem

'''
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        # fields = "__all__"
        fields = ['title', 'tags']
    # tags = serializers.CharField(many=True)
    tags = TagSerializer(many=True)

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        print(validated_data)
        problem = super(ProblemSerializer, self).create(validated_data)
        # Problem.objects.create(**validated_data)
        print(tags_data)
        return problem

'''