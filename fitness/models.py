from django.db import models    

# Create your models here.
class Usuario(models.Model):
    nombre      = models.TextField()
    apellido    = models.TextField()
    peso        = models.IntegerField()#kg
    talla       = models.IntegerField()#cm
    edad        = models.IntegerField()
    email       = models.EmailField(max_length=254)
    fechaInicio = models.DateTimeField(auto_now_add = True)
    fechaActualizacion = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return "/usuario/" + str(self.id) + "/"
