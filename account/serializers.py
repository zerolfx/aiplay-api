from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueTogetherValidator


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'username': {'min_length': 4, 'max_length': 30,
                                     'error_messages': {
                                         'min_length': 'Your username should contain at least 4 characters.',
                                         'max_length': 'Your username should not be more than 30 characters.',
                                     }},
                        'password': {'min_length': 6,
                                     'error_messages': {
                                         'min_length': 'Your password should contain at least 6 characters.',
                                     }},
                        }

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, error_messages={
        'max_length': "Username can't be longer than 30 characters."})
    password = serializers.CharField(max_length=150)
    #
    # def validate(self, data):
    #     user = authenticate(**data)
    #     if not user:
    #         raise serializers.ValidationError('Username or password is invalid.')
    #     return data
    #
    # def create(self, validated_data):
    #     return authenticate(**validated_data)
    #
    # def retrieve(self, validated_data):
    #     return authenticate(**validated_data)