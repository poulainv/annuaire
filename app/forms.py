from django import forms


class SubmissionForm(forms.Form):
    
    lastname = forms.CharField(label='Nom', max_length=100, required=True)
    firstname = forms.CharField(label='Prénom', max_length=100)
    email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Téléphone', max_length=100)
    project = forms.CharField(label='Mon projet en quelques mots', max_length=300, widget=forms.Textarea, required=True)
    url = forms.URLField(label='Lien vers le projet', required=True)
