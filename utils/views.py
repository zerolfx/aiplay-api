from rest_framework.views import Response
from rest_framework import generics
from . import md
from .serializers import MdSerializer


class MarkdownAPI(generics.GenericAPIView):
    serializer_class = MdSerializer

    def post(self, request):
        print(request.data)
        return Response(md.convert(md.convert(request.data.get('content', ''))))