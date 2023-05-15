from django.urls import path
from user.login import Login
from .views import CreateUpdateAccountAPIView, UserInfoListAPIView, PasswordUpdateAPIView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login", Login.as_view()),
    path("create_account", CreateUpdateAccountAPIView.as_view()),
    path("user_list", UserInfoListAPIView.as_view()),
    path('update_password', PasswordUpdateAPIView.as_view()),  # 追加
]