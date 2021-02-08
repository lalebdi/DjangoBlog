from django.db import models

# Create your models here.

# WHen you change the model you have to do 2 things:
# 1- go to settings.py and add the app to the installed apps list.
# 2- Ensure the changes that are mode are reflected in the database. -> done by typing the following in the terminal:
# a. python manage.py makemigrations
# b. python manage.py migrate
# The above is done so the database knows whats in the model.


class BlogPost(models.Model):
    # id = models.IntegerField() or the primary key
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # slug is url encoded value e.g. hello world -> hello-world
    content = models.TextField(null=True, blank=True)