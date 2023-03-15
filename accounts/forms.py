from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    "Custom user creation form"
    # NOTE: According to the django docs `UserCreationForm.Meta`
    # is subclassed.
    # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):
    "Custom user change form"
    # WARN: Just testing the super class `UserCreationForm.Meta`,
    # it seems more intuitive.
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
