from django.db import models

class Purchase(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.user.name} purchased {self.book.title}"