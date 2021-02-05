from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import BlogPost


def blog_post_detail_page(request, id):
    try:
        obj = BlogPost.objects.get(id=id) # this query -> database -> get the data -> django renders it
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

