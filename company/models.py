from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True)
    logo = models.ImageField(upload_to='logos', null=True)
    website = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
