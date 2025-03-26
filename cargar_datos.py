import json
import os
from datetime import datetime


def cargar_artista():
    try:
        with open("artistas.json","r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
artistas = []
    
def guardar_artista():
    with open("artistas.json", "w") as file:
        return json.dump(artistas,file, indent=4)
    
artistas = cargar_artista()

def mostrar_artistas():
    print(artistas)
    
def crear_artista():
    nombre = input("Ingrese el nombre del artista: ")
    pais = input("Ingres el pais de origen del artista, incluyendo nombre y codigo ISO3: ")
    anos_actividad = input("Ingrese el primer año y ultimo año del artista (EJ: 1979/2013) ")
    disco = input("Ingrese el año de lanzamiento del primer disco que llego a las listas: ")
    genero= input("Ingrese el genero musical del artista y su descripcion (EJ: Rock/Pop) ")
    unidades = input("Ingrese la cantidad de unidades certificadas: ")
    ventas = input("Ingrese la cantidad de ventas reclamadas: ")
    estado = input("El artista se encuentra actualmente activo, escriba SI o NO: ")

    artista = {
        "Nombre del artista": nombre,
        "Estado actual del artista:": estado,
        "Pais del artista:": pais,
        "Anos de actividad:": anos_actividad,
        "Ano de lanzamiento del primer disco:": disco,
        "Genero:": genero,
        "Total de unidades certificadas vendidas:": unidades,
        "Total de ventas reclamadas:": ventas}
    
    artistas.append(artista)
    guardar_artista()



