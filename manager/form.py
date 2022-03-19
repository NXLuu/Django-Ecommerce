from django import forms
from shop.models import *

class CreatePostForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = "__all__"  