from django.urls import path
from . views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('book/', book, name='book'),
    path('menu/', menu, name='menu'),
    path('menu_detail<int:id>/', menu_detail, name='menu_detail'),
]