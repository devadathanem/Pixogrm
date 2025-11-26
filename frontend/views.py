from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,"Index.html")
def Gallery(request):
    data=producttable.objects.all()
    return render(request,"Gallery.html",{"data":data})
def Services(request):
    return render(request,"Services.html")
def Blog(request):
    data=producttable.objects.all()
    return render(request,"Blog.html",{"data":data})
def About(request):
    return render(request,"About.html")
from backend.models import producttable

def Blogpage(request):
    return render(request, 'Blog.html')
