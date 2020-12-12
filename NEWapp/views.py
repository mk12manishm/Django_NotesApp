from django.shortcuts import render,redirect
from NEWapp.models import Document
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from NEWapp.forms import Savenote
# Create your views here

@login_required
def editor(request):
    documents=Document.objects.filter(contactholder=request.user)
    if request.method=="POST":
        form=Savenote(request.POST or None)
        if form.is_valid():
            form.save(commit=False).contactholder=request.user
            form.save()
    return render(request,'editor.html',{'documents':documents})


def User_Login(request):
    return render(request,'user_Login.html')

def First_Page(request):
    return render(request,'first_Page.html')

@csrf_exempt
def register(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    username=request.POST['user_name']
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']
    email=request.POST['email']

    if password==confirm_password:
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('/First_page/')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already Taken')
            return redirect('/First_page/')
        else:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            messages.info(request,'User Created')
            return redirect('/First_page/')
    else:
        messages.info(request,'Password Not Matching')
        return redirect('/First_page/')
    return render(request,'first_Page.html')

@csrf_exempt
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print(user)
        print(username)
        if user is not None:
            auth.login(request,user)
            return redirect("/editor/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/User_Login')
    else:
        return render(request,'user_Login.html')

@login_required
def destroy(request,id):
    fees=Document.objects.get(pk=id)
    fees.delete()
    return redirect('/editor/')

def logout(request):
    auth.logout(request)
    return redirect('/First_page/')