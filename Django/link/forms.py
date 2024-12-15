from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    # name=forms.CharField(max_length=50)
    # url=forms.URLField(max_length=200)
    # slug=forms.SlugField(required=False)
    class Meta:
        model=Link
        fields=['name','url','slug']