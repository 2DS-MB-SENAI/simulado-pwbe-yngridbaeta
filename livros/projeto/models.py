from django.db import models

#titulo 50, autor 30, paginas int
class Livros(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    pagina = models.IntegerField()

    def __str__(self):
        return self.titulo
