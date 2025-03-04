arquivo = 'ex_02_input.txt'

lista_1 = []
lista_2 = []
total = 0
list_total = []

with open(arquivo, 'r') as file:
    for linha in file:
        valores = linha.split()
        lista_1.append(int(valores[0])) 
        lista_2.append(int(valores[1])) 

print("Lista 1:", lista_1)
print("Lista 2:", lista_2)


for a in lista_1:
    # print(a)
    b = lista_2.count(a)
    # print(b)
    list_total.append(b*a)

print("Lista de similaridade: ", list_total)
print("A soma da similaridade é: ", sum(list_total))

