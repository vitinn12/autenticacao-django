from django.urls import path
from .views import index, perfil, registro, autenticar

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro, name='registro'),
    path('login/', autenticar,name='login')
]