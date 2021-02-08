from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField() #This has to match the name attribute in the input tag
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError("This is not a valid email. Don't use .edu 🙄")
        return email