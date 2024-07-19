from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # Use AutoField for integer ID
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    def calculate_fine(self):
        if self.returned_at and self.due_date and self.returned_at > self.due_date:
            days_overdue = (self.returned_at - self.due_date).days
            self.fine_amount = days_overdue * 5  # Example: $5 per day overdue
        else:
            self.fine_amount = 0
        self.save()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
