from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Trip,Note
class HomeView(TemplateView):
    template_name='link/index.html'
# Create your views here.

def trip_list(request):
    trips=Trip.objects.all()
    context={
        "trips":trips
    }
    return render(request,'trip/index.html',context)