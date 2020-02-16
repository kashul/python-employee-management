from django.db import models
from company.models import Company


class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
