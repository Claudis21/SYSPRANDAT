import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView 
from regusuarios.models import Usuario
from .forms import FormularioLogin, FormularioUsuario


class Login(FormView):
    template_name = 'login.html'
    form_class =FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
           return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)
 
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')   

class InicioListadoUsuario(TemplateView):
    template_name = 'usuarios/listar_users.html'
       
class ListadoUsers(ListView):
    model = Usuario
    template_name = 'usuarios/listar_users.html'
    
     
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo = True)

    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json',self.get_queryset()),'aplication/json')
        else:
            return redirect('usuarios:inicio_usuarios')
    

class RegistrarUsers(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_users.html'
    #success_url = reverse_lazy('usuarios:listar_users')

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_usuario = Usuario(
                email= form.cleaned_data.get('email'),
                username= form.cleaned_data.get('username'),
                nombres= form.cleaned_data.get('nombres'),
                apellidos= form.cleaned_data.get('apellidos')       

                )
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()
                #return redirect('usuarios:listar_users')
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje,'error': error})
                response.status_code= 201
                return response   
                #return redirect('usuarios:listar_users')                             
            else:
                #return render(request,self.template_name, {'form':form })  
                mensaje = f'{self.model.__name__}No se ha  podido registrar'
                error= form.errors
                response = JsonResponse({'mensaje': mensaje,'error': error})
                response.status_code= 400
                return response
        else:
             return redirect('usuarios:inicio_usuarios')

class EditarUsuario(UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/editar_usuario.html'

    def post(self, request, *args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_context_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje,'error': error})
                response.status_code= 201
                return response   
                #return redirect('usuarios:listar_users')                             
            else:
                #return render(request,self.template_name, {'form':form })  
                mensaje = f'{self.model.__name__}No se ha podido actualizar'
                error= form.errors
                response = JsonResponse({'mensaje': mensaje,'error': error})
                response.status_code= 400
                return response
        else:
             return redirect('usuarios:inicio_usuarios')
