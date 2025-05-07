import re
from ..models import People

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != int(cpf[i]):
            return False
    return True

def criar_pessoa(dados):
    if not validar_cpf(dados['cpf']):
        raise ValueError("CPF inválido")

    pessoa = People.objects.create(
        nome=dados['nome'],
        data_nasc=dados['data_nasc'],
        cpf=dados['cpf'],
        sexo=dados['sexo'],
        altura=dados['altura'],
        peso=dados['peso']
    )
    return {
        'id': pessoa.id,
        'nome': pessoa.nome,
        'cpf': pessoa.cpf
    }

def buscar_pessoa_por_cpf(cpf):
    try:
        pessoa = People.objects.get(cpf=cpf)
        return {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'cpf': pessoa.cpf,
            'sexo': pessoa.sexo,
            'altura': pessoa.altura,
            'peso': pessoa.peso
        }
    except People.DoesNotExist:
        return None

def atualizar_pessoa_por_id(pessoa_id, dados):
    try:
        pessoa = People.objects.get(id=pessoa_id)

        novo_cpf = dados.get('cpf')
        if novo_cpf and not validar_cpf(novo_cpf):
            raise ValueError("CPF inválido")

        pessoa.nome = dados.get('nome', pessoa.nome)
        pessoa.data_nasc = dados.get('data_nasc', pessoa.data_nasc)
        pessoa.cpf = novo_cpf if novo_cpf else pessoa.cpf
        pessoa.sexo = dados.get('sexo', pessoa.sexo)
        pessoa.altura = dados.get('altura', pessoa.altura)
        pessoa.peso = dados.get('peso', pessoa.peso)
        pessoa.save()
        return {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'cpf': pessoa.cpf
        }
    except People.DoesNotExist:
        return None
