def crear_ciudad(datos):
    datos = dict(datos)
    ciudad={}
    ciudad["nombre"]=input("Ingrese el nombre: ")
    ciudad["postal"]=input("Ingrese el código postal: ")
    try:
        ciudad["poblacion"]=int(input("Ingrese la población estimada: "))
    except Exception:
        print("¡Valor ingresado no válido!")
        print("Se debe actualizar luego con la opción (2) 'Editar las ciudades existentes'")
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