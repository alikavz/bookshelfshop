from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2) # ta 5 ragham save kun ke 2 raghamesh ashaare

    def __str__(self):
        return f'{self.author}: {self.title}'

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

