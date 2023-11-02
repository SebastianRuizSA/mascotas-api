from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #Por que se añade esto?, ver pagina 65 de scoops (ver herencias)

class Raza(models.Model):
    """
    Modelo que define el comportamiento de Razas
    """

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500, default='')
    photo_main = models.ImageField(upload_to='photos/razas')

    def __str__(self):
        return f"{self.nombre}"

class Perro(TimeStampedModel):
    """
    Modelo que define el comportamiento de Dog
    """

    nombre = models.CharField(max_length=200)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500, default='')
    photo_main = models.ImageField(upload_to='photos/perros')

    def __str__(self):
        return f"{self.nombre}"