def eh_primo(numero):
    multiplos=0

    for contador in range(2,numero):
        if (numero % contador == 0):
            multiplos += 1

    if(multiplos==0):
        return True
    else:
        return False


def listagem_de_numeros_primos(final_da_lista:int):
    """
    final_da_lista --> é o tamanho do range que você quer. Se final_da_lista ==100, a lista será de 0 a 100
    Esta função retorna todos os numeros encontrados no range informado.
    ex:
    listagem_de_numeros_primos(10) retorna uma lista com os números primos encontrados numa lista de 0 a 10.
    listagem_de_numeros_primos(10) --> [2,3,5,7]
    """
    lista = [numero for numero in range(2,(final_da_lista+1))]
    lista_primos = []

    for numero in lista:
        if eh_primo(numero) == True:
            lista_primos.append(numero)

    return lista_primos

def maior_numero_primo_da_lista(final_da_lista:int):
    """
    Explicação geral das funções:
    - listagem_de_numeros_primos(10) retorna uma lista com os números primos encontrados numa lista de 0 a 10.
    - maior_numero_primo(10) retorna o maior número primo encontrado em uma lista de 0 a 10
    Atributo da função
    numero_final: O usuário irá informar o final do range de pesquisa.
    Ex maior_numero_primo(10000), numero_final está recebendo o valor 10000 e o range da lista será de 0 a 10000
    """
    lista = listagem_de_numeros_primos(final_da_lista)
    return max(lista)


def total_de_numeros_primos_encontrados(final_da_lista:int):
    lista = listagem_de_numeros_primos(final_da_lista)
    return f'Foram encontrados em um range de 0 a {final_da_lista}, um total de {len(lista)} numeros primos'