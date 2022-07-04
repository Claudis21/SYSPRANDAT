from django.urls import path
from django.contrib.auth.decorators import login_required
from.views import *

urlpatterns =[
    path('crear_usuario/',login_required(CrearUsuario.as_view()), name = 'crear_usuario'),
    path('listarusuario/',login_required(ListadoUsuario.as_view()), name = 'listarusuario'),
    path('editar_usuario/<int:pk>/',login_required(ActualizarUsuario.as_view()), name = 'editar_usuario'),
    path('eliminar_usuario/<int:pk>/', login_required(EliminarUsuario.as_view()), name = 'eliminar_usuario'),
    
    path('inicio_documento/',InicioDocumento.as_view(), name = 'inicio_documento'),
    path('listar_documentos/', login_required(ListadoDocumentos.as_view()), name = 'listado_documentos'),
    path('crear_documento/', login_required(CrearDocumento.as_view()), name = 'crear_documento'),
    path('editar_documento/<int:pk>/', login_required(ActualizarDocumento.as_view()), name = 'editar_documento'),
    path('eliminar_documento/<int:pk>/', login_required(EliminarDocumento.as_view()), name = 'eliminar_documento'),

    path('analisis_datos/', AnalisisDatos, name = 'analizar_datos')
]

