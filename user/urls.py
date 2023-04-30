from django.urls import path
from user.login import Login
from .views import CreateUpdateAccountAPIView


urlpatterns = [
    path("login", Login.as_view()),
    path("create_account", CreateUpdateAccountAPIView.as_view())
]