from django.db import models

# Create your models here.
class Familiar(models.Model):

    nombre=models.CharField(max_length=40)
    parentesco=models.CharField(max_length=40)
    edad=models.IntegerField()
    nacimiento=models.DateField()

    def __str__(self) -> str:
        return f'{self.nombre} es mi {self.parentesco} y tiene {self.edad} años dado que nació en {self.nacimiento}' 

