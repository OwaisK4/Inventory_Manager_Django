from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("<H2>HEY! Welcome to my website! </H2>")

def time_view(request):
    now = datetime.now()
    time = f"Current time is {now}"
    return HttpResponse(time)

def templatized_index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'test.html',context=my_dict)

def myself(request):
    return render(request, 'myself.html')

def image(request):
    return render(request, 'webapp/image.html')

def about_page(request):
    return render(request, 'webapp/index.html')
def components_page(request):
    return render(request, 'webapp/components.html')


# def templatized_view(request):
#     context = {
#         "Name" : "Owais Ali Khan",
#         "Age" : "20",
#         "Designation" : "Software Engineer",
#     }
#     return render(request, "printer.html", context)