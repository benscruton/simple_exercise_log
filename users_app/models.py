from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = {}
        users_with_email = User.objects.filter(email = post_data["email"])

        if (len(post_data["first_name"]) < 1):
            errors["first_name"] = "First name is required."
        if (len(post_data["last_name"]) < 1):
            errors["last_name"] = "Last name is required."
        if (not EMAIL_REGEX.match(post_data["email"]) or len(post_data["email"]) < 1):
            errors["email"] = "A valid email address is required."
        if len(users_with_email) > 0:
            errors["email"] = "There is already a user registered with this email address."
        if len(post_data["password"]) < 8:
            errors["password"] = "Password must be at least 8 characters long."
        if not (post_data["password"] == post_data["confirm_pw"]):
            errors["confirm_pw"] = "Passwords must match."

        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    hashed_pw = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()