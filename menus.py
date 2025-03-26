from utilidades_menu import *
from cargar_datos import *

def menu_principal():
    print(primer_menu)

def menu_generacion_informes():
    print(menu_listados)


def ejecucion_menu_principal():
    while True:
        print(menu_principal())
        opc = input("Ingrese una opcion: ")
        if opc == "1":
            print(crear_artista())
        if opc == "2":
            while True:
                print(menu_generacion_informes())
                opc = input("Ingrese una opcion: ")
                if opc == "1":
                    pais_2 = input("Ingrese el pais del artista: ")
                    tiempo_2 = input("Ingrese el periodo de tiempo del artista: ")
                    print("Aca esta la informacion de su artista: ")
                if opc == "2":
                    artista = input("Ingrese el nombre del artista: ")
                    print("Aca esta el listado: ")
                if opc == "3":
                    print(ejecucion_menu_principal())
                if opc == "4":
                    print("Hasta luego...")
                    break          
                else:
                     print("Escriba bien.")
        if opc == "3":
            artista = input("Ingrese el nombre del artista: ")
            print("Aca esta el listado: ")   
        if opc == "4":
            print("Hasta luego...")
            break
        else:
            print("Escriba bien.")                 




    