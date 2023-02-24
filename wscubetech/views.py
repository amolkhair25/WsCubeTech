from django.http import HttpResponse
from django.shortcuts  import render

def homepage(request):
    data={
        'title':'Home new',
        'bdata':'Welcome to Django',
        'clist':['PHP','Java','Django'], # list in for loop
        'Students_details':[
            {'name':'Amol','phone':'9665776401'},# dictionary in list in for loop
            {'name':'Rahul','phone':'7709115186'}
        ],
        'num':[10,20,30,40,50]# for if else condition
    }
    return render(request,"index.html",data) # passing data from django views to a templates


def about(request):
    return HttpResponse("Welcome")

def contact(request):
    return HttpResponse("9665776401")  

def name(request):
    return HttpResponse("Amol Khair")      

def course(request,courseid):
    return HttpResponse(courseid)         