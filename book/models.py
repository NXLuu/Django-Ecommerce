from django.db import models
from author.models import AuthorProfile
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='products_category')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='products')
    price = models.IntegerField()
    summary = models.TextField()
    language = models.TextField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    author = models.ManyToManyField(AuthorProfile)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, )
    inventory = models.IntegerField(default=1)

    def __str__(self):
        return self.name