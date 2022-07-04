from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from regusuarios.views import ListadoUsers,RegistrarUsers,EditarUsuario

 
urlpatterns = [
   path('listado_usuarios/', login_required(ListadoUsers.as_view()),
    name ='listar_users'),
   path('registrar_usuarios/', login_required(RegistrarUsers.as_view()),
    name ='registrar_users'), 
   path('actualizar_usuario/<int:pk>', login_required(EditarUsuario.as_view()),
    name = 'actualizar_usuario'),
]

urlpatterns += [
    path('inicio_usuarios/',login_required(
       TemplateView.as_view(
            template_name = 'usuarios/listar_users.html'
        )
    ), name ='inicio_usuarios'),
]
