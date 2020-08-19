from django.urls import path
from . import views

urlpatterns = [
    path('', views.coaching, name='coaching')
]
