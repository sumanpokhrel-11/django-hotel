from django.shortcuts import render, redirect
from .models import Food
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):

    foods = Food.objects.all()
    return render(request, 'index.html', {'foods':foods})

def subscribe(request):
    if request.method =='POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email= request.POST['email']

        if password1==password2: 
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('subscribe')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('subscribe')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name,email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            return redirect('/')
    else:
        return render(request, 'subscribe.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')