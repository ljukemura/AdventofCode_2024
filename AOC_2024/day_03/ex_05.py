import re

arquivo = "ex_05_input.txt"
exemplo = r"mul\(\d{1,3}\,\d{1,3}\)"
lista = [] 

def busca_mul(string: str, pattern: str) -> list[str]:

    resposta = re.findall(pattern, string)
    return resposta



with open(arquivo, 'r') as file:
    conteudo = file.read()  
    print(conteudo)

    a = busca_mul(string=conteudo, pattern=exemplo)
    print(a)
    for i in a:
        numero = re.findall(r"\d+", i) 

        multiplcacao = int(numero[0]) * int(numero[1])
        lista.append(multiplcacao)


print(lista)
print(sum(lista))

