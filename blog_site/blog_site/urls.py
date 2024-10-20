
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('articles.urls')),
    path('second/',include('articles.urls')),
    path('second/button/',include('articles.urls')),
    path('second/login/',include('articles.urls')),
    path('index/',include('articles.urls')),
    path('second/click/', include('articles.urls')),
    path('second/login/viewport/',include('articles.urls')),
]
