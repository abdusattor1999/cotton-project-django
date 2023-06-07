from django import forms  
from .models import Cotton

class CottonForm(forms.ModelForm):
    class Meta:
        model = Cotton
        fields = "__all__"

    