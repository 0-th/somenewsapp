from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model"""
    # Add an age field to the default fields from `AbstractUser`
    age = models.PositiveIntegerField(null=True, blank=True)
    # The age field can store a db entry as null and accepts an empty
    # value as input (e.g form field input).
