from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'fecha_publicacion']
        widgets = {
            'fecha_publicacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }