from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        ex_user = CustomUser.objects.filter(email=email).first()
        if password1.isspace() or password1 != password2 or password2.isspace() or email.isspace():
            return redirect('register')
        elif ex_user:
            return HttpResponse('<h1>Bu email orqali oldin ro`yxatdan o`tilgan</h1>')
        else:
            user=CustomUser.objects.create_user(email=email,first_name=first_name,last_name=last_name,password=make_password(password1))
            login(request=request,user=user)
            return redirect('home')
    return render(
        request=request,
        template_name='auth/registor.html'
    )
def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request=request, email=email, password=password)
        if user and password!=None and email!=None:
            login(request=request, user=user)
            return redirect('home')
        else:
            return HttpResponse('<h1>email yoki passwordni xato kiritdingiz </h1>')
    return render(request=request,template_name='auth/login.html')
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')