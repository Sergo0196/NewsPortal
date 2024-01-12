from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', max_length=20)
    category_post = forms.CharField(label='Категория')
    class Meta:
        model = Post
        fields = [
            'title',
            'category_post',
        ]

class PostCreate(forms.ModelForm):
    title = forms.CharField(label='Заголовок', max_length=20)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'category',
        ]

        labels = {'text': 'Текст', 'author': 'Автор'}







