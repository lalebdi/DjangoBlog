from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Hello there..."
    context = {"title": my_title}
    template_name = "index.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
    return HttpResponse(rendered_item)


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    return render(request, "index.html", {"title": "Contact Us"})


def example_page(request):
    context = {"title": "Example"}
    template_name = "index.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
