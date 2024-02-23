from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'owner', 'price', 'created_at'] # listede hangi bilgilerin görüneceğini belirler
  list_filter = ['owner'] # hangi bilgilere göre filtreleme yapılabileceğini belirler (sağ tarafa filtre ekler)
  search_fields = ['owner__username__icontains', 'name'] # arama inputu oluşturur ve hangi bilgilere arama yapabileceğimizi belirler
  readonly_fields = ['owner', 'id', 'created_at'] # Hangi inputların sadece okunabilir olacağını belirler
  # list_per_page = 2 # Sayfa başına kaç tane öğe göstereceğini belirler
  list_display_links = ['name', 'owner'] # hangilerinin tıklanabilir olmasını belirler
    # ordering = ['-created_at'] # hangi bilgiye göre sıralanacağını belirler
  date_hierarchy = 'created_at' # Tarihe göre filtreleme yapmamızı sağlar
  list_editable = ['price'] # listede hangi alanı düzenleyebileceğimizi belirler


class SepetAdmin(admin.ModelAdmin):
    list_display = ['alici','urun','total','created_at','updated_at']
    lister_filter = ['alici']
    search_fields = ['alici__username__icontains','urun_name_icontains']
    readonly_fields = ['total','created_at','updated_at']
    date_hierarchy = 'created_at'

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Sepet, SepetAdmin)