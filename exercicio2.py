#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def cumulativo(lista):
    nova_lista = [lista[0]]
    for i in range(1,len(lista)):
        nova_lista.append(nova_lista[i-1] + lista[i]) 
    return nova_lista


# Teste a sua função aqui (caso ache necessário)










