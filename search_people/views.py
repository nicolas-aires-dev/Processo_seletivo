# search_people/views.py
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .services.pessoa_service import incluir_pessoa, buscar_pessoa, atualizar_pessoa, excluir_pessoa
from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


@csrf_exempt
def pessoa_view(request, cpf=None):

    if request.method == 'OPTIONS':
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        response = JsonResponse({'mensagem': 'Pessoa criada com sucesso!'})
        response["Access-Control-Allow-Origin"] = "*"
        return response

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            resultado = incluir_pessoa(data)
            return JsonResponse({'mensagem': 'Pessoa criada com sucesso!', 'pessoa': resultado}, status=201)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    
    elif request.method == 'GET':
        try:
            cpf = request.GET.get('cpf')
            if not cpf:
                return JsonResponse({'erro': 'CPF não informado'}, status=400)
            
            pessoa = buscar_pessoa(cpf)
            if pessoa:
                return JsonResponse({'pessoa': pessoa}, status=200)
            else:
                return JsonResponse({'erro': 'Pessoa não encontrada'}, status=404)
        
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)

    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
            pessoa_id = data.get('id')
            if not pessoa_id:
                return JsonResponse({'erro': 'ID não informado'}, status=400)
            
            resultado = atualizar_pessoa(pessoa_id, data)
            if resultado:
                return JsonResponse({'mensagem': 'Pessoa atualizada com sucesso!', 'pessoa': resultado}, status=200)
            else:
                return JsonResponse({'erro': 'Pessoa não encontrada'}, status=404)
        
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    
    elif request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            pessoa_id = data.get('id')
            if not pessoa_id:
                return JsonResponse({'erro': 'ID não informado'}, status=400)

            sucesso = excluir_pessoa(pessoa_id)
            if sucesso:
                return JsonResponse({'mensagem': 'Pessoa excluída com sucesso!'}, status=200)
            else:
                return JsonResponse({'erro': 'Pessoa não encontrada'}, status=404)
        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
        
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)
    
@csrf_exempt
def calcular_peso_ideal(request, pessoa_id=None):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sexo = data.get('sexo')
            altura = data.get('altura')

            if not sexo or not altura:
                return JsonResponse({'erro': 'Sexo e altura são obrigatórios.'}, status=400)

            if sexo == 'M':
                peso_ideal = (72.7 * altura) - 58
            elif sexo == 'F':
                peso_ideal = (62.1 * altura) - 44.7
            else:
                return JsonResponse({'erro': 'Sexo inválido.'}, status=400)

            return JsonResponse({'peso_ideal': round(peso_ideal, 2)}, status=200)

        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=400)
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)