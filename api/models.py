from django.db import models
from django.db.models.fields import CharField

class Client(models.Model):
    STAGES_AVAILABLE = (
        ('Documents', 'Aguardando assinatura de documentos'),
        ('Resources', 'Aguardando transferência de recursos'),
        ('Management', 'Gestão de patrimônio ativa'),
    )

    name = models.CharField(max_length=255, blank=False)
    cpf = models.CharField(max_length=11, blank=False, unique=True)
    stage = CharField(max_length=255, choices= STAGES_AVAILABLE)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'