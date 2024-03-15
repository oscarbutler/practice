from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    email = models.EmailField()
    # And whatever other custom fields here; maybe make a ForeignKey link to User? Whatever.

class Table(models.Model):
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

class Reservation(models.Model):
    table = models.ForeignKey('Table', on_delete=Models.CASCADE)
    party = models.ForeignKey('Customer', on_delete=Models.CASCADE)
    spot = models.DateField()