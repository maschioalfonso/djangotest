from django.contrib import admin
from sia.models import Alumno, Pais, Materia, Curso, Cursado, Cuota

admin.site.register(Pais)
admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(Curso)
admin.site.register(Cursado)
admin.site.register(Cuota)
