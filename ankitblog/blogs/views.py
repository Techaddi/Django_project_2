from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blog, Title, Blog, Contact, About, Welcome
from django.contrib import messages

# Create your views here.
def index(request):
    title=Title.objects.all()
    welcome = Welcome.objects.all()
    return render(request, 'index.html',{'title':title,'welcome':welcome})

def about(request):
    abouts=About.objects.all()
    return render(request, 'about.html',{'abouts':abouts})

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        print(name, email, phone, message)
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        messages.info(request,'Detail send')
    

    return render(request, 'contact.html')

def post(request):
    blog1 = Blog.objects.all()
    return render(request, 'post.html',{'blog1':blog1})