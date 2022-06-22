from django.forms import ModelForm
from .models import NotasEntradas
from django.forms import TextInput, Select, Textarea

class NotasEntradasForm(ModelForm):
    class Meta:
        model = NotasEntradas
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
