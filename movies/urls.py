from django.urls import path
from movies.views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('about/',about,name='about'),    
]