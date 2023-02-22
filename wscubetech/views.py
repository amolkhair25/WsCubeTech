from django.http import HttpResponse
from django.shortcuts  import render

def homepage(request):
    return render(request,"index.html") # render use for page e.g index.html page


def about(request):
    return HttpResponse("Welcome")

def contact(request):
    return HttpResponse("9665776401")  

def name(request):
    return HttpResponse("Amol Khair")      

def course(request,courseid):
    return HttpResponse(courseid)         