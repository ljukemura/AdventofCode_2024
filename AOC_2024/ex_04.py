arquivo = 'ex_04_input.txt'

lista = []
lista_reverse = []
qnt_total = []
numero_de_listas = 0


def check_regra(lista):
    if len(lista) != len(set(lista)):
        return False
    
    if lista != sorted(lista) and lista != sorted(lista, reverse=True):
        return False

    for i in range(len(lista) - 1):
        if abs(lista[i] - lista[i + 1]) > 3:
            return False

    return True


with open(arquivo, 'r') as file:
    for linha in file:
        numero_de_listas += 1

        lista = linha.strip().split()
        lista = list(map(int, lista))
        print(lista)

        a = check_regra(lista=lista)
        print(a)
        if a:
            qnt_total.append(numero_de_listas)
            
        else:
            for i in range(len(lista)):
                lista_arrumada = lista[:i] + lista[i+1:]
                a = check_regra(lista=lista_arrumada)
                if a:
                    qnt_total.append(numero_de_listas)
                    break

print(qnt_total)
print(len(set(qnt_total)))