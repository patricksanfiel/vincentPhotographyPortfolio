from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio_images', default='media/default.png')
    notes = models.CharField(max_length=200)
    tag = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.title)

class ClientContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    budget_choices = (
        (100, 100),
        (200, 200),
        (300, 300),
        (400, 400),
        (500, 500),
        (600, 600),
        (700, 700),
        (800, 800),
        (900, 900),
        (1000, 1000),
    )
    budget = models.IntegerField(choices=budget_choices, default = 500)
    event_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s" % (self.name)
