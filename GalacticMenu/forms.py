from django import forms
from GalacticMenu.models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Product
        fields = ['name', 'opis', 'cena', 'kategorija', 'image']  # Избери само релевантни полиња
