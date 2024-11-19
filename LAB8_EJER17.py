#Programa: Ejecutar una tarea larga en segundo plano (ejemplo de cómo se usa)
#archivo: LAB8_EJER17.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code

import asyncio


async def main():
    try:
        async with asyncio.timeout(None) as cm:
            new_deadline = asyncio.get_running_loop().time() + 10
            cm.reschedule(new_deadline)
            await long_running_task() #Ejemplo de tarea larga
    except TimeoutError:
        pass

    if(cm.expired):
        print("The long operation timed out, but it will continue in the background")