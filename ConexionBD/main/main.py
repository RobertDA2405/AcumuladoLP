import os
from dao.daoConnection import Connection, DaoCity
from models.clases import City

os.system('cls')

conex = Connection("localhost", "root", "", "bdregisters")
conex.connect()


# Instanciar objetos de City
city1 = City("Managua", 1)
city2 = City("León", 1)
city3 = City("Granada", 1)
city4 = City("Masaya", 1)
city5 = City("Estelí", 1)
city6 = City("Jinotepe", 1)


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
cities = daoCity.get_all()
for city in cities:
    print(city)