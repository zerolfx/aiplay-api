from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework import mixins, generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, authenticate


class UserRegisterAPI(generics.GenericAPIView,
                      mixins.CreateModelMixin):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        return self.create(request)


class TestViewAPI(APIView):
    def get(self, request):
        print(request.user)
        return Response(None)

