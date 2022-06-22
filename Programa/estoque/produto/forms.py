from django.forms import ModelForm, TextInput, Select, Textarea
from .models import Produtos

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'cor', 'flag']
        # fields = '__all__'
        # exclude = ['criado', 'modificado']
        widgets = {
            'produto': TextInput(attrs={'class':'input'}),
            'cor': Select(attrs={'class':'select'}),
            #'flag': TextInput(attrs={'class':'checkbox'})
        }
