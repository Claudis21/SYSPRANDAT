from logging import PlaceHolder
from django import forms
from matplotlib import widgets
from.models import Usuario, Documento

class UsuarioForm(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = ['cedula', 'nombres', 'apellidos','descripcion']
        labels = {
            'cedula':'Cedula del usuario',
            'nombres':'Nombres del usuario',
            'apellidos':'Apellidos del usuario',
            'descripcion':'Descripción del usuario',
        }
        widgets = {
            'cedula': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el nombre del usuario',
                    'id': 'cedula'
                }
            ),
            'nombres': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese los nombres del usuario',
                    'id': 'nombres'
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese los apellidos del usuario',
                    'id': 'apellidos'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese descripcion del usuario',
                    'id': 'descripcion'
                }
            ),
        }

class DocumentoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Usuario_id'].queryset = Usuario.objects.filter(estado = True)
            
    class Meta:
        model = Documento
        fields = ('titulo','resumen','Usuario_id','fecha_publicacion','palabras_clave','archivo', 'tipo_producto')
        label = {
            'titulo': 'Título del producto',
            'resumen': 'Resumen del producto',
            'Usuario_id': 'Autor(es) del producto',
            'fecha_publicación': 'Fecha publicación del libro',
            'palabras_clave': 'Palabras clave del producto',
            'archivo': 'Adjuntar archivo del producto',
        }
        widgets = {
            'título': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placehoder': 'Ingrese el título del producto',
                }
            ),
            'resumen': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placehoder': 'Ingrese el resumen del producto',
                }
            ),
            'Usuario_id': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(),
            'palabras:clave': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placehoder': 'Ingrese las palabras clave del producto',
                }
            ),
            #'archivo': forms.TextInput(
                #attrs = {
                   # 'class': 'form-control',
                    #'placehoder': 'Adjunte el archivo del producto',
               # }
           # ),
        }

        
