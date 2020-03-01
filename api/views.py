from .models import *
from .serializers import *
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class ProdutoList(APIView):
    def get(self, request):
        try:
            lista_produtos = Produto.objects.all()
            serializer = ProdutoSerializer(lista_produtos, many=True)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = ProdutoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProdutoDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero"}, status=status.HTTP_400_BAD_REQUEST)
            produto = Produto.objects.get(pk=pk)
            serializer = ProdutoSerializer(produto)
            return Response(serializer.data)
        except Produto.DoesNotExit:
            return JsonResponse({'mensagem': "Esse produto não existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero"}, status=status.HTTP_400_BAD_REQUEST)
            produto = Produto.objects.get(pk=pk)
            serializer = ProdutoSerializer(produto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Produto.DoesNotExist:
            return JsonResponse({'mensagem': "Esse produto não existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return  JsonResponse({'mensagem': "O ID deve ser maior que zero"}, status=status.HTTP_400_BAD_REQUEST)
            produto = Produto.objects.get(pk=pk)
            produto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Produto.DoesNotExist:
            return JsonResponse({'mensagem': "Esse produto não existe"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return  JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
