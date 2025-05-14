from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField

class CustomUser(AbstractUser):
    age_group  = models.CharField(max_length=20, blank=True)
    hair_types = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    skin_types = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    allergies  = ArrayField(models.CharField(max_length=50), default=list, blank=True)

    def __str__(self):
        return self.username
