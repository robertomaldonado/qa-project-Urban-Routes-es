![Python](https://img.shields.io/badge/python-3.11.3-blue?logo=python)
![Pytest](https://img.shields.io/badge/pytest-8.2.0-blue?logo=pytest)
![Selenium](https://img.shields.io/badge/selenium-4.20.0-darkgreen?logo=selenium)

# Pruebas Automatizadas para Urban Routes

Prueba automatizada para la aplicacion URBAN ROUTES.  
Realiza la comprobación de ingreso de datos y selección de opciones en la aplicación.

---

## Descripción:

Se realiza una prueba de funcionalidad completa, simulando el comportamiento de un usuario al realizar las siguientes acciones:

1. Configurar la dirección
2. Seleccionar la tarifa Comfort
3. Rellenar el número de teléfono
4. Agregar una tarjeta de crédito
5. Escribir un mensaje para el controlador (Modificar opciones del pedido)
6. Pedir una manta y pañuelos (Modificar opciones del pedido)
7. Pedir 2 helados (Modificar opciones del pedido)
8. Aparece el modal para buscar un taxi
9. Esperar a que aparezca la información del conductor en el modal

---

## Ejecución de pruebas:

Para ejecutar las pruebas automatizadas hay varias opciones:

1. Ejecutar pruebas con tu IDE favorito (ejemplo: PyCharm)
2. Ejecutar pruebas con pytest (correr como modulo de python):

> > python3 -m pytest <filename> -vv -s

---

## Tecnología utilizada:

- Pytest
- Selenium Web Driver (Python)

- Para una descripcion detallada de librerias y versiones utlilizadas revisar requirements.txt
