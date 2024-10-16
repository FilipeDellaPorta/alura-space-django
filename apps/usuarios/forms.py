from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
           attrs={
                "class": "form-control",
                "placeholder": "Ex: Joao Silva"
            } 
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Joao Silva"
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: joaosilva@xpto.com"
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Digite sua senha"
            }
        )
    )
    confirmacao_senha=forms.CharField(
        label='Confirmação de senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Digite sua senha mais uma vez"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome= self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserir espaços neste campo!")
            else:
                return nome
            
    
    def clean_confirmacao_senha(self):
         senha = self.cleaned_data.get("senha")
         confirmacao_senha = self.cleaned_data.get("confirmacao_senha")

         if senha and confirmacao_senha:
              if senha != confirmacao_senha:
                   raise forms.ValidationError("Senhas divergentes!")
              else:
                  return confirmacao_senha