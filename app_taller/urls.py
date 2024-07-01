from django.urls import path
from . import views

app_name = 'app_taller'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('quienessomos/', views.quienessomos, name='quienessomos'),
]