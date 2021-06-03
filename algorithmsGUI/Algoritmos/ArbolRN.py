<<<<<<< HEAD
import sys
from tkinter import messagebox

class NodoRN():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

class ArbolRN():
    def __init__(self,pasos=[]):
        self.TNULL = NodoRN(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.pasos = pasos

    def pre_order_helper(self, node):
        if node != TNULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    def in_order_helper(self, node):
        if node != TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.item + " ")
            self.in_order_helper(node.right)

    def post_order_helper(self, node):
        if node != TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(node.item + " ")

    def search_tree_helper(self, node, key):
        if node == TNULL or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    def get_color(self,color):
        return "negro" if color == 0 else "rojo"

    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                    self.pasos.append("Recolorear " + str(x.parent.item) + " a " + self.get_color(x.parent.color))
                    self.pasos.append("Rotar " + str(x.parent.item) + " a la izquierda")
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)

                        self.pasos.append("Recolorear " + str(s.left.item) + " a " + self.get_color(s.left.color))
                        self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                        self.pasos.append("Rotar " + str(s.item) + " a la derecha")    

                        s = x.parent.right
                    

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                    self.pasos.append("Recolorear " + str(s.right.item) + " a " + self.get_color(s.right.color))
                    self.pasos.append("Recolorear " + str(x.parent.item) + " a " + self.get_color(x.parent.color))
                    self.pasos.append("Rotar " + str(x.parent.item) + " a la izquierda")  

                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                    self.pasos.append("Recolorear " + str(x.parent.color) + " a " + self.get_color(x.parent.color))
                    self.pasos.append("Rotar " + str(x.parent.item) + " a la derecha")  
                             
                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left
            
                        self.pasos.append("Recolorear " + str(s.right.item) + " a " + self.get_color(s.right.color))
                        self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                        self.pasos.append("Rotar " + str(s.item) + " a la derecha")       

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                    self.pasos.append("Recolorear " + str(s.left.item) + " a " + self.get_color(0))
                    self.pasos.append("Recolorear " + str(x.parent.item) + " a " + self.get_color(0))
                    self.pasos.append("Rotar " + str(x.parent.item) + " a la derecha") 

                    x = self.root
              
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node_helper(self, node, key):
        self.pasos = []
        z = self.TNULL

        while node != self.TNULL:

            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            messagebox.showinfo(message="El nodo " + key + " no se encuentra en el árbol", title="Advertencia")
            return

        self.pasos.append("Borrar " + str(key))
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            if z.right.item != 0:
                self.pasos.append("Reemplazar "+ str(z.item) + " con " + str(z.right.item))
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            if z.left.item != 0:
                self.pasos.append("Reemplazar "+ str(z.item) + " con " + str(z.left.item))
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                if y.right.item != 0 :
                    self.pasos.append("Reemplazar "+ str(y.item) + " con " + str(y.right.item))
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            if y.item != 0:
                self.pasos.append("Reemplazar "+ str(z.item) + " con " + str(y.item))
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            self.pasos.append("Recolorear " + str(y.item) + " a " + self.get_color(z.color))
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    self.pasos.append("Recolorear " + str(k.parent.item) +", " +str(u.item) +", "+ str(k.parent.parent.item))
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.pasos.append("Rotar " + str(k.item) + " a la derecha")
                        self.right_rotate(k)
                    self.pasos.append("Recolorear " + str(k.parent.item) + " , " + str(k.parent.parent.item))
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.pasos.append("Rotar " + str(k.parent.parent.item) + " a la derecha")
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    self.pasos.append("Recolorear " + str(k.parent.item) +", " + str(u.item) +", "+ str(k.parent.parent.item))
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.pasos.append("Rotar " + str(k.item) + " a la izquierda")
                        self.left_rotate(k)
                    self.pasos.append("Recolorear " + str(k.parent.item) + " , " + str(k.parent.parent.item))
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.pasos.append("Rotar " + str(k.parent.parent.item) + " a la derecha")
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self,  x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insertar(self, key):
        self.pasos = []
        self.pasos.append("Insertar " + str(key))
        node = NodoRN(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def borrar(self, item):
        self.delete_node_helper(self.root, item)

    def print_tree(self):
        self.__print_helper(self.root, "", True)

    def get_altura_nodo(self,nodo):
        if nodo.left == self.TNULL:
            alturaIzq = 1
        else:
            alturaIzq = 1 + self.get_altura_nodo(nodo.left)

        if nodo.right == self.TNULL:
            alturaDer = 1
        else:
            alturaDer = 1 + self.get_altura_nodo(nodo.right)

        return  max(alturaIzq , alturaDer)

    def get_altura(self,nodo):
        altura  = self.get_altura_nodo(nodo)
        return  altura



# if __name__ == "__main__":
#     bst = ArbolRN(pasos=[])

#     bst.insertar(10)
#     bst.insertar(20)
#     bst.insertar(30)
#     bst.insertar(40)
#     bst.insertar(50)
#     bst.insertar(60)
#     bst.insertar(234)
#     bst.insertar(235)


#     bst.print_tree()
#     print(bst.get_altura(bst.root))

#     bst.print_tree()

    # bst.insertar(30)
    # bst.insertar(40)


# #     bst.insertar(2)
#     bst.insertar(3)
#     bst.insertar(4)
#     bst.insertar(5)
#     bst.insertar(6)
#     bst.insertar(7)
#     bst.insertar(8)
#     bst.insertar(9)
#     bst.insertar(10)


#     bst.print_tree()
#     # print(bst.pasos)
#     print("\nAfter deleting an element")
#     bst.print_tree()
#     print(bst.pasos)
#     print(bst.pasos)
=======
import sys
from tkinter import messagebox

class NodoRN():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

class ArbolRN():
    def __init__(self,pasos=[]):
        self.TNULL = NodoRN(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.pasos = pasos

    def pre_order_helper(self, node):
        if node != TNULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    def in_order_helper(self, node):
        if node != TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.item + " ")
            self.in_order_helper(node.right)

    def post_order_helper(self, node):
        if node != TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(node.item + " ")

    def search_tree_helper(self, node, key):
        if node == TNULL or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    def get_color(self,color):
        return "negro" if color == 0 else "rojo"

    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                    self.pasos.append("Recolorear " + str(x.parent.item) + " a " + self.get_color(x.parent.color))
                    self.pasos.append("Rotar " + str(x.parent.item) + " a la izquierda")
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)

                        self.pasos.append("Recolorear " + str(s.left.item) + " a " + self.get_color(s.left.color))
                        self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                        self.pasos.append("Rotar " + str(s.item) + " a la derecha")    

                        s = x.parent.right
                    

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                    self.pasos.append("Recolorear " + str(s.right.item) + " a " + self.get_color(s.right.color))
                    self.pasos.append("Recolorear " + str(x.parent.item) + " a " + self.get_color(x.parent.color))
                    self.pasos.append("Rotar " + str(x.parent.item) + " a la izquierda")  

                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                    self.pasos.append("Recolorear " + str(x.parent.color) + " a " + self.get_color(x.parent.color))
                    self.pasos.append("Rotar " + str(x.parent.item) + " a la derecha")  
                             
                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left
            
                        self.pasos.append("Recolorear " + str(s.right.item) + " a " + self.get_color(s.right.color))
                        self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                        self.pasos.append("Rotar " + str(s.item) + " a la derecha")       

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)

                    self.pasos.append("Recolorear " + str(s.item) + " a " + self.get_color(s.color))
                    self.pasos.append("Recolorear " + str(s.left.item) + " a " + self.get_color(0))
                    self.pasos.append("Recolorear " + str(x.parent.item) + " a " + self.get_color(0))
                    self.pasos.append("Rotar " + str(x.parent.item) + " a la derecha") 

                    x = self.root
              
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node_helper(self, node, key):
        self.pasos = []
        z = self.TNULL
        print(type(node.item),node.item)
        print(type(key),key)
        while node != self.TNULL:

            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            messagebox.showinfo(message="El nodo " + key + " no se encuentra en el árbol", title="Advertencia")
            return

        self.pasos.append("Borrar " + str(key))
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            if z.right.item != 0:
                self.pasos.append("Reemplazar "+ str(z.item) + " con " + str(z.right.item))
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            if z.left.item != 0:
                self.pasos.append("Reemplazar "+ str(z.item) + " con " + str(z.left.item))
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                if y.right.item != 0 :
                    self.pasos.append("Reemplazar "+ str(y.item) + " con " + str(y.right.item))
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            if y.item != 0:
                self.pasos.append("Reemplazar "+ str(z.item) + " con " + str(y.item))
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            self.pasos.append("Recolorear " + str(y.item) + " a " + self.get_color(z.color))
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    self.pasos.append("Recolorear " + str(k.parent.item) +", " +str(u.item) +", "+ str(k.parent.parent.item))
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.pasos.append("Rotar " + str(k.item) + " a la derecha")
                        self.right_rotate(k)
                    self.pasos.append("Recolorear " + str(k.parent.item) + " , " + str(k.parent.parent.item))
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.pasos.append("Rotar " + str(k.parent.parent.item) + " a la derecha")
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    self.pasos.append("Recolorear " + str(k.parent.item) +", " + str(u.item) +", "+ str(k.parent.parent.item))
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.pasos.append("Rotar " + str(k.item) + " a la izquierda")
                        self.left_rotate(k)
                    self.pasos.append("Recolorear " + str(k.parent.item) + " , " + str(k.parent.parent.item))
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.pasos.append("Rotar " + str(k.parent.parent.item) + " a la derecha")
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self,  x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insertar(self, key):
        self.pasos = []
        self.pasos.append("Insertar " + str(key))
        node = NodoRN(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def borrar(self, item):
        self.delete_node_helper(self.root, item)

    def print_tree(self):
        self.__print_helper(self.root, "", True)


# if __name__ == "__main__":
#     bst = ArbolRN(pasos=[])

#     bst.insertar(10)

#     print(bst.root.item)
#     bst.print_tree()

#     bst.insertar(20)
#     print(bst.root.item)

#     bst.print_tree()

# #     bst.insertar(2)
#     bst.insertar(3)
#     bst.insertar(4)
#     bst.insertar(5)
#     bst.insertar(6)
#     bst.insertar(7)
#     bst.insertar(8)
#     bst.insertar(9)
#     bst.insertar(10)


#     bst.print_tree()
#     # print(bst.pasos)
#     print("\nAfter deleting an element")
#     bst.borrar(6)
#     bst.print_tree()
#     print(bst.pasos)
#     print(bst.pasos)
>>>>>>> sortingAlg
