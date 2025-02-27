from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Reader(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='readers')

    def __str__(self):
        return self.name

# Create your models here.
