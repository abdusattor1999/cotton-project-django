from django.urls import path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('create/', cotton_add, name='create'),
    path('umumiy/', umumiy, name='umumiy'),
    path('cotton-list/', cotton_list, name='cotton_list'),
    path('cotton-list/<int:pk>/', cotton_list, name='cotton_list'),
    path('standart/', standart, name='standart'),
    # User
    path('login/', login_view, name='login'),
    path('sign-up/', register, name='register'),
    path('details/', details, name='details'),
    path('', home_page, name='home_page')
]
