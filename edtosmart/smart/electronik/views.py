from django.shortcuts import render
from .models import Electronik
from django.contrib.auth.decorators import login_required


# @login_required
def electronic(request):
    texnicalar = Electronik.objects.all().order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'texnikalar': texnicalar
    }
    return render(
        request=request,
        template_name='electronic.html',
        context=context
    )


# @login_required
def smartphone_gadget(request):
    texnicalar = Electronik.objects.filter(category='smartphone_gadget').order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'texnikalar': texnicalar
    }
    return render(
        request=request,
        template_name='electronic.html',
        context=context
    )


# @login_required
def office_instrument(request):
    texnicalar = Electronik.objects.filter(category='office_instrument').order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'texnikalar': texnicalar
    }
    return render(
        request=request,
        template_name='electronic.html',
        context=context
    )


# @login_required
def computer_gadget(request):
    texnicalar = Electronik.objects.filter(category='computer_gadget').order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'texnikalar': texnicalar
    }
    return render(
        request=request,
        template_name='electronic.html',
        context=context
    )
def appliance_machine(request):
    texnicalar = Electronik.objects.filter(category='appliance_machine').order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'texnikalar': texnicalar
    }
    return render(
        request=request,
        template_name='electronic.html',
        context=context
    )
def kitchen_gadget(request):
    texnicalar = Electronik.objects.filter(category='kitchen_gadget').order_by('-id')  # ==SELECT*FROM maqola;
    context = {
        'texnikalar': texnicalar
    }
    return render(
        request=request,
        template_name='electronic.html',
        context=context
    )

def texnic_detail(request, id):
    detail = Electronik.objects.get(id=id)
    contex = {
        "detail": detail
    }
    return render(request=request, template_name='texnic.html', context=contex)
def packet(request):
    return render(request, 'packet.html')



# Create your views here.
