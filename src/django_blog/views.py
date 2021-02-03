from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = "Hello there..."
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
    return render(request, "index.html", {"title": my_title})


def about_page(request):
    return render(request, "index.html", {"title": "About Us"})


def contact_page(request):
    return render(request, "index.html", {"title": "Contact Us"})

