from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from store.models import Book
from store.models import Category

@login_required(login_url="signin")
def home(request):
    data={}
    storedata=None
    categorydata=Category.objects.all()

    storedataid=request.GET.get('category')
    if storedataid:
        storedata=Book.objects.filter(category=storedataid)
    else:
        storedata=Book.objects.all()
    data={
        "storedata":storedata,
        "categorydata":categorydata,
    }
    return render(request,"home.html",data)
def signup (request):
    try:
        if request.method=="POST":
            uname=request.POST.get("username")
            email=request.POST.get("email")
            pass1=request.POST.get("password1")
            pass2=request.POST.get("password2")
            if pass1 != pass2:
                return HttpResponse ("Your password And Confirm Password does not match")
            else:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect("signin")
    except:
        pass
    return render(request,"Signup.html")

def signin (request):
    try:
        if request.method=="POST":
            uname=request.POST.get("username")
            pass1=request.POST.get("pass")
            my_user=authenticate(request,username=uname,password=pass1)
            if my_user is not None:
                login(request,my_user)
                return redirect ("home")
            else:
                return HttpResponse ("Password does not match")
    except:
        pass
    return render (request,"Signin.html")

def logoutpage (request):
    logout(request)
    return redirect ("signin")

# Create your views here.
