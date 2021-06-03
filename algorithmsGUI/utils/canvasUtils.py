<<<<<<< HEAD
from tkinter import *
from tkinter import ttk
import sys
import os
import copy
sys.path.append('..')
sys.path.append('algorithmsGUI')
from Algoritmos.arbolAVL import ArbolAVL

r = 30

def dibujar_arbol(arbol,tipo, canvas):

    if tipo not in ["rojo-negro","avl"]:
        return
    if arbol is None:
        return

    altura = None
    arbolRN = None
    if tipo == "rojo-negro":
        arbolRN = arbol
        altura = arbol.get_altura(arbol.root)
        arbol = arbol.root

    elif tipo == "avl":
        altura = arbol.altura

    x = int(int(canvas["width"])/2)
    while x/(2**altura) < r:
        x *= 2

    dibujar_arbol_recursivo(arbol, tipo, x, r + 10, canvas, int(x/2), altura, r+10,arbolRN)

def dibujar_arbol_recursivo(arbol, tipo, x, y, canvas, d, altura, dy,arbolRN):
    valor = None
    arbolIzq = None
    arbolDer = None
    alturaSubArbol = None 
    if tipo == "rojo-negro":
        valor = arbol.item
        arbolIzq = arbol.left
        arbolDer = arbol.right
        alturaSubArbol = arbolRN.get_altura(arbol)
    elif tipo == "avl":
        valor = arbol.value
        arbolIzq = arbol.arbolIzq
        arbolDer = arbol.arbolDer
        alturaSubArbol = arbol.altura 

    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvas.create_oval(x0, y0, x1, y1)
    canvas.create_text(int((x0 + x1)/2), int((y0+y1)/2), text=str(valor))

    deltaX = (d/(2**altura)) * (2**alturaSubArbol)

    condicion = None if tipo == "avl" else arbolRN.TNULL
    if arbolIzq is not condicion:
        canvas.create_line(x-r, y, x-deltaX, y+dy)
        dibujar_arbol_recursivo(arbolIzq, tipo, x-deltaX, y+dy+r, canvas, d, altura, dy, arbolRN)

    if arbolDer is not condicion:
        canvas.create_line(x+r, y, x+deltaX, y+dy)
        dibujar_arbol_recursivo(arbolDer, tipo, x+deltaX, y+dy+r, canvas, d, altura, dy, arbolRN)

class HashTableSlot:
    def __init__(self, canvas, x1, y1, x2, y2, valor):
        self.canvas = canvas
        self.imagen = canvas.create_rectangle(x1, y1, x2, y2)
        val = str(valor)
        aux_x = int((x1 + x2)/2)
        aux_y = int((y1 + y2)/2)
        self.text =  canvas.create_text(aux_x, aux_y, text = valor)

x1_slot = 75
x2_slot = 175
y1_slot = 50
y2_slot = 100
offset_y_slots = int((y2_slot - y1_slot) * 1.5)

def dibujar_slots_tabla_hash(canvas,m):
    canvas.delete("all")
    for i in range(0,m):
        rect = HashTableSlot(canvas, x1_slot, y1_slot + offset_y_slots * i, x2_slot, y2_slot + offset_y_slots * i, i)

inicio_flecha_hash = 20
final_flecha_hash =  50
largo_flecha = final_flecha_hash - inicio_flecha_hash
alto_keys = 30
largo_keys = 60
offset_x_keys = int(largo_keys*1.5)

def dibujar_keys_tabla_hash(canvas,m,slots):
    canvas.delete("all")
    dibujar_slots_tabla_hash(canvas, m)
    for slot in slots.keys():
        if slots[slot]:
            y1_key =  (offset_y_slots + offset_y_slots*slot) - alto_keys/2
            y2_key =  (offset_y_slots + offset_y_slots*slot) + alto_keys/2
            flecha_offset =  inicio_flecha_hash + final_flecha_hash
            for i in range(len(slots[slot])): 
                x1 = x2_slot+ flecha_offset + (flecha_offset + largo_keys) * i 
                x2 = x2_slot+ flecha_offset + largo_keys + (flecha_offset + largo_keys) * i  
                x1_flecha = x2_slot + inicio_flecha_hash + (flecha_offset + largo_keys) * i
                x2_flecha = x2_slot + inicio_flecha_hash + largo_flecha + (flecha_offset + largo_keys) * i
                canvas.create_line(x1_flecha, offset_y_slots + offset_y_slots*slot, x2_flecha, offset_y_slots + offset_y_slots*slot, arrow=LAST)  
                rect = HashTableSlot(canvas, x1, y1_key , x2, y2_key , slots[slot][i])



