from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def project(request):
    return render(request,'projects.html')

def about(request):
    return redirect('/')

def resume(request):
    return render(request,"resume.html")

from .models import enquiry
def contact(request):
    if request.method=="POST":
        name=request.POST.get("myname")
        email=request.POST.get("myemail")
        description=request.POST.get("mydesc")
        e=enquiry()
        e.name=name
        e.email=email
        e.description=description
        e.save()
        return render(request,'contact.html')
    else:
        return render(request,"contact.html")