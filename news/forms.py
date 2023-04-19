from .models import New
from django.forms import ModelForm

class NewtForm(ModelForm):
      class Meta:
        model = New
        fields = ['title', 'text1', 'data', 'image', 'fultext']