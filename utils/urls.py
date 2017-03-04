from django.conf.urls import url
from .views import MarkdownAPI

urlpatterns = [
    url(r'^markdown$', MarkdownAPI.as_view())
]