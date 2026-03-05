# Sistema de gestión de biblioteca
# Descripción del sistema: Desarrollar un programa completo en Python para gestionar los libros de una biblioteca, aplicando todos los conceptos aprendidos en las secciones anteriores. El sistema debe permitir realizar operaciones básicas de mantenimiento de un catálogo bibliográfico.

# Requisitos funcionales:
# Estructura de datos: Utilizar una lista de diccionarios para almacenar la información de los libros. Cada libro debe contener: id (numérico autoincremental), título, autor, año de publicación y estado de disponibilidad (True/False).
# Funciones principales: o agregar_libro(): Permite registrar un nuevo libro validando que el año sea numérico y mayor a 1900. o mostrar_libros(): Muestra todos los libros en formato legible: "ID: 1 - 'Cien años de soledad' (Gabriel García Márquez, 1967) [Disponible]" o buscar_libro(): Permite buscar libros por título o autor, mostrando coincidencias parciales. o prestar_libro(id): Cambia el estado de disponibilidad a False si el libro existe y está disponible. o devolver_libro(id): Cambia el estado de disponibilidad a True. o eliminar_libro(id): Elimina un libro solo si no está prestado actualmente. o menu_principal(): Implementa un menú interactivo con las opciones anteriores utilizando while para repetir hasta que se seleccione salir.
# Funciones adicionales desafiantes: o libros_por_autor(autor): Lista todos los libros de un autor específico. o estadisticas(): Muestra estadísticas del sistema: cantidad total de libros, libros disponibles y libros prestados. o exportar_a_txt(): Guarda todos los libros en un archivo de texto llamado "biblioteca.txt".
# Entregables esperados:
# • Archivo Python ejecutable con el nombre biblioteca.py • Código completo con comentarios explicativos en cada función

# Sistema de gestión de biblioteca

# Estructura de datos para almacenar los libros
biblioteca = []
# funcion para mostrar los libros de manera mas limpia
def mostrar_libro_formateado(libro):
    estado = "Disponible" if libro["disponible"] else "Prestado"
    print("-----------------")
    print(f"ID: {libro['id']} - '{libro['titulo']}' "
          f"({libro['autor']}, {libro['anio_publicacion']}) "
          f"[{estado}]")

