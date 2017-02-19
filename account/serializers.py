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
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user


class UserAbstractView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'avatar', 'about')


class UserDetailView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'avatar', 'about', 'birth_date', 'country', 'city', 'organization')
        extra_kwargs = {'username': {'read_only': True}
                        }
