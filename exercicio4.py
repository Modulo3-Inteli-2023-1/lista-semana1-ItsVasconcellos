#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    elementos_vistos = []
    for element in lista:
        if element in elementos_vistos:
            return True
        else:
            elementos_vistos.append(element)
    return False


# Teste a sua função aqui (caso ache necessário)