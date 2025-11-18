from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="user_register"),
    path('login/', views.auth_login, name="user_login"),
    path('logout/', views.auth_logout, name="user_logout")
]
