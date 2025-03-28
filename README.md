# Artistas

Este proyecto está diseñado para gestionar información sobre artistas. El sistema permite cargar, almacenar y visualizar datos de artistas de manera sencilla y organizada.

## Tabla de Contenidos

- [Características](#características)
- [Estructura de Datos](#estructura-de-datos)
- [Módulos (Archivos) del Proyecto](#módulos-archivos-del-proyecto)
- [Instalación](#instalación)
- [Contribuciones](#contribuciones)

## Características

- **Gestión de Artistas**: Permite cargar y visualizar datos sobre artistas.
- **Almacenamiento en JSON**: Los datos se almacenan en un archivo JSON para garantizar la persistencia.
- **Interactividad**: La aplicación permite que los usuarios interactúen con un menú para cargar y visualizar la información.

## Estructura de Datos

Los datos de los artistas se almacenan en un archivo JSON (`artistas.json`) y se gestionan a través de varios módulos.

## Módulos (Archivos) del Proyecto

El proyecto tiene la siguiente estructura de archivos:


- **`main.py`**: Archivo principal donde se ejecuta la aplicación y se interactúa con los usuarios.
- **`cargar_datos.py`**: Contiene funciones para cargar los datos de los artistas desde un archivo JSON.
- **`menus.py`**: Maneja la visualización y gestión del menú de opciones para el usuario.
- **`utilidades_menu.py`**: Proporciona funciones auxiliares para manejar la interfaz de usuario.
- **`artistas.json`**: Archivo que contiene los datos de los artistas.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Jharmo05/Artistas.gitç
   ```

1. Ejecutar el script principal:
   ```bash
   python main.py
   ```

