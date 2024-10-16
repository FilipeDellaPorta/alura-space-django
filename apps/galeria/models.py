from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        (" ", " "),
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("PLANETA", "Planeta"),
        ("GALÁXIA", "Galáxia"),
        ("BURACO NEGRO", "Buraco Negro"),
        ("SUPERMASSIVO BURACO NEGRO", "Supermassivo Buraco Negro"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA) #, default='')
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    descricao = models.TextField(null=False, blank=False)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        # return f"Fotografia {self.nome}"
        return self.nome
    
