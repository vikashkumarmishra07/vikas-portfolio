from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)   # new
    created_at = models.DateTimeField(auto_now_add=True)  # new

    def __str__(self):
        return self.name