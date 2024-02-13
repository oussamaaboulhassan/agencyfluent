from django import forms
from . import models

class Create_lead(forms.ModelForm):
    class Meta:
       model = models.Article
       fields = [
           "name", "email", "subject", "body"
       ]