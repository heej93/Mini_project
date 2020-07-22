from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=255)
    user_pw = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_dog = models.CharField(max_length=255)
    def __str__(self):
        return str((self.user_id, self.user_pw, self.user_email, self.user_dog))