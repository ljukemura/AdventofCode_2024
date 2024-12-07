arquivo = 'ex_03_input.txt'

lista = []
lista_reverse = []
qnt_total = []
numero_de_listas = 0

with open(arquivo, 'r') as file:
    for linha in file:
        numero_de_listas += 1

        lista = linha.strip().split()
        lista = list(map(int, lista))
        lista_reverse = sorted(lista, reverse=True)
        print(lista)
        print(lista_reverse == lista)
        print(len(lista) == len(set(lista)))

        if len(lista) == len(set(lista)):
            if lista == sorted(lista) or lista == lista_reverse:
                qnt_linha = 0
                for i in range(len(lista)-1): 
                    if abs(lista[i] - lista[i+1]) > 3:
                        qnt_linha += 1
                if qnt_linha == 0:
                    qnt_total.append(numero_de_listas)
            else:
                print(lista, " - UNSafe ordem")
                
        else:
            print(lista, " - UNSafe repetido")

print(qnt_total)
print(len(qnt_total))