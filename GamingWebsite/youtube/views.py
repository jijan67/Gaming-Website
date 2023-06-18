from django.shortcuts import render,HttpResponse,redirect
from .models import *


def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        content =request.POST['content']
        contact=Contact(name=name, email=email, content=content)
        contact.save()
        print(tnx)
        return redirect('tnx')
    return render(request, "index.html")

def tnx(request):
    return render(request,'tnx.html')
