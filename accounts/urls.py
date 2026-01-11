from django.urls import path
from .views import (
    register_view,
    login_view,
    change_password_view,
    profile_view,
    refresh_token_view,
)

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('token/refresh/', refresh_token_view),
    path('change-password/', change_password_view),
    path('profile/', profile_view),
]
