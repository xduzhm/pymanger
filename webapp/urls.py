from django.urls import path
from webapp import views

urlpatterns = [
    path('index', views.index)
]