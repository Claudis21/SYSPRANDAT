from attr import attrs
from django import forms
from  django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.forms import AuthenticationForm
from matplotlib import widgets
from regusuarios.models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormularioUsuario(forms.ModelForm):
 
    
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña..',
            'id': 'password1',
            'required': 'required', 
        }
    ))

    password2 = forms.CharField(label = 'contraseña de confirmación', widget= forms.PasswordInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña..',
            'id': 'password2',
            'required': 'required', 
        }
    ))

    class Meta: 
        model = Usuario
        fields = ('email','username','nombres','apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Correo Electónico',
                }
            ),
            'nombres': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'username': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            )
            
        }


    def clean_password2(self):
    #validación de Contraseña 
    #Metodo que valida ambas contraseñas, ingresadas sean iguales, esto antes de ser encriptadas
    #y guardadas en la BD, Retornar la contraseña valida
    
    #Excepciones:
    # Validation error: cuando las contraseñas no son iguales muestra un mensaje de error
        print (self.cleaned_data)
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

    def save(self,commit = True):
        usuario = super().save(commit = False)
        usuario.set_password(self.cleaned_data['password1'])
        if commit:
            usuario.save()
        return usuario