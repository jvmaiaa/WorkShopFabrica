from django.db import models
from uuid import uuid4

class Author (models.Model):
    nome = models.CharField ( max_length = 100, primary_key = True )
    idade = models.CharField (max_length = 3 )


class Books (models.Model):
    id_do_livro = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    título = models.CharField ( max_length = 255 ) 
    data_de_publicação = models.IntegerField()
    estado = models.CharField(max_length = 50)
    página = models.IntegerField() 
    criado_por = models.DateField(auto_now_add = True) 
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
