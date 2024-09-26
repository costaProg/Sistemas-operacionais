

cond = True
fila = []

while cond:
    op = int(input("\n--------| Menu |--------\n[1] - Inserir elemento na fila\n[2] - Remover elemento da fila\n[3] - Sair\nEscolha uma opção: "))
    if(op == 1):
        valor = int(input("Informe um valor inteiro: "))
        fila.append(valor)
        print(fila)
    elif(op == 2):
        if not fila:
            print("Fila está vazia!")
        else:
            fila.pop(0)
            print(fila)
    elif(op == 3):
        print(fila)
        cond = False