from django.db import models
from author.models import AuthorProfile

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

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='products')
    price = models.IntegerField()
    details = models.TextField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=None, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE, null=True)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, )
    inventory = models.IntegerField(default=1)

    def __str__(self):
        return self.name

# class Menu(models.Model):
#     name = models.CharField(max_length=30)
# class Item(models.Model):
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     description = models.CharField(max_length=100)
#     price = models.FloatField(blank=True,null=True)


