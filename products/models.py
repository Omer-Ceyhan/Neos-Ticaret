from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
  name = models.CharField(max_length=100, verbose_name='kategori Adı')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = "Kategoriler"
    verbose_name = "Kategori"
  
class SubCategory(models.Model):
  name = models.CharField(max_length=100, verbose_name='Alt Kategori')
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = "Alt Kategoriler"
    verbose_name = "Alt Kategori"
class Product(models.Model):
  owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Satıcı", null = True, editable = False)
  created_at = models.DateTimeField(auto_now_add = True, verbose_name = "Oluşturulma Tarihi", null = True)
  category = models.ForeignKey(Category, on_delete = models.SET_NULL , null = True, verbose_name="Kategori")
  sub_category = models.ManyToManyField(SubCategory,verbose_name='Alt Kategori')
  name = models.CharField(max_length=100, verbose_name="Ürün ismi")
  content = RichTextField(verbose_name="Ürün Açıklaması")
  price = models.IntegerField(("Ürün Fiyatı"))
  image = models.FileField(upload_to= "products/" , null=True , default="")
  favorite = models.ManyToManyField(User, blank=True, related_name="favorites_user")

  
  

  def __str__(self):
      return self.name # admin panelindeki idleri türkçe yapmaya yarıyor
  
  class Meta:
    verbose_name_plural = "Ürünler"
    verbose_name = "ürün" 
  

  #many to one = ForignKEy
  #many to many
  #one to one  
    

    #SEPETE EKLE
  #Alıcı
  #Ürün
  #adet
  #Toplam Tutar
  
class Sepet(models.Model):
  alici = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="Sepete Ekleyen")
  urun = models.ForeignKey(Product, on_delete= models.CASCADE, verbose_name="Sepete Eklenen Ürün")
  adet = models.IntegerField(("Sepete Eklenen Adet"))
  total = models.DecimalField(("Toplam Tutar"), max_digits = 10 , decimal_places=2)
  created_at = models.DateTimeField(auto_now_add = True , verbose_name="sepete eklenme tarihi")
  updated_at= models.DateTimeField(auto_now_add=True , verbose_name="Güncelleme Tarihi")

  def __str__(self):
    return self.alici.username
  
  class Meta:
    verbose_name_plural = "Sepetteki Ürünler"
    verbose_name = "Ürün"


  def save(self,*args, **kwargs):
    self.total = self.urun.price * self.adet
    super().save(*args, **kwargs)