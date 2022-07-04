import os
import json
from re import template
from sre_constants import SUCCESS
from winreg import DeleteKey
from django import dispatch
from django.core.serializers import serialize
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from matplotlib.style import context
from pytest import Instance
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from requests import request
from sqlalchemy import false
from .forms import UsuarioForm, DocumentoForm
from .models import Usuario,Documento



#1. dispatch(): Valida la petición y elige que metodo http se utilizo para la solicitud ###
#2. http_method_not_allowed(): retorna un error cuando se utiliza un metodo http no soportado a definido
#3. options()

#def home(request):
 #   return render(request,'index.html')

#class TemplateView(View):
   # def get(self, request, *args, **kwargs):
    #    pass

class Inicio(TemplateView):
    template_name = 'index.html'
    #def get(self, request, *args, **kwargs):
        #return render(request, 'index.html')

class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuario/autor/listar_usuario.html'
    context_object_name ='usuarios'
    queryset = Usuario.objects.filter(estado = True)

    #def get_queryset(self):
        #print("MENSAJE DESDE GET QUERYSET")        
        #return self.queryset

class ActualizarUsuario(UpdateView):
    model = Usuario
    template_name = 'usuario/autor/crear_usuario.html'
    form_class =UsuarioForm
    success_url = reverse_lazy('listarusuario')

class CrearUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/autor/crear_usuario.html'
    success_url = reverse_lazy('listarusuario')

class EliminarUsuario(DeleteView):
    model = Usuario
    #success_url = reverse_lazy('listarusuario')

    def post(self,request,pk,*args,**kwargs):
        object = Usuario.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('listarusuario')
    
class ListadoDocumentos(ListView):
    model = Documento
    #form_class = DocumentoForm
    template_name = 'usuario/documento/listar_documento.html' #queryset = documento.objects.all()
    
    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():  
            return HttpResponse (serialize('json',self.get_queryset(),use_natural_foreign_keys =True),'appication/json')
        else:
            return render(request,self.template_name)
        

class InicioDocumento(TemplateView):
    template_name = 'usuario/documento/listar_documento.html'
    permission_required = ('libro.view_libro', 'libro.add_libro',
                          'libro.delete_libro', 'libro.change_libro')

class CrearDocumento(CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'usuario/documento/crear_documento.html'
    #success_url = reverse_lazy('listado_documentos')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(data = request.POST,files = request.FILES)
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        return redirect('usuario:inicio_documento')

class ActualizarDocumento(UpdateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'usuario/documento/documento.html'
    success_url = reverse_lazy('listado_documentos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['documentos'] = Documento.objects.filter(estado = True)
        return context

class EliminarDocumento(DeleteView):
    model = Documento

    def post(self,request,pk,*args,**kwargs):
        object = Documento.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('listado_documentos')

def AnalisisDatos(request):
      return render(request,'usuario/estadis.html')