=======
from tkinter import *
from tkinter import ttk
import sys
import os
print(os.getcwd())
sys.path.append('..')
sys.path.append('algorithmsGUI')
from Algoritmos.arbolAVL import ArbolAVL

r = 30

def drawAVLTree(avlTree, canvas):

    if avlTree is None:
        return
    x = int(int(canvas["width"])/2)

    while x/(2**avlTree.altura) < r:
        x *= 2

    drawAVLTreeRecursive(avlTree, x, r + 10, canvas, int(x/2), avlTree.altura, r+10)

def drawAVLTreeRecursive(avlTree, x, y, canvas, d, altura, dy):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvas.create_oval(x0, y0, x1, y1)
    canvas.create_text(int((x0 + x1)/2), int((y0+y1)/2), text=str(avlTree.value))

    deltaX = (d/(2**altura)) * (2**avlTree.altura)

    if avlTree.arbolIzq is not None:
        canvas.create_line(x-r, y, x-deltaX, y+dy)
        drawAVLTreeRecursive(avlTree.arbolIzq, x-deltaX, y+dy+r, canvas, d, altura, dy)

    if avlTree.arbolDer is not None:
        canvas.create_line(x+r, y, x+deltaX, y+dy)
        drawAVLTreeRecursive(avlTree.arbolDer, x+deltaX, y+dy+r, canvas, d, altura, dy)

class HashTableSlot:
    def __init__(self,canvas,x1,y1,x2,y2,valor):
        self.canvas = canvas
        self.imagen = canvas.create_rectangle(x1,y1,x2,y2)
        val = str(valor)
        aux_x = int((x1+x2)/2)
        aux_y = int((y1+y2)/2)
        self.text =  canvas.create_text(aux_x,aux_y,text=valor)

x1_slot = 75
x2_slot = 175
y1_slot = 50
y2_slot = 100
offset_y_slots = int((y2_slot - y1_slot)*1.5)

def dibujar_slots_tabla_hash(canvas,m):
    canvas.delete("all")
    for i in range(0,m):
        rect = HashTableSlot(canvas,x1_slot,y1_slot+offset_y_slots*i,x2_slot,y2_slot+offset_y_slots*i,i)

def hash_div_aux(m,k):
    return k % m


inicio_flecha_hash = 20
final_flecha_hash =  50
largo_flecha = final_flecha_hash - inicio_flecha_hash
alto_keys = 30
largo_keys = 60
offset_x_keys = int(largo_keys*1.5)

def dibujar_keys_tabla_hash(canvas,m,slots):
    canvas.delete("all")
    dibujar_slots_tabla_hash(canvas,m)
    for slot in slots.keys():
        if slots[slot]:
            y1_key =  (offset_y_slots + offset_y_slots*slot) -alto_keys/2
            y2_key =  (offset_y_slots + offset_y_slots*slot) + alto_keys/2
            flecha_offset =  inicio_flecha_hash + final_flecha_hash
            for i in range(len(slots[slot])): 
                x1 = x2_slot+ flecha_offset + (flecha_offset + largo_keys) * i 
                x2 = x2_slot+ flecha_offset + largo_keys + (flecha_offset + largo_keys) * i  
                x1_flecha = x2_slot + inicio_flecha_hash + (flecha_offset + largo_keys) * i
                x2_flecha = x2_slot + inicio_flecha_hash + largo_flecha + (flecha_offset + largo_keys) * i
                canvas.create_line(x1_flecha, offset_y_slots + offset_y_slots*slot,x2_flecha, offset_y_slots + offset_y_slots*slot, arrow=LAST)  
                rect = HashTableSlot(canvas, x1, y1_key ,x2, y2_key , slots[slot][i])


def dibujarSort(data, color):
    canvas.delete("all") 
    cHeight = 1200
    cWidth = 700 
    
    algoWidth = cWidth /  (len(data) + 1)
    algoHeight = cWidth /  (len(data) + 1)
    offset = 20
    spacing = 10

    tamData = [i / max(data) for i in data]

    for i, height in enumerate(tamData):
        
        x0 = i * algoWidth + offset + spacing
        y0 = cHeight - height * 100

        
        x1 = (i+1) * algoWidth + offset
        y1 = cHeight 

        canvas.create_oval(x0,y0,x1,y1, fill = color[i])
        canvas.create_text(x0+2,y0, anchor = SW, text=str(data[i]))

>>>>>>> sortingAlg
