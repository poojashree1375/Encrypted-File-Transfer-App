from django import forms

class UploadForm(forms.Form):
    file = forms.FileField(label="Choose File")
    expiry_minutes = forms.IntegerField(min_value=1, label="Expiry (minutes)")
