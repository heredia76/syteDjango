from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def articles(request, year):
    return HttpResponse(' O ano enviado foi :' + str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 28},
        {'nome': 'MariAna', 'idade': 30}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0 }


def fname(request, nome):
    result = lerDoBanco(nome)
    print(result)
    return HttpResponse(result)

