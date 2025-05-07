from search_people.models import People
from ..tasks.pessoa_task import criar_pessoa, buscar_pessoa_por_cpf, atualizar_pessoa_por_id

def incluir_pessoa(dados):
    return criar_pessoa(dados)

def buscar_pessoa(cpf):
    return buscar_pessoa_por_cpf(cpf)

def atualizar_pessoa(pessoa_id, dados):
    return atualizar_pessoa_por_id(pessoa_id, dados)

def excluir_pessoa(pessoa_id):
    try:
        pessoa = People.objects.get(id=pessoa_id)
        pessoa.delete()
        return True
    except People.DoesNotExist:
        return False