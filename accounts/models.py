from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.postgres.fields import ArrayField

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        # default username to part before “@” if none provided
        username = username or email.split('@')[0]
        original = username
        count = 1
        while self.model.objects.filter(username=username).exists():
            username = f"{original}{count}"
            count += 1

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, username=username, **extra_fields)


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField('email address', unique=True)
    objects = CustomUserManager()

    age_group  = models.CharField(max_length=20, blank=True)
    hair_types = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    skin_types = ArrayField(models.CharField(max_length=20), default=list, blank=True)
    allergies  = ArrayField(models.CharField(max_length=50), default=list, blank=True)

    def __str__(self):
        return self.email
