from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostModelForm

# Create your views here.


# Get implies a single object
# filter implies a list of objects. query sets will help account for the repeated slug problem (Multiple Objects returned)
#
# def blog_post_detail_page(request, slug):
#     # queryset = get_object_or_404(BlogPost, slug=slug)
#     # queryset = BlogPost.objects.filter(slug=slug)
#     # if queryset.count() == 0:  # this will handle the multiple objects returned errors
#     #     raise Http404
#     # obj = queryset.first()
#     obj = get_object_or_404(BlogPost, slug=slug)
#     template_name = "blog_post_detail.html"
#     context = {"object": obj}
#     return render(request, template_name, context)


def blog_post_list_view(request):
    '''lists out objects, could be search. For search change the .all() to .filter(title__icontains='insert word')'''
    qs = BlogPost.objects.all().published()  # Objects is a django manager that allows me to call methods without modifying the model
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct() # <- this combines both query sets of the same class and uses the only ones there
    template_name = 'blog/list.html'
    context = {"object_list": qs}  # queryset -> list of objects
    return render(request, template_name, context)


# @login_required   # can use this -> (login_url='/login') instead of in the settings
@staff_member_required
def blog_post_create_view(request):
    '''  Create objects by using a form. request.user -> return something '''
    form = BlogPostModelForm(request.POST or None, request.FILES or None) # request.FILES is there since we declared the enctype in the HTML
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user # sets the data when created
        obj.save()

        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    ''' this is going to be 1 object or detail view'''
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"title": f"Update {obj.title}", 'form': form}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
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