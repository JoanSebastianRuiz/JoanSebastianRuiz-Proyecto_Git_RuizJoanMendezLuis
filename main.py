from ciudades import *
from datos import *

bandera1=True

while (bandera1==True):
    bandera2=True

    print("Bienvenido,  ")
    print("1. Registrar ciudad")
    print("2. Modificar ciudad")
    print("3. Leer ciudades")
    print("4. Busqueda de ciudad")
    print("5. Filtrar ciudades")
    print("6. Exportar datos")
    print("7. Salir")
    print("")

    opcion=input("Seleccione la opción que desea realizar:")
    if opcion=="1":
        datos=cargar_datos("ciudades.json")
        datos_subir=crear_ciudad(datos)
        guardar_datos(datos_subir, "ciudades.json")
        print("")

    elif opcion=="2":
        datos=cargar_datos("ciudades.json")
        datos_subir=editar_ciudad(datos)
        guardar_datos(datos_subir, "ciudades.json")
        print("")
    
    elif opcion=="7":
        print("Hasta pronto!")
        bandera1=False

    else:
        print("Opcion invalida")
        print("")


"""
    elif opcion=="3":

    elif opcion=="4":
        while (bandera2==True):
            print("Estas son las opciones de busqueda:")
            print("1. Buscar por nombre")
            print("2. Buscar por país")
            print("3. Buscar por código postal")
            opcion2=input("Seleccione la opción que desea realizar:")

            if opcion2=="1":

                bandera2=False

            elif opcion2=="2":

                bandera2=False

            elif opcion2=="3":

                bandera2=False

            else:
                print("Opcion invalida")

        

    elif opcion=="5":
        print("1. Obtener ciudades con poblacion mayor a un numero especifico")
        print("2. Obtener ciudades con poblacion menor a un numero especifico")
        opcion2=input("Seleccione la opción que desea realizar:")

        while (bandera2==True):
            if opcion2=="1":

                bandera2=False

            elif opcion2=="2":

                bandera2=False

            else:
                print("Opcion invalida")

                
    elif opcion=="6":
"""




    