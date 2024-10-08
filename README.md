[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
Nombre: ALEJANDRO OSORIO PEÑARANDA
ID: 000548058
---
## **LISTA DE TAREAS PENDIENTES**
###### El problema que elegimos resolver es la gestión de una lista de tareas pendientes. Imagina que tienes una lista de cosas por hacer, y deseas llevar un registro de ellas. El objetivo es crear un programa que permita al usuario agregar nuevas tareas, marcar tareas como completadas y ver las tareas pendientes.

#### **IMPORTANCIA DEL PROGRAMA:**
###### La importancia de este programa radica en su simplicidad y utilidad cotidiana. Muchas personas necesitan llevar un registro de sus tareas diarias, ya sea para el trabajo, los estudios o las actividades personales. Un programa como este puede ayudar a mantener organizadas las responsabilidades y evitar olvidos.

#### **ALCANCE:**
###### Las funcionalidades que tendrá el programa son las siguientes:

-   **Agregar Tarea:** El usuario podrá ingresar una nueva tarea a la lista.
La tarea se agregará como “pendiente” por defecto.
- **Marcar Tarea como Completada:** El usuario podrá indicar que una tarea ha sido completada.
Se actualizará el estado de la tarea en la lista.
- **Mostrar Tareas Pendientes:**
El programa mostrará todas las tareas pendientes en pantalla.
- **Salir del Programa:**
El usuario podrá salir del programa cuando lo desee.

#### **ESTRUCTURA DE DATOS UTILIZADA:**
###### Se utilizará un diccionario para almacenar las tareas. Cada tarea será una clave en el diccionario, y su valor asociado indicará si está completada o no ( True o False).

#### **PSEUDOCÓDIGO:**
INICIO
    Crear un diccionario llamado "tareas"
    
    MIENTRAS verdadero:
        MOSTRAR "Lista de Tareas:"
        MOSTRAR "1. Agregar tarea"
        MOSTRAR "2. Marcar tarea como completada"
        MOSTRAR "3. Mostrar tareas pendientes"
        MOSTRAR "4. Salir"
        LEER opción
        
        SI opción == 1:
            LEER nueva_tarea
            tareas[nueva_tarea] = False  # Marcar tarea como pendiente
            MOSTRAR "Tarea 'nueva_tarea' agregada."
        SINO SI opción == 2:
            LEER tarea_completada
            SI tarea_completada en tareas:
                tareas[tarea_completada] = True  # Marcar tarea como completada
                MOSTRAR "Tarea 'tarea_completada' marcada como completada."
            SINO:
                MOSTRAR "Tarea 'tarea_completada' no encontrada en la lista."
        SINO SI opción == 3:
            PARA cada tarea, completada en tareas:
                SI NO completada:
                    MOSTRAR "- tarea"
        SINO SI opción == 4:
            MOSTRAR "¡Hasta luego!"
            SALIR
        SINO:
            MOSTRAR "Opción no válida. Inténtalo de nuevo."
FIN
