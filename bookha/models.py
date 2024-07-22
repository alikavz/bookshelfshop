from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2) # ta 5 ragham save kun ke 2 raghamesh ashaare
    covers = models.ImageField(upload_to='covers/', blank=True)  # pillow nasb shavad ghablesh va setting, urls/config modify shavand


    def __str__(self):
        return f'{self.author}: {self.title}'

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    Which_book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}:{self.text}'


