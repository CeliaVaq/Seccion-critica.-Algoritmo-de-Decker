#01

from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array

N = 8

def task(common, tid, turn):
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        while turn.value!=tid:
            pass
        print(f'{tid}−{i}: Critical section')
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section')
        common.value = v
        print(f'{tid}−{i}: End of critical section')
        turn.value = (tid + 1) % N

def main():
    lp = []
    common = Value('i', 0)
    turn = Value('i', 0)
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, turn)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")


if __name__ == "__main__":
    main()

"""
tid es el identificador de cada proceso, turn la variable que indica quien 
tiene el turno, aes una variable local a cada proceso
Los procesos son independientes, para hacer memoria compartida en multiprocessign 
hay que declarar las variables de una forma especial, como arguntos

7−98: Inside critical section
6−99: End of non−critical Section     SE HA SALIDO DE LA REGIÓN CRÍTICA
7−98: End of critical section


si hacemos-> for i in range(100 + tid) se queda bloqueado por que no cede el turno al segundo
EN LA SECCION NO CRITICA SE PUEDE PARAR EN CUALQUIER MOMENTO


hilo de ejecución que se crea cuando se empieza un proceso, se puede bifurcar
Procesoss(___)
    tarjet = _
    args = (___)
esto no ejecuta nada simplemente crea un objeto nuevo con esas cosas
si ejecuto un programa P2 se crea una rama en la hebra/hilo
hago un for para ejecutar todos los procesos

Para asegurarnos de que este programa acaba tenemos que hacer un p.join()
si el proceso p ha acabado entonces no hace nada
hacemos el bucle for p in lp
                    p.join()
Para que acaben todos los procesos



"""