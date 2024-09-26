import time

fila = [3,4,3,1.5,4,1,3]
tempo = 2
print(fila)
while len(fila) > 0:
    x = fila.pop(0)
    if(x > tempo):
        fila.append(x - tempo)
    time.sleep(tempo)
    print(fila)

