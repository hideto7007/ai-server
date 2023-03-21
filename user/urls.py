from django.urls import path
from user.login import Login


urlpatterns = [
    path("login", Login.as_view())
]