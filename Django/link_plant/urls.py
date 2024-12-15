from django.urls import path
from .views import *
urlpatterns = [
    path('', LinkListView.as_view(),name='link-list'),
    path('create/', LinkCreateView.as_view(),name='link-create'),
    path('<int:pk>/update/', LinkUpdateView.as_view(),name='link-update'),
    path('<int:pk>/delete/', LinkDeleteView.as_view(),name='link-delete'),
    path('<slug:profile_slug>/', root_link,name='profile'),
]