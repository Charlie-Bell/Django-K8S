from django import forms


# form
class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Name'})) # CharField is the database datatype. Widget is the frontend link.
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': 'E-Mail'})) # attrs configuration is here instead of in the Html.
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Your message here...', "rows": 5}))