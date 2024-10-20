
from django.shortcuts import render, redirect
from .models import *


def about(request):
    info = Company.objects.all().order_by('-id')
    context = {
        'info': info,
        'html_name': 'about',
        'title': 'Company'
    }
    return render(request, 'about/index.html', context=context)


def employees_info(request):
    info = Employees.objects.all().order_by('-position')
    context = {
        'info': info,
        'html_name': 'employees_info',
        'title': 'Employees'
    }
    return render(request, 'about/index.html', context=context)


def report(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        f = Report(name=name, email=email, message=message)
        if name.strip() == '' and email.strip() == '':
            return redirect('report')
        else:
            f.save()
            return redirect('about')
    else:
        return render(request=request, template_name='about/index.html', context={
            'html_name': 'report',
            'title': 'Report',
        })
