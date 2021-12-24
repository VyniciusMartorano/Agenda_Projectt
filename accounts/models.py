from django.db import models
from contatos.models import Contato
from django import forms


class FormContatos(forms.ModelForm):
    class Meta:
        model = Contato
        #exclude exclui um componente do formulario no caso é so colocar
        #por exemplo exclude = ('mostrar',) NÃO ESQUECE DA VIRGULA PORRA
        exclude = ()


