from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField() #This has to match the name attribute in the input tag
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)