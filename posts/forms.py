from .models import Post, Comment
from django import forms 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        widgets = {'comment': forms.Textarea(attrs={'class': 'form-control'})}