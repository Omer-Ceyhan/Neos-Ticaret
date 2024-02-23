from .models import *
from django.forms import ModelForm

class ProductForm(ModelForm):
  class Meta:
    model = Product
    fields = ['name','content','category','image','price']

  def __init__(self,*args, **kwargs):
    super(ProductForm,self).__init__(*args, **kwargs)
    for name,field in self.fields.items():
      field.widget.attrs.update({'class':'form-control'})        