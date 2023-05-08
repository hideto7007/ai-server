from django.urls import path
from user.login import Login
from .views import CreateUpdateAccountAPIView, UserInfoListAPIView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login", Login.as_view()),
    path("create_account", CreateUpdateAccountAPIView.as_view()),
    path("user_list", UserInfoListAPIView.as_view()),
    path('password_change_form',
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change_form'),  # 追加
    path('password_change_done',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_finish.html'),
         name='password_change_done'),  # 追加
]