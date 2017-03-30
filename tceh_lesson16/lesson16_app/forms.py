from django import forms
from django.core.exceptions import ValidationError


class BlogPostForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise ValidationError('Title is too short')
        elif len(title) > 140:
            raise ValidationError('Title is too long')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise ValidationError('Text is too short')
        elif len(text) > 3500:
            raise ValidationError('Text is too long')
        return text
