from django.db import models

# Create your models here.
class Estudiantes(models.Model):
   id_estudiante=models.AutoField(primary_key=True)
   nombre=models.CharField(max_length=25)
   apellidos=models.CharField(max_length=25)
   celular=models.CharField(max_length=25)
   cedula=models.IntegerField(unique=True)
   correo=models.EmailField(unique=True)
   semestre=models.IntegerField()
   def __str__(self):
       return self.nombre
   class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"    
class Semestre(models.Model):
    id_semestre=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25,unique=True)
    def __str__(self):
      return self.nombre
class Espacio_academico(models.Model):
    id_espacio_academico=models.IntegerField
    espacio=models.CharField(max_length=25,unique=True)
    id_estudiante=models.ManyToManyField(Estudiantes,blank=True)
    id_semestre=models.ForeignKey(Semestre,on_delete=models.CASCADE)

    def __str__(self):
        return self.espacio  

class Sesiones(models.Model):
    id_sesion=models.AutoField(primary_key=True)
    sesion=models.CharField(max_length=25)
    fecha=models.DateTimeField()
    horainicio=models.TimeField()
    horafin=models.TimeField()
    id_espacio_academico=models.ForeignKey(Espacio_academico,on_delete=models.CASCADE,blank=True)
    id_estudiante = models.ManyToManyField(Estudiantes,through='Asistencia',blank=True)
    def __str__(self):
       return self.sesion 
    class Meta:
        verbose_name = "sesion"
        verbose_name_plural = "sesiones"

class Asistencia(models.Model):
    id_sesion=models.ForeignKey(Sesiones,on_delete=models.CASCADE)
    id_estudiante=models.ForeignKey(Estudiantes,on_delete=models.CASCADE,blank=True)
    
    