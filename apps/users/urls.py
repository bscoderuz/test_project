from django.urls import path
from . import api_endpoints as views

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='get_token'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('blacklist/', views.BlacklistTokenView.as_view(), name='blacklist'),
    path('token/refresh/', views.RefreshTokenView.as_view(), name='refresh_token'),

]
