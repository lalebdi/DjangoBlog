from django.conf import settings
from django.db import models

# Create your models here.

# WHen you change the model you have to do 2 things:
# 1- go to settings.py and add the app to the installed apps list.
# 2- Ensure the changes that are mode are reflected in the database. -> done by typing the following in the terminal:
# a. python manage.py makemigrations
# b. python manage.py migrate
# The above is done so the database knows whats in the model.

User = settings.AUTH_USER_MODEL # -> whenever you need to add a user use this 🤷🏼‍♀️


class BlogPost(models.Model): # To get the query set of a user -> blogpost_set
    # id = models.IntegerField() or the primary key
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # slug is url encoded value e.g. hello world -> hello-world
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"
