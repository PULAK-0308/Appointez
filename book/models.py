from django.db import models


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=30,default="")
    age  = models.IntegerField(default=0)
    deptofdoctor = models.CharField(max_length=30,default="")
    doctor = models.CharField(max_length=30,default="")
    email=models.CharField(max_length=122,default="")
    date = models.DateField()
    
    
    def __str__(self):
        return f'{self.name} {self.age} {self.deptofdoctor} {self.doctor} {self.email} {self.date}'