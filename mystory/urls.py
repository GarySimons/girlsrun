from django.urls import path
from . import views

urlpatterns = [
    path('', views.mystory, name='mystory')
]
