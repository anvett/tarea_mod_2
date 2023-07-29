from django.db import models

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200, blank=False, null=False, verbose_name='Título')
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.titulo
    
    
    