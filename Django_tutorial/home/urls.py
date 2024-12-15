from django.urls import path
from .views import *

urlpatterns = [
    path('home', home,name='home'),
    # path('welcome', welcome),
    path('', HomeView.as_view()),
    # path('authorized', authorized),
    path('authorized', AuthorizedView.as_view(),name='authorized'),
    path('login', LoginInterfaceView.as_view(),name='login'),
    path('logout', LogoutInterfaceView.as_view(),name='logout'),
    path('signup', SignupView.as_view(),name='signup'),
]
