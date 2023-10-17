from django.db import models

# Create your models here.
class Boys(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    Talent = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    Birth_Date = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.phone} {self.Talent} {self.age} {self.Birth_Date}"
    
    
