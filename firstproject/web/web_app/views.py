from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, "index.html")

def reg(request):
    if request.method =='POST':
        
        uname= request.POST['name']
        email= request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username already taken')
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('reg')
            else:
                user=User.objects.create_user(username=uname,email=email, password=password)
                user.save()
                
        else:
            messages.info(request,'password not match') 
            return redirect('reg')       
        return redirect('login')
       
      
    return render(request, "register.html")


def log(request):
    if request.method =='POST': 
        username= request.POST['user']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
          
        else:
            messages.info(request, "invalid credential")
            return redirect('login')

    return render(request, "login.html")

def logoutfrom(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return redirect('login')





