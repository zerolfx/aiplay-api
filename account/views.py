from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.response import Response

from .serializers import (
    UserRegisterSerializer,
    UserAbstractSerializer,
    UserDetailSerializer,
)

from .models import User


class UserRegisterAPI(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserAbstractAPI(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserAbstractSerializer


class UserDetailAPI(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin
                    ):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TestViewAPI(APIView):
    def get(self, request):
        print(request.user)
        return Response(None)