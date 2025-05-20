from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.postgres.fields import ArrayField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)

        # default username to the part before “@”
        uname = username or email.split('@')[0]
        original = uname
        count = 1
        # avoid collisions
        while self.model.objects.filter(username=uname).exists():
            uname = f"{original}{count}"
            count += 1

        user = self.model(email=email, username=uname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, username=username, **extra_fields)


class CustomUser(AbstractUser):
    # plug in the custom manager
    objects = CustomUserManager()

    age_group  = models.CharField(max_length=20, blank=True)
    hair_types = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    skin_types = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    allergies  = ArrayField(models.CharField(max_length=50), default=list, blank=True)

    def __str__(self):
        return self.username
