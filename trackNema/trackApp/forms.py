from django import forms
from trackApp.models import Returnformnema

# class TrackappDocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('description', 'document', )
#         docfile = forms.FileField(label='Select a file')

class Returnformnema(forms.Form):
    docfile = forms.FileField(label='Select a file')
