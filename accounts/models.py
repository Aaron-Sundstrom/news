from django.db import models
from django.contrib.auth.models import AbstractUser

# Model for available classes
class AvailableClass(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# Custom User model for Tutors
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True,blank=True)
    major = models.CharField(max_length=255,null=True,blank=True)
    # Many-to-many relationship: a tutor can teach many classes
    classes = models.ManyToManyField(AvailableClass, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
