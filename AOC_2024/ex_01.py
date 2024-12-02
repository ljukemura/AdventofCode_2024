arquivo = 'ex_01_input.txt'

lista_1 = []
lista_2 = []
total = 0

with open(arquivo, 'r') as file:
    for linha in file:
        valores = linha.split()
        lista_1.append(int(valores[0])) 
        lista_2.append(int(valores[1])) 


lista_1.sort()
lista_2.sort()


print("Lista 1:", lista_1)
print("Lista 2:", lista_2)
# print(len(lista_1))

for pos in range(0,len(lista_1)):       
    total += abs(lista_1[pos] - lista_2[pos])
    # print(lista_1[pos], " - ", lista_2[pos], " = ", total)

print("Total distâncias:",total)
      