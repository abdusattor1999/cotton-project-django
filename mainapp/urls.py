from django.urls import path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('create/', cotton_add, name='create'),
    path('umumiy/', umumiy, name='umumiy'),
    path('cotton-list/', cotton_list, name='cotton_list'),
    path('cotton-list/<int:pk>/', cotton_list, name='cotton_list'),
    path('', home_page, name='home_page')
]
