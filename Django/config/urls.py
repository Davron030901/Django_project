"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from my_app.views import index,about,hello,add
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('about/',about),
    path('hello/<str:first_name>',hello),
    path('add/<int:num1>/<int:num2>',add),
    path('movies/',include('movies.urls')),
    path('job/',include('job_board.urls')),
    path('link/',include('link.urls')),
    path('link_plant/',include('link_plant.urls')),
    path('trip/',include('trip.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
