from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'name': 'name', 'placeholder': 'Name *', 'class': 'bg-transparent border-color-white text-white', 'id': 'name'}))
    company = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'name': 'Organization', 'placeholder': 'Name of Organization  *', 'class': 'bg-transparent border-color-white medium-input', 'id': 'Organization'}))
    phone = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'name': 'phone', 'placeholder': 'Phone *', 'class': 'bg-transparent border-color-white medium-input', 'id': 'phone'}))

    job_title = forms.CharField( max_length=50, required=False, widget=forms.TextInput(attrs={'name': 'Job Title', 'placeholder': 'Job Title', 'class': 'bg-transparent border-color-white medium-input', 'id': 'Job Title '}))
    description = forms.CharField(widget=forms.Textarea(attrs={'name': 'comment', 'placeholder': 'A brief description of your need', 'class': 'bg-transparent border-color-white medium-textarea', 'id': 'comment'}))
    