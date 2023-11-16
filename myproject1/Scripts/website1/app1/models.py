from django.db import models

# Create your models here.
class form1(models.Model):
    name= models.CharField( max_length=50)
    wish= models.CharField( max_length=50)
    address= models.CharField( max_length=50)
    number= models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    