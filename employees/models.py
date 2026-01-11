from django.db import models

# Create your models here.

class Employee(models.Model):
    form_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
