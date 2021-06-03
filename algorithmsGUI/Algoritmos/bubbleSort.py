import time 

data = []

def bubbleSort(data, dibujar, lista):
    print("entro a bubble sort")

    lista.insert(lista.index('end'),"Inciando bubble sort....")

    for _ in range(len(data)-1): 
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                
                #lista.delete(0, 'end')
                
                a = (("El numero " + str(data[j]) + " es mayor que " + str(data[j+1])))
                lista.insert(lista.index('end'), str(a))
                
                 
                
                data[j],data[j+1] = data[j+1], data[j] 
                b = (("Intercambiando de lugar " + str(data[j]) + " con " + str(data[j+1])))
                lista.insert(lista.index('end'), str(b))

                dibujar(data, 
                    [
                    'yellow' 
                    if x == j or x  == j+1 
                    else 'white' for x in range(len(data))
                    ]
                )
                time.sleep(0.5)
    dibujar(data, ['green' for x in range(len(data))])
    
    #lista.delete(0, 'end')
    lista.insert(lista.index('end'), 'Ordenado')
    