from django.shortcuts import render,get_object_or_404,redirect

from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Profile,Link

class LinkListView(ListView):
    model=Link
    
class LinkCreateView(CreateView):
    model=Link
    fields='__all__'
    success_url=reverse_lazy('link-list')
    
class LinkUpdateView(UpdateView):
    model=Link
    fields=['name','url']
    success_url=reverse_lazy('link-list') 
    
class LinkDeleteView(DeleteView):
    model=Link
    success_url=reverse_lazy('link-list')
    
def root_link(request,profile_slug):
    profile=get_object_or_404(Link,slug=profile_slug)
    links=profile.links.all()
    links.click()
    return redirect(links.url)
    