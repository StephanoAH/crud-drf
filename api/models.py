from django.db import models
import uuid


class Jokes(models.Model):
    joke = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name
