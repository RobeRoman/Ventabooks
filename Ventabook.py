import Funciones as fu

while True:
    fu.limpiarpantalla()
    fu.printv("SISTEMA VENTABOOKS")
    fu.printv("******************")
    print("1) Guardar")
    print("2) Buscar")
    print("3) Certificados")
    print("0) Salie")
    opcion = int(input("Selecciones : "))

    #Validamos la opcion
    if opcion==0:
        fu.printv("Adios")
        break
    elif opcion==1:
        fu.printv("Guardar")
    elif opcion==2:
        fu.printv("Buscar")
    elif opcion==3:
        fu.printv("Certificados")
    else:
        fu.printr("Opcion no valida")