from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # Add other fields as needed

    def __str__(self):
        return self.username
