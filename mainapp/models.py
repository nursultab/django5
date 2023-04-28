from django.db import models

class Planets (models.Model):
    name =  models.CharField(max_length=127)
    number=models.PositiveIntegerField(default=1)
    life=models.CharField(max_length=127)

    class Meta:
        verbose_name = 'планета'
        verbose_name_plural = 'планеты'

    def __str__(self):
          return f'планета {self.name} номер {self.number}'
    
class 