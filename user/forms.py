from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','email','password1','password2']

  def __init__(self,*args, **kwargs):
      super(UserForm,self).__init__(*args, **kwargs)
      # self.fields['username'].widget.attrs.update({'class':'form-control'})
      self.fields['username'].help_text = "Kullanıcı adının gırılmesi zorunludur"
      for name,field in self.fields.items():
          field.widget.attrs.update({'class':'form-control mb-2'})
          field.help_text = ""
      