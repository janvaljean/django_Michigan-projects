from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('goodbye/', views.index1, name='index1'),
    path('main/', views.index2, name='index2'),
]