from django import forms
 
class GalleryForm(forms.Form):
    image_field = forms.ImageField(label="Upload The Image Here")