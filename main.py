import tkinter as tk
from tkinter import messagebox
import random

class Nodo:
    def __init__(self, dato):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)


class interfazGrafica:
    def __init__(self):
        self.arbol = Arbol("myArbol")
        self.root = tk.Tk()

        self.root.geometry("600x600")  # cambia el tamaño de la ventana
        self.root.title("Agenda")  # Cambia el título de la ventana
    def mainmenu(self):
        self.botonAgregarDatos = tk.Button(self.root, text="", width=20, font=("Helvetica", 15))
        self.buscar_entry = tk.Entry(self.root, width=30, font=("Helvetica", 15))


        #Listbox para mostrar datos
        self.eventos_listbox = None  # Inicialmente, no se crea la lista

        # Etiquetas
        Menu_label = tk.Label(self.root, text="Menú del arbol, selecciona una opción: ", font=("Helvetica", 15))
        Menu_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        #botones
        botonAgregarDatos = tk.Button(self.root, text="Agregar dato",command=self.agregarDato, width=20, font=("Helvetica", 15))
        botonAgregarDatos.place(relx=.5, rely=0.4, anchor=tk.CENTER)

        botonAgregar1000Datos = tk.Button(self.root, text="Agregar 1000 numeros",command=self.agregar1000Datos, width=20, font=("Helvetica", 15))
        botonAgregar1000Datos.place(relx=.5, rely=0.5, anchor=tk.CENTER)

        botonBuscarDato = tk.Button(self.root, text="Buscar dato",command=self.buscarDato, width=20, font=("Helvetica", 15))
        botonBuscarDato.place(relx=.5, rely=0.6, anchor=tk.CENTER)



        self.root.mainloop()

    def buscarDato(self):
        # Elimina el cuadro de entrada y el botón "Aceptar" si ya existen
        if hasattr(self, 'buscar_entry'):
            self.buscar_entry.destroy()
        if hasattr(self, 'botonAceptar'):
            self.botonAceptar.destroy()

        # Cuadro de texto para la búsqueda
        self.buscar_entry = tk.Entry(self.root, width=30, font=("Helvetica", 15))
        self.buscar_entry.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

        # Botón "Aceptar" para agregar el dato
        self.botonAceptar = tk.Button(self.root, text="Aceptar", command=self.buscarDesdeArbol, width=20,font=("Helvetica", 15))
        self.botonAceptar.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    def buscarDesdeArbol(self):
        datoABuscar = str(self.buscar_entry.get())  # Obtiene el dato a buscar desde la entrada
        # Destruye el cuadro de entrada y el botón "Aceptar"
        self.buscar_entry.destroy()
        self.botonAceptar.destroy()

        # Busca el dato en el árbol
        nodoEncontrado = self.arbol.buscar(datoABuscar)

        if nodoEncontrado:
            mensaje = "El dato " + str(nodoEncontrado.dato) + " sí existe"
            messagebox.showinfo("Encontrado", mensaje)
        else:
            mensaje = "El dato " + datoABuscar + " no existe"
            messagebox.showinfo("No encontrado :(", mensaje)

    def agregar1000Datos(self):
        for _ in range (1000):
            nuevos_numeros = random.randint(0, 100000)
            print(nuevos_numeros)
            self.arbol.agregar(str(nuevos_numeros))
        messagebox.showinfo("Hecho", "1000 numeros random ingresados al arbol correctamente")

    def agregarDato(self):
        # Elimina el cuadro de entrada y el botón "Aceptar" si ya existen
        if hasattr(self, 'buscar_entry'):
            self.buscar_entry.destroy()
        if hasattr(self, 'botonAceptar'):
            self.botonAceptar.destroy()

        # Cuadro de texto para la búsqueda
        self.buscar_entry = tk.Entry(self.root, width=30, font=("Helvetica", 15))
        self.buscar_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Botón "Aceptar" para agregar el dato
        self.botonAceptar = tk.Button(self.root, text="Aceptar", command=self.agregarDatoConfirmado, width=20,
                                      font=("Helvetica", 15))
        self.botonAceptar.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def agregarDatoConfirmado(self):
        # Obtiene el dato del cuadro de entrada y lo agrega al árbol
        dato = self.buscar_entry.get()
        self.arbol.agregar(dato)

        # Destruye el cuadro de entrada y el botón "Aceptar"
        self.buscar_entry.destroy()
        self.botonAceptar.destroy()

        # Vuelve al menú principal
        self.mainmenu()



myMenu = interfazGrafica()
myMenu.mainmenu()




