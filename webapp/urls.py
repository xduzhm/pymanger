from django.urls import path
from webapp import views

urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('<str:views>.html', views.view),
    path('<str:direct>/<str:views>.html', views.directory),
    path('resource/list', views.resource_list),

]
