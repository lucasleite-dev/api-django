from rest_framework import serializers
from .models import *


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "marca", "preco", "quantidade", "status"]
