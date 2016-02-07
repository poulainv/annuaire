#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django import forms


class SubmissionForm(forms.Form):
    
    lastname = forms.CharField(max_length=100, required=True,                       widget=forms.TextInput(attrs={'placeholder' : 'NOM', 'id': 'form-lastname'}))
    firstname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'PRENOM', 'id': 'form-firstname'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'EMAIL', 'id': 'form-email'}))
    phone = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'placeholder': 'TELEPHONE', 'id': 'form-phone'}))
    project_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'NOM DU PROJET', 'id': 'form-project-name' }))
    url = forms.URLField(required=True, widget=forms.TextInput(attrs={'placeholder': 'URL', 'id': 'form-url' }))
    project = forms.CharField(max_length=300, required=True, widget=forms.Textarea(attrs={'placeholder': 'DITES-NOUS EN PLUS SUR LE PROJET QUE VOUS SOUHAITEZ AJOUTER OU BIEN MODIFIER', 'id': 'form-project'}))
