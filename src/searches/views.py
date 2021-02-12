from django.shortcuts import render
from blog.models import BlogPost
from .models import SearchQuery
# Create your views here. then add it to the project urls


def search_view(request):
    query = request.GET.get('q', None)  # q is the name of the input/ None is for the default value
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query) # this will save the query every time
        blog_list = BlogPost.objetcs.search(query=query)
        context['blog_list'] = blog_list
    return render(request, 'searches/view.html', context)