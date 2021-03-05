from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate_api', views.calculate_api, name='calculate_api')
]