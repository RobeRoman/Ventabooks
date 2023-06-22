import numpy
import os  
import msvcrt
from colorama import Style, Fore, Back
import random

############################################
#Crear arreglo
libros = numpy.empty([10,4],object)

############################################
#Funciones de diseño
def printv (texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printr (texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def limpiarpantalla():
    printv("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system("cls")

############################################
#Funciones de arreglo

#validar codigo
def validar(codigo):
    for i in range(10):
        if libros [i,0]==codigo:
            return i
    return -1
#guardar
def guardar(codigo,titulo,autor,precio):
    if None in libros:
        if validar(codigo)<0:
            if len(titulo)>4:
                if precio>=0:
                    for i in range(10):
                        if libros[i,0]==None:
                            libros[i,0]=codigo
                            libros[i,1]=titulo
                            libros[i,2]=autor
                            libros[i,3]=precio
                            printv("Libro registrado")
                            break
                else:
                    printr("El precio no puede ser negativo")            
            else:
                printr("El minimo debe ser 4 caracteres")                
        else:
            printr("El codigo se encuentra repetido")
    else:
        printr("No hay espacio")


#buscar
def buscar(codigo):
    posicion = validar(codigo)
    if validar(codigo)>=0:
        printv  (f"{libros[posicion,0]} {libros[posicion,1]} {libros[posicion,2]} {libros[posicion,3]}{libros[posicion,4]}") 
    else:
        printr("Libro no encontrado")





#certificado de criticas

#certificado de detalles