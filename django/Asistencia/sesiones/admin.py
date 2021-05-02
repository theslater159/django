from django.contrib import admin
from sesiones.models import Estudiantes,Semestre,Espacio_academico,Sesiones,Asistencia

# Register your models here.
class EstudiantesAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellidos", "semestre")
    search_fields=("nombre", "semestre")
class Sesiones_admin(admin.ModelAdmin):
    list_display=("sesion","fecha","horainicio","horafin","id_espacio_academico")
    list_filter= ("id_espacio_academico",)  
class Espacio_academico_admin(admin.ModelAdmin):
    list_display=("espacio","id_semestre")
    list_filter= ("id_semestre",)    
class Asistencia_admin(admin.ModelAdmin):
    list_display=("id_sesion","id_estudiante")     
    list_filter= ("id_sesion",)      

admin.site.register(Espacio_academico,Espacio_academico_admin)
admin.site.register(Estudiantes,EstudiantesAdmin)
admin.site.register(Semestre)
admin.site.register(Sesiones,Sesiones_admin)
admin.site.register(Asistencia,Asistencia_admin)

