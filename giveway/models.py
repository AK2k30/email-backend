from django.db import models

class UserSubmission(models.Model):
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email
