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

#guardar

#buscar

#certificado de criticas

#certificado de detalles