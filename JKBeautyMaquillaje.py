print("Hecho por Paola De La Fuente Alarcon y Sara Maylea Ramirez Reyes")
print("JK Beauty Enterteminent")

contraseña = ""
while contraseña != "milkelif":
    contraseña = input("Introduce la contraseña: ")

print("Contraseña correcta!")

# Lista para almacenar los datos de maquillaje
maquillajes = []

def agregar():
    if len(maquillajes) < 10:
        maquillaje = {}
        maquillaje["Nombre"] = input("Ingrese el nombre del maquillaje: ")
        maquillaje["Marca"] = input("Ingrese la marca del maquillaje: ")
        maquillaje["Color"] = input("Ingrese el color del maquillaje: ")
        maquillaje["Tipo de Piel"] = input("Ingrese el tipo de piel recomendado: ")
        maquillaje["Precio"] = input("Ingrese el precio del maquillaje: ")
        maquillaje["Fecha de Caducidad"] = input("Ingrese la fecha de caducidad: ")
        maquillaje["Uso Recomendado"] = input("Ingrese el uso recomendado: ")
        maquillaje["Ingredientes"] = input("Ingrese los ingredientes: ")
        maquillaje["Resistencia al Agua"] = input("¿Es resistente al agua? (Sí/No): ")
        maquillaje["SPF"] = input("Ingrese el SPF (factor de protección solar): ")
        maquillajes.append(maquillaje)
        print("¡Maquillaje agregado!")
    else:
        print("No se pueden agregar más de 10 maquillajes.")

def consultar():
    if not maquillajes:
        print("No hay maquillajes para mostrar.")
    else:
        for i, maquillaje in enumerate(maquillajes, start=1):
            print(f"\nMaquillaje {i}:")
            for key, value in maquillaje.items():
                print(f"{key}: {value}")

def modificar():
    consultar()
    if maquillajes:
        index = int(input("Ingrese el número del maquillaje a modificar: ")) - 1
        if 0 <= index < len(maquillajes):
            maquillaje = maquillajes[index]
            for key in maquillaje.keys():
                nuevo_valor = input(f"Ingrese el nuevo valor para {key} (o deje en blanco para mantener el valor actual): ")
                if nuevo_valor:
                    maquillaje[key] = nuevo_valor
            print("¡Maquillaje modificado!")
        else:
            print("Índice fuera de rango.")

def eliminar():
    consultar()
    if maquillajes:
        index = int(input("Ingrese el número del maquillaje a eliminar: ")) - 1
        if 0 <= index < len(maquillajes):
            maquillajes.pop(index)
            print("¡Maquillaje eliminado!")
        else:
            print("Índice fuera de rango.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar (Insertar/Alta)")
        print("2. Consultar (Mostrar)")
        print("3. Modificar (Editar)")
        print("4. Eliminar (Borrar)")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar()
        elif opcion == '2':
            consultar()
        elif opcion == '3':
            modificar()
        elif opcion == '4':
            eliminar()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()