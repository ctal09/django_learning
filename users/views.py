from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello, world! This is the home page of the users app.")

def username(request, id):
    response = HttpResponse()
    response.content = """Hello, user with ID {}!!""".format(id)
    return response

def education(request,id):
    return HttpResponse("This is the education page of the user {} app.".format(id))

def experience(request, id):
    return HttpResponse("This is the experience page of the user {} app.".format(id))