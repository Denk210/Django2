from django.db import models

# Create your models here.

from django.db import models

class History(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    user_solution = models.TextField(blank=True, null=True)
    correct_solution = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.a}x^2 + {self.b}x + {self.c} = 0'

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='news_images/')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title