from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
def msg(request):
    return HttpResponse("messege sented")
from backend.forms import productform

def form(request):
    frm=productform()
    # form=producttable.objects.filter(user=request.user)
    return render(request,"form.html",{"frm":frm})

def save(request):
    if request.POST:
        frm=productform(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('Blog')
    else:
        frm=productform()
    return render(request,"form.html",{"frm":frm})
from backend.models import producttable
def table(request):
    data=producttable.objects.all()
    return render(request,"table.html",{"data":data})
def delete(request,dataid):
    data=producttable.objects.filter(id=dataid)
    data.delete()
    return redirect(table)
def edit(request,dataid):
    edited=producttable.objects.get(id=dataid)
    if request.POST:
        frm=productform(request.POST,request.FILES,instance=edited)
        if frm.is_valid():
            frm.save()
            return redirect(table)
    else:
        frm=productform(instance=edited)
    return render(request,"edit.html",{"frm":frm})

from django.shortcuts import render
def blogpage(request):
    return render(request, 'Blog.html')