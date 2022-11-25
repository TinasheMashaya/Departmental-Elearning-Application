from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args ,**keyargs):
    return render(request, "pages/home.html", {})

def about_view(request ,*args ,**keyargs):

    return render(request, "pages/about.html",{})

# Create your views here.
def department_view(request, *args ,**keyargs):
    return render(request,"pages/department.html" ,{})

def index_main(request, *args ,**keyargs):
    return render(request,"pages/index.html" ,{})

def student_dashboard(request, *args ,**keyargs):
    return render(request,"pages/student-dashboard-my-courses.html" ,{})

def course_detail(request,*args,**keyargs):
    return render(request ,"pages\courses-detail.html",{})