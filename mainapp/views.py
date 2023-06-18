from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from .models import Cotton
from django.http import HttpResponse
# from django.conf.urls import 

def home_page(request):
    return render(request, 'index.html')

def umumiy(request):
    return render(request, 'mainapp/umumiy.html')


def cotton_add(request):
    if request.method == 'POST':
        form = CottonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mainapp:home_page')
    else:
        form = CottonForm()
        return render(request, 'mainapp/cotton_create.html', {'form':form})
    

def cotton_list(request, pk=False):
    if int(pk) == 2:
        cottons = Cotton.objects.filter(local=True)
    elif int(pk) == 1:
        cottons = Cotton.objects.filter(popular=True)
    else:
        cottons = Cotton.objects.all()

    return render(request, 'mainapp/cottonlist.html', {'cottons':cottons})


# User
def register(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return redirect('mainapp:login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html',{'form':user_form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('mainapp:details')
            else:
                return HttpResponse("Validatsiya xato !")     
        else:
            return HttpResponse('Malumot topilmadi !')     
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form':form})

def details(request):
    user = request.user
    return render(request, 'account/details.html', {'user':user})
