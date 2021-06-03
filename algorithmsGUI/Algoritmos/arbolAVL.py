from tkinter import *
from tkinter import ttk

class ArbolAVL:

    def __init__(self, arbolIzq, arbolDer, value, padre, output):
        self.value = value
        self.arbolIzq = arbolIzq
        self.arbolDer = arbolDer
        self.padre = padre
        self.fb = 0
        self.altura= 1
        self.output = output

    def __str__(self):
        return "(VAL: " + str(self.value) + ", fb: " + str(self.fb) + ", altura: " + str(self.altura) + ", IZQ " + str(self.arbolIzq) + ", DER " + str(self.arbolDer) + " )"

    def aumentaraltura(self):
        alturaizq = 0
        alturader = 0

        if self.arbolIzq is None:
            alturaizq = 1

        else:
            alturaizq = 1 + self.arbolIzq.altura

        if self.arbolDer is None:
            alturader = 1

        else:
            alturader = 1 + self.arbolDer.altura

        self.altura = (alturaizq if alturaizq > alturader else alturader)
        self.fb = alturaizq - alturader

        if self.padre is not None:
            self.padre.aumentaraltura()

    def aumentaralturaRoot(self):
        alturaizq = 0
        alturader = 0

        if self.arbolIzq is None:
            alturaizq = 1

        else:
            alturaizq = 1 + self.arbolIzq.aumentaralturaRoot()

        if self.arbolDer is None:
            alturader = 1

        else:
            alturader = 1 + self.arbolDer.aumentaralturaRoot()

        self.altura = (alturaizq if alturaizq > alturader else alturader)
        self.fb = alturaizq - alturader

        return self.altura

    def verificarbalance(self):
        if self.fb > 1 or self.fb < -1:
            #print("fbb: " + str(self))
            self.balancear()

        elif self.padre is not None:
            self.padre.verificarbalance()


    def recalcularenhojas(self):
        if self.arbolIzq is None and self.arbolDer is None:
            self.aumentaraltura()
        else:
            if self.arbolIzq is not None:
                self.arbolIzq.recalcularenhojas()
            if self.arbolDer is not None:
                self.arbolDer.recalcularenhojas()

    def balancear(self):

        p = ArbolAVL(self.arbolIzq, self.arbolDer, self.value, self.padre, self.output)
        p.fb = self.fb
        p.altura = self.altura
        q = (self.arbolIzq if (self.arbolIzq.altura if self.arbolIzq is not None else 0) > (self.arbolDer.altura if self.arbolDer is not None else 0) else self.arbolDer)
        r = (q.arbolIzq if (q.arbolIzq.altura if q.arbolIzq is not None else 0) > (q.arbolDer.altura if q.arbolDer is not None else 0) else q.arbolDer)

        if p.fb == -2 and (q.fb == -1 or q.fb == 0):
            self.output.insert(self.output.index("end"), f'Rotacion Simple izquierda, p = { p.value }, q = {q.value}')
            self.value = q.value
            self.arbolDer = q.arbolDer
            self.arbolIzq = ArbolAVL(p.arbolIzq, q.arbolIzq, p.value, self, self.output)
            self.arbolIzq.padre = self
            self.arbolDer.padre = self

        elif p.fb == 2 and (q.fb == 1 or q.fb == 0):
            self.output.insert(self.output.index("end"), f'Rotacion Simple derecha, p = {p.value}, q = {q.value}')
            self.value = q.value
            self.arbolIzq = q.arbolIzq
            self.arbolDer = ArbolAVL(q.arbolDer, p.arbolDer, p.value, self, self.output)
            self.arbolIzq.padre = self
            self.arbolDer.padre = self

        elif p.fb == -2 and (q.fb == 1 or q.fb == 0):
            self.output.insert(self.output.index("end"), f'Rotacion Doble izquierda, p = {p.value}, q = {q.value}, r = {r.value}')
            self.value = r.value
            self.arbolIzq = ArbolAVL(p.arbolIzq, None, p.value, self, self.output)
            self.arbolDer = ArbolAVL(None, q.arbolDer, q.value, self, self.output)
            self.insertararbol(self.arbolIzq, r.arbolIzq)
            self.insertararbol(self.arbolDer, r.arbolDer)
            self.arbolIzq.padre = self
            self.arbolDer.padre = self

        elif p.fb == 2 and (q.fb == -1 or q.fb == 0):
            self.output.insert(self.output.index("end"),
                               f'Rotacion Doble Derecha, p = {p.value}, q = {q.value}, r = {r.value}')
            self.value = r.value
            self.arbolIzq = ArbolAVL(q.arbolIzq, None, q.value, self, self.output)
            self.arbolDer = ArbolAVL(None, p.arbolDer, p.value, self, self.output)
            self.insertararbol(self.arbolIzq, r.arbolIzq)
            self.insertararbol(self.arbolDer,r.arbolDer)
            self.arbolIzq.padre = self
            self.arbolDer.padre = self

        else:
            print(f'nodo p {p.value} nodo q {q.value}')

        self.recalcularenhojas()
        self.aumentaralturaRoot()



    def insertararbol(self, destino, fuente):
        if fuente is not None:
            destino.insertar(fuente.value)
            self.insertararbol(destino, fuente.arbolIzq)
            self.insertararbol(destino, fuente.arbolDer)

    def insertar(self, value):
        value = int(value)
        if value < self.value:
            if self.arbolIzq is None:
                self.output.insert(self.output.index("end") + 1, f'Agregamos el nodo {value} como hijo Izquierdo de { self.value }')
                self.arbolIzq = ArbolAVL(None, None, value, self, self.output)
                self.aumentaraltura()
                self.verificarbalance()

            else:
                self.arbolIzq.insertar(value)

        else:
            if self.arbolDer is None:
                self.output.insert(self.output.index("end") + 1,
                                   f'Agregamos el nodo {value} como hijo Derecho de {self.value}')
                self.arbolDer = ArbolAVL(None, None, value, self, self.output)
                self.aumentaraltura()
                self.verificarbalance()

            else:
                self.arbolDer.insertar(value)

    def delete(self, value):
        if value == self.value:
            padre = self.padre

            if padre is not None:

                if self.padre.arbolIzq is not None and self.padre.arbolIzq.value == value:
                    if self.arbolIzq is not None:
                        self.output.insert(self.output.index("end") + 1,
                                                f'Eliminamos el nodo {value} y lo reemplazamos con su hijo izquierdo {self.arbolIzq.value}')
                        self.padre.arbolIzq = self.arbolIzq
                        self.padre.arbolIzq.insertararbol(self.padre.arbolIzq.arbolDer, self.arbolDer)

                    elif self.arbolDer is not None:
                        self.output.insert(self.output.index("end") + 1,
                                                f'Eliminamos el nodo {value} y lo reemplazamos con su hijo derecho {self.arbolDer.value}')
                        self.padre.arbolIzq = self.arbolDer
                    else:
                        self.output.insert(self.output.index("end") + 1,
                                                f'Eliminamos el nodo {value} y lo reemplazamos con None')
                        self.padre.arbolIzq = None

                else:

                    if self.arbolIzq is not None:
                        self.output.insert(self.output.index("end") + 1,
                                                f'Eliminamos el nodo {value} y lo reemplazamos con su hijo izquierdo {self.arbolIzq.value}')
                        self.padre.arbolDer = self.arbolIzq
                        self.padre.arbolDer.insertararbol(self.padre.arbolDer.arbolDer, self.arbolDer)
                    elif self.arbolDer is not None:
                        self.output.insert(self.output.index("end") + 1,
                                                f'Eliminamos el nodo {value} y lo reemplazamos con su hijo derecho {self.arbolDer.value}')
                        self.padre.arbolDer = self.arbolDer
                    else:
                        self.output.insert(self.output.index("end") + 1,
                                                f'Eliminamos el nodo {value} y lo reemplazamos con None')
                        self.padre.arbolDer = None
                padre.aumentaralturaRoot()
                padre.verificarbalance()

            else:
                if self.arbolIzq is not None:
                    self.output.insert(self.output.index("end") + 1,
                                       f'Eliminamos el nodo {value} y lo reemplazamos con su hijo izquierdo {self.arbolIzq.value}')
                    self.value = self.arbolIzq.value
                    self.arbolDer.insertararbol(self.arbolDer, self.arbolIzq.arbolDer)
                    self.arbolIzq = self.arbolIzq.arbolIzq

                elif self.arbolDer is not None:
                    self.output.insert(self.output.index("end") + 1,
                                       f'Eliminamos el nodo {value} y lo reemplazamos con su hijo derecho {self.arbolDer.value}')
                    self.value = self.arbolDer.value
                    self.arbolIzq.insertararbol(self.arbolIzq, self.arbolDer.arbolIzq)
                    self.arbolDer = self.arbolDer.arbolDer

                else:
                    self.output.insert(self.output.index("end") + 1,
                                       f'Eliminamos el nodo {value} y lo reemplazamos con None')
                    self = None

        elif value > self.value:
            if self.arbolDer is None:
                return

            self.arbolDer.delete(value)

        else:
            if self.arbolIzq is None:
                return

            self.arbolIzq.delete(value)



#arbol = ArbolAVL(None, None, 0,None)
"""
arbol.insertar(29)
arbol.insertar(71)
arbol.insertar(82)
arbol.insertar(48)
arbol.insertar(39)
arbol.insertar(101)
arbol.insertar(22)
arbol.insertar(46)
arbol.insertar(17)
arbol.insertar(3)
arbol.insertar(20)
arbol.insertar(25)
arbol.insertar(10)

arbol.insertar(1)
arbol.insertar(2)
arbol.insertar(3)
arbol.insertar(4)
arbol.insertar(5)

arbol.delete(3)

print(arbol)
"""