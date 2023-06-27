from django.urls import path
from . import views

urlpatterns = [
    path('milad/HTML', views.milad, name='milad'),
]