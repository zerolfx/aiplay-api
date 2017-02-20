from rest_framework import generics, mixins

from .serializers import ProblemSerializer, TagSerializer
from .models import Problem, Tag


class ProblemCreateAPI(generics.CreateAPIView):
    serializer_class = ProblemSerializer


class ProblemDetailAPI(generics.GenericAPIView,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       ):
    queryset = Problem.objects.all()
    lookup_field = 'id'
    serializer_class = ProblemSerializer

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)


class TagAPI(generics.GenericAPIView,
             mixins.CreateModelMixin,
             mixins.RetrieveModelMixin,
             mixins.DestroyModelMixin,
             ):
    queryset = Tag.objects.all()
    lookup_field = 'name'
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class TagCreateAPI(generics.CreateAPIView):
    serializer_class = TagSerializer