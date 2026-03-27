class CalificacionFueraDeRnagoError(Exception):
    pass

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero")

contador = 0

try:
    archivo = open("calificaciones.txt","a")

    while True:
        nombre = input("Nombre del estudiante (o salir para terminar):")

        if nombre.lower() == "salir":
            break

        calificacion = pedir_entero("calificacion (0-100)")

        #Validacion
        if calificacion < 0 or calificacion > 100:

            raise CalificacionFueraDeRnagoError("Calificacion fuera de rango")
        
        #Guardar en un archivo
        archivo.write(f"{nombre} - {calificacion}\n")

        contador += 1
        print("Registro guardado\n")

except CalificacionFueraDeRnagoError as e:
    print(e)

except FileNotFoundError:
    print("No se encontro el archivo")

except PermissionError:
    print("No tienes permiso para escribir el archivo")

finally:
    try:
        archivo.close()
    except:
        pass

    print(f"\n se regristraron {contador} estudiantes en la sesion")    