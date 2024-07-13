from django.db import models


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ["name"]
