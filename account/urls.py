from django.conf.urls import url
from .views import UserRegisterAPI, TestViewAPI

urlpatterns = [
    url(r'^register/', UserRegisterAPI.as_view(), name="register"),
    url(r'^test/', TestViewAPI.as_view()),
]
