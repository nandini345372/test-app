from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render(request,'student/home.html')


def create(request):
    form = Blogform()
    if request.method=='POST':
        form = Blogform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')


    context= {'form' : form}
    return render(request,'student/create.html',context)


def displayBlog(request):
    blog = BlogModel.objects.all()
    context = {'blog':blog}
    return render(request,'student/display.html',context)


def deletelist(request, id):
    blog = get_object_or_404(BlogModel, id = id)
    if request.method =="POST":
        blog.delete()
        return redirect("/")
    context = {}
    return render(request, "student/delete.html", context)

def updatelist(request, id):
    blog = get_object_or_404(BlogModel, id = id)
    form = Blogform(instance = blog)
    if(request.method=='POST'):
        form = Blogform(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form.save()
        return redirect('/')
    context ={'form':form}
    return render(request,'student/update.html',context)
