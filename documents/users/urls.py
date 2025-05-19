from django.urls import path

from .views import LoginUserView, LogoutUserView, RegisterUserView

app_name = 'users'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name = 'register'),
]
