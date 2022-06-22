from django.forms import ModelForm
from .models import NotasSaidas
from django.forms import TextInput, Select, Textarea

class NotasSaidasForm(ModelForm):
    class Meta:
        model = NotasSaidas
        fields = [
            'produto',
            'quantidade',
            'preco',
        ]
        widgets = {
            'produto': Select(attrs={'class':'input'}),
            'quantidade': TextInput(attrs={'class':'input', 'type':'number'}),
            'preco': TextInput(attrs={'class':'input','type':'number','step':'0.01'})
        }