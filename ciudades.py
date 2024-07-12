def crear_ciudad(datos):
    datos = dict(datos)
    ciudad={}
    ciudad["nombre"]=input("Ingrese el nombre: ")
    ciudad["postal"]=input("Ingrese el código postal: ")
    try:
        ciudad["poblacion"]=int(input("Ingrese la población estimada: "))
    except Exception:
        print("¡Valor ingresado no válido!")
        print("Se debe actualizar luego con la opción (2) 'Modificar ciudad'")
        ciudad["poblacion"]=0
    ciudad["pais"]=input("Ingrese el País: ")

    datos["ciudades"].append(ciudad)
    print("Ciudad registrada con éxito!")
    return datos

def editar_ciudad(datos):
    datos = dict(datos)
    ciudad = input("Ingrese el nombre de la ciudad: ")
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["nombre"] == ciudad:
            datos["ciudades"][i]["nombre"]=input("Ingrese el nombre: ")
    datos["ciudades"][i]["postal"]=input("Ingrese el código postal: ")
    try:
        datos["ciudades"][i]["poblacion"]=int(input("Ingrese la población estimada: "))
    except Exception:
        print("¡Valor ingresado no válido!")
        print("Se debe actualizar luego con la opción (2) 'Editar las ciudades existentes'")
        datos["ciudades"][i]["poblacion"]=0
    datos["ciudades"][i]["pais"]=input("Ingrese el País: ")
            
    print("Ciudad actualizada con éxito!")
    return datos

def buscar_ciudad_nombre(datos):
    datos = dict(datos)
    ciudad = input("Ingrese el nombre de la ciudad: ")
    for i in range(len(datos["ciudades"])):
        print("")
        if datos["ciudades"][i]["nombre"] == ciudad:
            for llave,valor in datos["ciudades"][i].items():
                print(f"{llave.capitalize()}: {valor}")

def buscar_ciudad_pais(datos):
    datos = dict(datos)
    pais = input("Ingrese el pais: ")
    for i in range(len(datos["ciudades"])):
        print("")
        if datos["ciudades"][i]["pais"] == pais:
            for llave,valor in datos["ciudades"][i].items():
                print(f"{llave.capitalize()}: {valor}")

def buscar_ciudad_postal(datos):
    datos = dict(datos)
    postal = input("Ingrese el pais: ")
    for i in range(len(datos["ciudades"])):
        print("")
        if datos["ciudades"][i]["postal"] == postal:
            for llave,valor in datos["ciudades"][i].items():
                print(f"{llave.capitalize()}: {valor}")


def leer_ciudades(datos):
    for ciudad in datos["ciudades"]:
        for llave,valor in ciudad.items():
            print(f"{llave.capitalize()}: {valor}")
        print("")

def filtrar_ciudades_poblacion_mayor(datos):
    while (True):
        poblacion=input("Ingrese la poblacion con la que desea filtrar las ciudades: ")
        if poblacion.isnumeric():
            break
        else:
            print("Número de poblacion invalida")
    
    print("")
    print(f"Las ciudades con una población mayor a {poblacion} son: ")

    for ciudad in datos["ciudades"]:
        if ciudad["poblacion"]>int(poblacion):
            for llave,valor in ciudad.items():
                print(f"{llave.capitalize()}: {valor}")
            print("")

def filtrar_ciudades_poblacion_menor(datos):
    while (True):
        poblacion=input("Ingrese la poblacion con la que desea filtrar las ciudades: ")
        if poblacion.isnumeric():
            break
        else:
            print("Número de poblacion invalida")
    print("")
    print(f"Las ciudades con una población mayor a {poblacion} son: ")

    for ciudad in datos["ciudades"]:
        if ciudad["poblacion"]<int(poblacion):
            for llave,valor in ciudad.items():
                print(f"{llave.capitalize()}: {valor}")
            print("")