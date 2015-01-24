

from django.forms import ModelForm, Form, EmailField, CharField, ModelChoiceField
from django.contrib.auth.models import User

from sia.models import Alumno, Pais


# Create the form class.
class UsuarioForm(ModelForm):

#	def __init__():
#		username = super(, help_text='')

    class Meta:
    	model = User
    	#fields = ['username', 'password']


class RegistroForm(ModelForm):
    nombre = CharField()
    apellido = CharField()
    email = EmailField(label='e-mail')
    password = CharField(label='Contraseña')
    pais = ModelChoiceField(queryset=Pais.objects.all(), empty_label=None, label='País Natal')

    
    class Meta:
        model = Alumno
        exclude = ['usuario']
        fields = ['nombre',
                  'apellido',
                  'email',
                  'documento',
                  'domicilio',
                  'pais',
                  'provincia',
                  'localidad',
                  'telefono',
                  'telefono_alter',
                  'fecha_de_nacimiento',
                 ]

        labels = {'nombre' : 'Nombre',
                  'apellido' : 'Apellido',
                  'documento' : 'Nro. de documento',
                  'domicilio' : 'Domicilio',
                  'provincia' : 'Provincia',
                  'localidad' : 'Localidad',
                  'telefono' : 'Teléfono',
                  'telefono_alter' : 'Teléfono alternativo',
                  'fecha_de_nacimiento' : 'Fecha de nacimiento',
                 }
