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


class UserLoginAPI(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)
            if not user:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                login(request, user)
                return Response({'username': user.username}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': 'invalid request'}, status=status.HTTP_400_BAD_REQUEST)


