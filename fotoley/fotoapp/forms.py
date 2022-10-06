from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    media = forms.FileField(required=False,
                            widget=forms.ClearableFileInput(
                                attrs=
                                {'multiple': False,
                                "class" : "is-medium file-label" },))
    caption = forms.CharField(required=True,
                widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Post some shit !!",    
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )
    class Meta:
        model = Post
        fields = ('media', 'caption')
        exclude = ('user',)
