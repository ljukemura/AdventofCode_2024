arquivo = "ex_07_input.txt"


lista_result = []


def check_horizontal(matriz: list, linha: int, pos: int):
        concat_h = ''.join(str(matriz[linha][pos]) for pos in range(pos, pos + 4))
        if concat_h == "XMAS" or concat_h == "SAMX":
            lista_result.append(concat_h)
            print(linha, pos, "h")
        return


def check_vertical(matriz: list, linha: int, pos: int):
        concat_v = ''.join(str(matriz[linha][pos]) for linha in range(linha, linha + 4))
        if concat_v == "XMAS" or concat_v == "SAMX":
            lista_result.append(concat_v)
            print(linha, pos, "v")
        return

def check_diagonal_1(matriz: list, linha: int, pos: int):
        concat_d1 = ''.join(str(matriz[linha + i ][pos + i]) for i in range(0, 4))
        if concat_d1 == "XMAS" or concat_d1 == "SAMX":
            lista_result.append(concat_d1)
            print(linha, pos, "d1")
        return

def check_diagonal_2(matriz: list, linha: int, pos: int):
        concat_d2 = ''.join(str(matriz[linha + i][pos - i]) for i in range(0, 4))
        if concat_d2 == "XMAS" or concat_d2 == "SAMX":
            lista_result.append(concat_d2)
            print(linha, pos, "d2")
        return


with open(arquivo, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    matriz = [list(linha.strip()) for linha in linhas]

    print(len(matriz), ' Tamanho matriz')


for linha in range(len(matriz)):
    for pos in range(len(matriz[linha])):
        flag_h = pos + 4 <= len(matriz[linha])
        flag_v = linha + 4 <= len(matriz)
        flag_d2 = pos - 3 >= 0

        if flag_h:
            check_horizontal(matriz=matriz, linha=linha, pos=pos)
            if flag_v:
                check_diagonal_1(matriz=matriz, linha=linha, pos=pos)
        if flag_v:
            check_vertical(matriz=matriz, linha=linha, pos=pos)
            if flag_d2:
                check_diagonal_2(matriz=matriz, linha=linha, pos=pos)

print(lista_result)
print(len(lista_result), " - Resposta final")
