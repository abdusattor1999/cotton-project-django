from django.shortcuts import render, redirect
from .forms import CottonForm
from .models import Cotton
# from django.conf.urls import 

def home_page(request):
    return render(request, 'home_page.html')

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
