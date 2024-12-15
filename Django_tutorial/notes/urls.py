from django.urls import path
from .views import *

urlpatterns = [
    # path('notes', list),
    path('notes', NoteListView.as_view(),name='notes.list'),
    # path('notes/<int:pk>', detail),
    path('notes/<int:pk>', NoteDetailView.as_view(),name='notes.detail'),
    path('notes/<int:pk>/delete', NoteDeleteView.as_view(),name='notes.delete'),
    path('notes/<int:pk>/edit', NoteUpdateView.as_view(),name='notes.update'),
path('notes/new', NoteCreateView.as_view(),name='notes.new'),
]