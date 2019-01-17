from django.urls import path
from webapp import views

urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('<str:views>.html/', views.view),
    path('<str:directory>/<str:views>.html/', views.directory),

]
