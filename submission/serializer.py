from rest_framework import serializers
from .models import Submission
from account.serializers import UserAbstractSerializer


class SubmissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
        # exclude = ['result']


class SubmissionAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        exclude = ['code']
    author = UserAbstractSerializer()


class SubmissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
    author = UserAbstractSerializer()
