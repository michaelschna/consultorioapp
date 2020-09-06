from django import forms
from .models import Medicos, Usuario

class MedicosForm(forms.ModelForm):
    class Meta:
        model=Medicos
        fields=['apellido','nombre','edad','email','sexo']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre','apellido','cedula','edad','email','sexo','tipousuario']

