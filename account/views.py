from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserAbstractView
)

from .models import User


class UserRegisterAPI(generics.GenericAPIView,
                      mixins.CreateModelMixin
                      ):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        return self.create(request)


class TestViewAPI(APIView):
    def get(self, request):
        print(request.user)
        return Response(None)


class UserAbstractAPI(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserAbstractView
