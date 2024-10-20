from django.urls import path
from .views import *


urlpatterns = [
    path('', electronic,name='home'),
    path('smartphone/',smartphone_gadget,name='smartphone'),
    path('office/',office_instrument,name='office'),
    path('computer/',computer_gadget,name='computer'),
    path('appliance/',appliance_machine,name='appliance'),
    path('kitchen/',kitchen_gadget,name='kitchen'),
    path('tarif/', packet, name='tarif'),
    path('texnic_detail/<int:id>',texnic_detail,name='texnic_detail'),
]