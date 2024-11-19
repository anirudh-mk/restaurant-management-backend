from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.CharField(primary_key=True, default=uuid.uuid4(), max_length=36)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = None
    phone = None
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    @classmethod
    def email_exists(cls, email):
        return cls.objects.filter(email=email).exists()

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
