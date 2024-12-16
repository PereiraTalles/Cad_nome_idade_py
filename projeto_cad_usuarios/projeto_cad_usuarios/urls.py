from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view respondavel, nome de referença
    #usuarios.com
    path('',views.home,name='home'),
]
