from django.db import models

class Purchase(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return f"{self.id}: {self.username}"



    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.user} purchased {self.book}'