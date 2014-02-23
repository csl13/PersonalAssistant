from django.http import HttpResponse
from django.template import Template, Context
from django.template.response import TemplateResponse

def home_page(request):
    return TemplateResponse(request, "index.html", {})

def hello(request):
	return HttpResponse("Hello world")

def my_404_view(request):
    return HttpResponse("page isn't exits!");
