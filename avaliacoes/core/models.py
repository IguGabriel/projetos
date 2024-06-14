from django.db import models
class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f"{self.usuario} - {self.pontuacao}"

class Review(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id}"
    

