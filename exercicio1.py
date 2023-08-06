# Fernando A. S. C. de Vasconcellos - Turma 9
#  Se achar necessario, faça import de outras bibliotecas

# Crie a função que será avaliada no exercício aqui
def multiplas_operacoes(n1,n2):
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2 
    if n2 != 0: 
        divisao = n1/n2
    else:
        divisao = 0
    return soma, subtracao, multiplicacao, divisao
# Teste a sua função aqui (caso ache necessário)