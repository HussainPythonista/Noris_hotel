from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method =='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username = request.POST['name']
        email= request.POST['email']
        password1= request.POST['password']
        password2= request.POST['re_password']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username Already Exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username, email=email, password=password1)
                user.save();
                return redirect('/')
        else:
            messages.error(request,"Password Does Not match")
            #return render(request,'register.html')
    
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Invalid Credential")
            return render(request,'login.html')
    else:
        return render(request,'login.html')
