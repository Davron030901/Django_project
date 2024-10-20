from django.urls import path
from .views import *


urlpatterns = [
    path('home/', maqola,name='home'),
    path('world/',world_news,name='world'),
    path('sport/',sports_news,name='sport'),
    path('local',local_news,name='local'),
    path('article_detail/<int:id>',article_detail,name='article_detail')
]