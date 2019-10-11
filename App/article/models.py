from django.db import models

class Author (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article (models.Model):
    title = models.CharField(max_length=120)
    start_time = models.DateField()
    end_time = models.DateField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.
