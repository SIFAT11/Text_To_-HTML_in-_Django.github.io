from django import forms
from .models import Text
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(config_name='default'), label="Text Editor")

    class Meta:
        model = Text
        fields = ('body',)
