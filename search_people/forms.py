from django import forms
from search_people.models import People

class NewPersonForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['nome', 'data_nasc', 'cpf', 'sexo', 'altura', 'peso']