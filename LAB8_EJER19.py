#Programa: Ejecutar una tarea larga en segundo plano (ejemplo de cómo se usa)
#archivo: LAB8_EJER19.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code

import asyncio

async def eternity():
    await asyncio.sleep(3600)  # One hour
    print('yay!')

async def main():
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())