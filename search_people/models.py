from django.db import models

class People(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    altura = models.FloatField()
    peso = models.FloatField()