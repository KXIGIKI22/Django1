from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.id}: {self.username}"

    def __str__(self):
        return self.title