from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    
    def __str__(self):
        return self.email
    