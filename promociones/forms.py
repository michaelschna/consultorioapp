from django import forms
from .models import Producto
import decimal

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['descripcion','precio']