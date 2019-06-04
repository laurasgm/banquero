
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#recursos
E = [6,3,4,2]

#asignacion de recursos (asignacion de recursos)
C = [[3,0,1,1],
     [0,1,0,0],
     [1,1,1,0],
     [1,1,0,1],
     [0,0,0,0]]
#solicitud de recursos
R = [[1,1,0,0],
     [0,1,1,2],
     [3,1,0,0],
     [0,0,1,0],
     [2,1,1,0]]


num_recursos = 4 #cantidad de recursos
num_procesos = 5 #cantidad de procesos

#cantidad de recursos disponibles
def A():
    A = []
    for x in range(num_recursos):
        aux = 0
        for y in C:
            aux += y[x]
        A.append(E[x]-aux)
    return A

#compara cuantos recursos solicita y cuantos recursos hay disponibles
def comparador():
    disponibles = A()
    cola_procesos = []


    for x in R:
        habilitador = True
        for y in range(len(disponibles)):
            if (x[y]>disponibles[y]):
                habilitador = False
                break
                #print habilitador

        if habilitador:
            cola_procesos.append(x)
            break
    return cola_procesos,disponibles


def proceso():
    cola_proceso, disponibles = comparador()
    #print "aaaaaaaaaaaaaaaaaaaaaaaa"
    estado = []

    for x in range(len(cola_proceso)):
        estado.append(R.index(cola_proceso[x]))

    for x in estado:
        print "antes ejecucion"
        for y in range(len(disponibles)):
            disponibles[y]=disponibles[y]-R[x][y]

        print "disponibles: ", disponibles
        print "Recursos: ", E
        print "Recursos_asignados", C
        print "Solicitud_recursos", R
        
        for y in range(len(disponibles)):
            C[x][y]=C[x][y]+R[x][y]
            disponibles[y]=disponibles[y]+C[x][y]
        estado.remove(x)
        C.remove(C[x])
        R.remove(R[x])

        #despues de ejecutar

        print "despues ejecucion"

        print "disponibles: ",disponibles
        print "Recursos: ", E
        print "Recursos_asignados", C
        print "Solicitud_recursos", R
        print "fin de iteracion \n\n\n"


def main():
    '''recursos_disp = A()
    print recursos_disp
    cola_procesos = comparador()
    print cola_procesos'''

    print "disponibles: ", A()
    print "Recursos: ", E
    print "Recursos_asignados", C
    print "Solicitud_recursos", R

    #while(C):

    while(C):
        proceso()


if __name__ == '__main__':
    main()
