def agregar_tarea(lista_tareas):
    tarea = input("Ingresa la nueva tarea: ")
    lista_tareas.append({"tarea": tarea, "completada": False})
    print(f"Tarea '{tarea}' agregada.")

def marcar_completada(lista_tareas):
    tarea = input("Ingresa la tarea completada: ")
    for t in lista_tareas:
        if t["tarea"] == tarea:
            t["completada"] = True
            print(f"Tarea '{tarea}' marcada como completada.")
            return
    print(f"Tarea '{tarea}' no encontrada en la lista.")

def mostrar_pendientes(lista_tareas):
    print("\nTareas pendientes:")
    for t in lista_tareas:
        if not t["completada"]:
            print(f"- {t['tarea']}")

def main():
    lista_tareas = []  # Lista de tareas (diccionarios)

    while True:
        print("\n--- Lista de Tareas ---")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas pendientes")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea(lista_tareas)
        elif opcion == "2":
            marcar_completada(lista_tareas)
        elif opcion == "3":
            mostrar_pendientes(lista_tareas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

def main():
    #Tu código va aquí. Mantén la indentación
    pass # borra esta línei

if __name__ == "__main__":
    main()
