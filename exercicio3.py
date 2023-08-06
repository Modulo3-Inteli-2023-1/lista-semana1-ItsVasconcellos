# Fernando A. S. C. de Vasconcellos - Turma 9
#  Se achar necessario, faça import de outras bibliotecas
# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista):
    resultado = 0
    for lista_interna in lista:
        for elemento in lista_interna:
            resultado += elemento
    return resultado

# Teste a sua função aqui (caso ache necessário)










