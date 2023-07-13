def comprarEntradas():
    cantEntradas=0
    while cantEntradas<1 or cantEntradas>3:
        cantEntradas=int(input("\nSeleccione la cantidad de entradas que desee (máximo 3): "))
        if cantEntradas<1 or cantEntradas>3:
            print("Debe ser una cantidad entre 1 y 3")
        print("\nLos precios de las entradas son los siguientes:\n-Platinum, $120.000. (Asientos del 1 al 20).\n-Gold, $80.000. (Asientos del 21 al 50).\n-Silver, $50.000. (Asientos del 51 al 100.).")
    if cantEntradas==1:
        asiento=int(input("\nEscoja su asiento: "))
        rut=int(input("\nIngrese su rut: "))
    if cantEntradas==2:
        asiento=int(input("\nEscoja los 2 asientos: "))
        rut=int(input("\nIngrese ambos rut: "))
    if cantEntradas==3:
        asiento=int(input("\nEscoja los 3 asientos: "))
        rut=int(input("\nIngrese los 3 rut: "))
    

    asientos()

    return

def ubicaDispo():
    return

def listadoAsist():

    return

def ganancias():
    print("\n\tTipo     Entrada    Cantidad    Total\n")
    print("\tPlatinum  $120.000       2       $240.000\n")
    print("\tGold      $80.000        4       $320.000\n")
    print("\tSilver    $50.000       10       $50.0000\n")
    print("\tTOTAL                   16       $1.060.000")
    return

def salir():
    print("\nSe ha cerrado la página\nHecho por: Antonio Campos Álvarez\n13/07/2023")
    return

menu=0
print("Venta de entradas del concierto VIP de Michael Jam")
while menu<1 or menu>5:
    print("\n1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    menu=int(input("\nSeleccione una opción: "))
    if menu<1 or menu>5:
        print("Opción inválida")

    if menu==1:
        comprarEntradas()

    if menu==2:
        ubicaDispo()

    if menu==3:
        listadoAsist()

    if menu==4:
        ganancias()

    if menu==5:
        salir()
        