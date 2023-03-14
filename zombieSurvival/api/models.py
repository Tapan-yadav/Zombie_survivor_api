from django.db import models

# Create your models here.

class Survivor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    is_infected = models.BooleanField()
    count_reports = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = u'Survivor'
        verbose_name_plural = u'Survivors'
        
    def __str__(self):
        return self.name
