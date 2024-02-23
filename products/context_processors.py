from .models import *

def get_categories(request):
  categories = Category.objects.all()
  return {'categories':categories}

def goruntuleme(request):
  sepetim_length = Sepet.objects.filter(alici = request.user).count() if request.user.is_authenticated else ""
  return{'sepetim_length':sepetim_length}