from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    UserRegisterSerializer,
    UserAbstractView,
    UserDetailView,
)

from .models import User


class UserRegisterAPI(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserAbstractAPI(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserAbstractView


class UserDetailAPI(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin
                    ):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserDetailView

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TestViewAPI(APIView):
    def get(self, request):
        print(request.user)
        return Response(None)