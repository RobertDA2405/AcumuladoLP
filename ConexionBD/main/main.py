import os
from dao.daoConnection import Connection, DaoCity
from models.clases import City

os.system('cls')

conex = Connection("localhost", "root", "", "bdregisters")
conex.connect()


def insertarCiudad():
    nombre = input("Digita el nombre de la Ciudad ")
    ciudad = City(0, nombre, 1 )
    daoC = DaoCity(conex)
    daoC.insert(ciudad)

def mostrarCiudad():
    daoC = DaoCity(conex)
    registros = daoC.get_all()
    for ciudad in registros:
        print(ciudad)

def editarCiudad():
    daoC = DaoCity(conex)
    id= input("Inserta el id de la ciudad a modificar: ")
    nombre = input("Inserta nombre: ")
    ciudad = City(id, nombre)
    registU = daoC.update(ciudad)

def eliminarCiudad():
    daoC = DaoCity(conex)
    id= input("Inserta el id de la ciudad a eliminar: ")
    Cid = City(id)
    registE = daoC.delete(Cid)


#print("Agregar Registro")
#insertarCiudad()


print("Mostrar Ciudad")
mostrarCiudad()

editarCiudad()

print("Mostrar Ciudad")
mostrarCiudad()


eliminarCiudad()


"""

# Instanciar objetos de City
city1 = City(1, "Managua", 1)
city2 = City(2, "León", 1)
city3 = City(3, "Granada", 1)
city4 = City(4, "Masaya", 1)
city5 = City(5, "Estelí", 1)
city6 = City(6, "Jinotepe", 1)


# Instanciar dao
daoCity = DaoCity(conex)

# Insertar ciudades
daoCity.insert(city1)
daoCity.insert(city2)
daoCity.insert(city3)
daoCity.insert(city4)
daoCity.insert(city5)
daoCity.insert(city6)

#consultar
#cities = daoCity.get_all()
#print(f"Estas son las ciudades: ")
#for city in cities:
#    print(city)

# Eliminar ciudades
#DeletC = int(input("Inserta el id de la ciudad que deseas eliminar: "))
#print(f"La ciudad seleccionada es: {daoCity.get_by_id(DeletC)} ")
#daoCity.delete(DeletC)

#consultar
#cities = daoCity.get_all()
#for city in cities:
#    print(city)

"""