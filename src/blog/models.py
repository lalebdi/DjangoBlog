from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone

# Create your models here.

# WHen you change the model you have to do 2 things:
# 1- go to settings.py and add the app to the installed apps list.
# 2- Ensure the changes that are mode are reflected in the database. -> done by typing the following in the terminal:
# a. python manage.py makemigrations
# b. python manage.py migrate
# The above is done so the database knows whats in the model.

User = settings.AUTH_USER_MODEL # -> whenever you need to add a user use this 🤷🏼‍♀️


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # same thing as BlogPost.objects.all()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (Q(title__icontains=query) |
                  Q(content__icontains=query) |
                  Q(slug__icontains=query) |
                  Q(user__first_name__icontains=query) |
                  Q(user__last_name__icontains=query))
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self): # this method calls the published method above
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model): # To get the query set of a user -> blogpost_set
    # id = models.IntegerField() or the primary key
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)  # slug is url encoded value e.g. hello world -> hello-world
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp'] # the'-' to get the most recent one first

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
