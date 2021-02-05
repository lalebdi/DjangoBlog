from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost


# Get implies a single object
# filter implies a list of objects. query sets will help account for the repeated slug problem (Multiple Objects returned)

def blog_post_detail_page(request, slug):
    # queryset = get_object_or_404(BlogPost, slug=slug)
    # queryset = BlogPost.objects.filter(slug=slug)
    # if queryset.count() == 0:  # this will handle the multiple objects returned errors
    #     raise Http404
    # obj = queryset.first()
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)




'''
Can use this for dynamic error handling
  try:
        obj = BlogPost.objects.get(id=id) # this query -> database -> get the data -> django renders it
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
'''