from django.shortcuts import render ,redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
def index(request):
  products = Product.objects.all()
  sepetim = Sepet.objects.filter(alici = request.user) if request.user.is_authenticated else " "
  search = ""
  if request.GET.get('query'):
    search = request.GET.get('query')
    products = Product.objects.filter(
        Q(name__icontains = search)|
        Q(category__name__icontains = search)|
        Q(sub_category__name__icontains = search)
        ).distinct()
    
  if 'fav' in request.POST:
    if request.user.is_authenticated:
      productId = request.POST.get('productId')
      product = Product.objects.get(id = productId)#kullanıcı hangı ürüne tıklandıysa onu çektik
      if request.user in product.favorite.all():
        product.favorite.remove(request.user)
        messages.success(request, 'Ürün favorilerden Çıkarıldı')
      else:
        product.favorite.add(request.user)
        messages.success(request,'ürün Favorilere Eklendi')
      product.save()
      return redirect('index')
    else:
      messages.error(request,'Favoriye Eklemeniz için Giriş Yapmalısınız')  
      return redirect('index')
    
  if 'sepet' in request.POST:
    if request.user.is_authenticated:
      product = Product.objects.get(id = request.POST.get('productId'))
      adetForm = int(request.POST.get('adetForm'))
      if Sepet.objects.filter(alici = request.user, urun = product).exists():
        sepet = Sepet.objects.get(alici = request.user, urun = product)
        sepet.adet += adetForm
        sepet.total = sepet.urun.price * sepet.adet
        sepet.save()
        messages.success(request, 'Sepet Güncellendi')
      else:
        yeniSepet = Sepet.objects.create(
          alici =request.user ,
          urun = product,
          adet = adetForm,
          total = product.price * adetForm
        )            
        yeniSepet.save()
        messages.success(request,'Ürün Sepete Eklendi')
      return redirect('index')

  

  context = {
    'products':products,
    'search':search,
    'sepetim':sepetim
  }
  return render(request,'index.html', context)

def detail(request , productId):
  product = Product.objects.get(id = productId)
  context = {
    'product':product
  }
  return render(request, 'detail.html' , context)

@login_required(login_url='login')
def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) # formdan gelen bilgileri ve resmi form ile eşleştirdik
        if form.is_valid():
            newProduct = form.save(commit = False) # ürünü oluşturur ancak veritabanına göndermez
            newProduct.owner = request.user # satıcı bilgisini girişli olan kullanıcı olarak kaydeder
            newProduct.save()
            messages.success(request, 'Ürününüz oluşturuldu')
            return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'create.html', context)

@login_required(login_url='login')
def cart(request):
  sepetim = Sepet.objects.filter(alici = request.user)
  if 'remove' in request.POST:
    cartId = request.POST.get('cartId')
    sepet = Sepet.objects.get(id = cartId)
    sepet.delete()
    messages.success(request,'Ürün sepetden kaldırıldı')
    return redirect('cart')
  
  if 'update' in request.POST:
    sepet = Sepet.objects.get(id = request.POST.get('cartId'))
    adetForm = int(request.POST.get('adetForm'))
    sepet.adet = adetForm
    sepet.total = sepet.urun.price * sepet.adet
    sepet.save()
    messages.success(request,'Ürün Adetiniz Güncellendi')
    return redirect('cart')
  context = {
    'sepetim':sepetim
  }
  return render(request,'cart.html',context)