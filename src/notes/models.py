from django.db import models
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    CRITICALITY= (
        ('W', 'Срочно'),
        ('M', 'Несрочно'),
        ('L', 'Бессрочно'),
    )
    discription =  models.CharField(max_length=120, verbose_name="Описание")
    date = models.DateTimeField(default=timezone.now, verbose_name="Дата")
    criticality = models.CharField(max_length=2, choices=CRITICALITY, verbose_name="Критичность")

    def __str__(self):
        return self.discription
