from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.
def register(request):
  
  form = UserForm()
  if request.method == 'POST': 
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'başarılı bir şekilde kayı oldunuz')
        return redirect('login')
    
        print(request.POST)
  context = {
    'form':form
  }
  return render(request,'register.html',context)


def userLogin(request):
  if request.method == 'POST':
    kullanici= request.POST.get('kullanici_form')
    sifre = request.POST.get('sifre_form') 

    user = authenticate(request,username = kullanici,password = sifre)

    if user is not None:
      login(request, user)
      messages.success(request,'başarılı bir sekilde giriş yaptınız')
      next = request.GET.get('next')
      if next:
        return redirect(next)
      else:
        return redirect('index')
      return redirect('index')
    else:
      messages.error(request,"Kullanıcı adı veya şifre hatalı")
  return render(request,'login.html')

def userLogout(request):
  logout(request)
  messages.success(request,'çıkısı yapıldı')
  return redirect('index')