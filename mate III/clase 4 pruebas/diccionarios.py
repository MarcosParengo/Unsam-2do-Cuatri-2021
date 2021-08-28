#Los diccionarios sirven para guardar pares de objetos

#Crear diccionarios
yo={
    "nombre":"marcos",
    "apellido":"Sancho",
    "edad":20
}
sele=dict(nombre="selena",apellido="Laviola",edad=19)
nn=dict.fromkeys(["nombre", "apellido", "edad"], 0)

#Acceder a los datos
print(sele["nombre"])
print(yo.get("nombre"))
print(yo.get("clave","mensaje si no existe la clave"))

#Actulizar info
print(f'Mi nombre es {yo["nombre"]} y mi apellido {yo["apellido"]} tengo {yo["edad"]} años')
yo["nombre"]="Marcos"
print(f'Mi nombre es {yo["nombre"]} y mi apellido {yo["apellido"]} tengo {yo["edad"]} años')
print("\n")

#Borrar info
print(yo.get("nombre","mensaje si no existe la clave"))
del yo["nombre"]
print(yo.get("nombre","No existe la clave"))
print("\n")

#Actualizar info (unir dos diccionarios y reemplazar en el caso que se repita)
print(f'Su nombre es {sele["nombre"]} y su apellido {sele["apellido"]} tiene {sele["edad"]} años')
sele.update(yo)#reemplaza todo menos el nombre ya que en "yo" esta clave no existe
print(f'Su nombre es {sele["nombre"]} y su apellido {sele["apellido"]} tiene {sele["edad"]} años')
print("\n")

#Imprimir todos las claves
for k in sele:
    print(k)
print("\n")

#Imprimir todos los valores
for k in sele.values():
    print(k)
print("\n")

#Imprimir valores y claves
for k,v in sele.items():
    print(f"{k}:{v}")
print("\n")


