
def crearUsuario(request):
    if request.method == 'POST':
        print(request.POST)
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
           usuario_form.save()
           return redirect('index')
    else:
        usuario_form = UsuarioForm()
        print(usuario_form)
    return render (request, 'usuario/crear_usuario.html',{'usuario_form': usuario_form}) 
    

def listarUsuario(request):
    usuarios = Usuario.objects.filter(estado = True)
    return render(request, 'usuario/listar_usuario.html',{'usuarios':usuarios})

def editarUsuario(request,id):
    usuario_form = None
    error = None
    try:
        usuario = Usuario.objects.get(id = id)
        if request.method == 'GET':
               usuario_form = UsuarioForm(instance = usuario)
               #print(usuario_form)
        else: 
            usuario_form = UsuarioForm(request.POST, instance = usuario)
            if usuario_form.is_valid():
                usuario_form.save()
            return redirect('usuario/listarusuario')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'usuario/crear_usuario.html',{'usuario_form': usuario_form, 'error': error})        

def eliminarUsuario(request,id):
    usuario = Usuario.objects.get(id = id)
    if request.method == 'POST':
       usuario.estado = False 
       usuario.save()
       return redirect('listarusuario')
    return render(request, 'usuario/eliminar_usuario.html', {'usuario': usuario})