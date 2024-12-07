arquivo = "ex_08_input.txt"


lista_result = []
gabarito_1 = ["M", "M", "A", "S", "S"]
gabarito_2 = ["M", "S", "A", "M", "S"]
gabarito_3 = ["S", "S", "A", "M", "M"]
gabarito_4 = ["S", "M", "A", "S", "M"]



def check_padrao(matriz: list, linha: int, pos: int):
    padrao = [matriz[linha][pos], matriz[linha][pos+2], matriz[linha+1][pos+1], matriz[linha+2][pos], matriz[linha+2][pos+2]]
    if padrao == gabarito_1:
        concat_p1 = str(linha)+"-"+str(pos)+"-g1"
        lista_result.append(concat_p1)
    if padrao == gabarito_2:
        concat_p2 = str(linha)+"-"+str(pos)+"-g2"
        lista_result.append(concat_p2)
    if padrao == gabarito_3:
        concat_p3 = str(linha)+"-"+str(pos)+"-g3"
        lista_result.append(concat_p3)
    if padrao == gabarito_4:
        concat_p4 = str(linha)+"-"+str(pos)+"-g4"
        lista_result.append(concat_p4)
    return

with open(arquivo, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    matriz = [list(linha.strip()) for linha in linhas]

    print(len(matriz), ' Tamanho matriz')

for linha in range(len(matriz)-2):
    for pos in range(len(matriz[linha])-2):

        check_padrao(matriz=matriz, linha=linha, pos=pos)



print(lista_result)
print(len(lista_result), " - Resposta final")
