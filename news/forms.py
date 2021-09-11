from .models import Articles
from django.forms import ModelForm, widgets

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            "title": widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи' 
            }),
            "anons": widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи' 
            }),
            "full_text": widgets.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи' 
            }),
        }