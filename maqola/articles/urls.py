from django.urls import path
from .views import main,second,button,login,index,click,viewport

urlpatterns=[
    path('',main,name="main"),
    path('second/',second,name="second"),
    path('button/',button,name="button"),
    path('login/',login,name="login"),
    path('index/',index,name="index"),
    path('click/',click,name="button"),
    path('viewport/',viewport,name="viewport"),
]