# funcion para agregar un libro
def agregar_libro(biblioteca):
    #solicitud al cliente
    titulo = input("Ingrese el título del libro: ").strip()
    autor = input("Ingrese el autor del libro: ").strip()

    if not titulo or not autor:
        print("Titulo y autor son obligatorio")
        return
    # Validar el año de publicación
    while True:
        try:
            anio_publicacion = int(input("Ingrese el año de publicación (mayor a 1900): "))
            if anio_publicacion > 1900:
                break
            else:
                print("El año debe ser mayor a 1900. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    # Generar un nuevo ID autoincremental
    if not biblioteca:
        nuevo_id = 1
    else:
        nuevo_id = biblioteca[-1]["id"] + 1
    # Crear un nuevo libro y agregarlo a la biblioteca
    libro = {
        "id": nuevo_id,
        "titulo": titulo,
        "autor": autor,
        "anio_publicacion": anio_publicacion,
        "disponible": True
    }
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado con ID {nuevo_id}.")


# funcion para mostrar
def mostrar_libros(biblioteca):
    # Verificar si la biblioteca está vacía
    if not biblioteca:
        print("No hay ningun libro en la biblioteca.")
    else:
        # Mostrar todos los libros en formato legible
        for libro in biblioteca:
            mostrar_libro_formateado(libro)

#funcion para buscar
def buscar_libro(biblioteca):
    # Ingrese de datos del usuario
    busqueda = input("Ingrese autor o titulo: ")
    encontrado = False
    busqueda = busqueda.lower().strip() #convierte todo a minuscula y quita espacios adelante y atras
    # Buscar libros por título o autor, mostrando coincidencias parciales
    for libro in biblioteca:
        # Verificar si la búsqueda coincide con el título o el autor (coincidencia parcial)
        if busqueda in libro["titulo"].lower() or busqueda in libro["autor"].lower():
            mostrar_libro_formateado(libro)
            encontrado = True
        # Si no se encontraron coincidencias, mostrar un mensaje
    if not encontrado:
        print("No se encontraron libros con ese nombre ni autor.")

#funcion para prestar un libro
def prestar_libro(biblioteca):
    # se pide los datos al usuario
    try:
        id_buscar = int(input("Ingrese el ID del libro a prestar: "))

    except ValueError:
        print("ID invalido")
        return
    
    encontrado = False
    # recorremos la lista
    for libro in biblioteca:
        if libro["id"] == id_buscar:
            encontrado = True
            # se hace el proceso del prestamo
            if libro["disponible"]:
                libro["disponible"] = False
                print("Libro prestado correctamente.")
            else:
                print("El libro ya fue prestado")

            break

    if not encontrado:
        print("No se encontro un libro con ese ID")

#funcion para devolverlo
def devolver_libro(biblioteca):
    # se pide los datos al usuario
    try:
        id_buscar = int(input("Ingrese el ID del libro a devolver: "))

    except ValueError:
        print("ID invalido")
        return
    
    encontrado = False
    # recorremos la lista
    for libro in biblioteca:
        if libro["id"] == id_buscar:
            encontrado = True
            # se hace el proceso de devolucion
            if not libro["disponible"]:
                libro["disponible"] = True
                print("Libro devuelto correctamente.")
            else:
                print("El libro ya está disponible.")

            break

    if not encontrado:
        print("No se encontro un libro con ese ID")

#funcion para eliminar un libro
def eliminar_libro(biblioteca):
    # se pide los datos al usuario
    try:
        id_buscar = int(input("Ingrese el ID del libro a eliminar: "))

    except ValueError:
        print("ID invalido")
        return
    
    encontrado = False
    
    # recorremos la lista
    for libro in biblioteca:
        if libro["id"] == id_buscar:
            encontrado = True
            # se hace el proceso de eliminacion
            if libro["disponible"]:
                biblioteca.remove(libro) #elimina el libro de la lista
                print("Libro eliminado correctamente.")

            else:
                print("No se puede eliminar un libro si esta prestado")

            break
    # Si no se encontró el libro, mostrar un mensaje
    if not encontrado:
        print("No se encontro un libro con ese ID")

# da las estadisticas de la biblioteca
def estadisticas(biblioteca):
    total_libros = len(biblioteca) #cuenta cuantos libros hay.
    contador_autores = {} # contador de autores
    libros_disponibles = 0 # cuenta cuantos libros hay disponible
    libros_prestados = 0 # contamos cuantos libros hay prestados

    for libro in biblioteca:
        if libro["disponible"]:
            libros_disponibles += 1
        
        else:
            libros_prestados += 1

        autor = libro["autor"]

        if autor in contador_autores:
            contador_autores[autor] += 1

        else:
            contador_autores[autor] = 1

    print("\n--- Estadísticas ---")
    print(f"Total de libros: {total_libros}")
    print(f"Libros disponibles: {libros_disponibles}")
    print(f"Libros prestados: {libros_prestados}")

    print("\nLibros por autor:")
    for autor, cantidad in contador_autores.items():
        print(f"{autor}: {cantidad}")


# exporta un archivo txt
def exportar_a_txt(biblioteca):
    # se exporta la biblioteca a un archivo txt
    with open("biblioteca.txt", "w") as archivo:
        for libro in biblioteca:
            if libro["disponible"]:
                estado = "Disponible"
            else:
                estado = "Prestado"
            # se escribe cada libro en el archivo con su formato legible
            archivo.write(f"ID: {libro['id']}\n")
            archivo.write(f"Título: {libro['titulo']}\n")
            archivo.write(f"Autor: {libro['autor']}\n")
            archivo.write(f"Año de publicación: {libro['anio_publicacion']}\n")
            archivo.write(f"Estado: {estado}\n")
            archivo.write("-----------------------------\n") # separador entre libros
    print("Biblioteca exportada a biblioteca.txt....")

# menu principal
def menu_principal():
    while True:
        print("\n--- Sistema de Gestión de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Eliminar libro")
        print("7. Estadísticas")
        print("8. Exportar a TXT")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro(biblioteca)
        elif opcion == "2":
            mostrar_libros(biblioteca)
        elif opcion == "3":
            buscar_libro(biblioteca)
        elif opcion == "4":
            prestar_libro(biblioteca)
        elif opcion == "5":
            devolver_libro(biblioteca)
        elif opcion == "6":
            eliminar_libro(biblioteca)
        elif opcion == "7":
            estadisticas(biblioteca)
        elif opcion == "8":
            exportar_a_txt(biblioteca)
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")

# Ejecutar el menú principal
menu_principal()