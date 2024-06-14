from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=64)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']
        labels = {
            'nota': 'Nota',
            'comentario': 'Comentário'
        }
        widgets = {
            'nota': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),  # Exemplo para notas de 1 a 5
            'comentario': forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CadastroForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
