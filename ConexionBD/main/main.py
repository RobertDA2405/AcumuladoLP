import os
import daoConnection as dao
import clases as c

os.system('cls')
conex = dao.Connection("localhost", "root", "", "bdregisters")
conex.connect()

#instanciar modelo
city1 = c.City("Managua", 1)
city2 = c.City("León", 1)
city3 = c.City("Granada", 1)
city4 = c.City("Masaya", 1)
city5 = c.City("Estelí", 1)
city6 = c.City("Jinotepe", 1)

#instanciar dao
daoCity = dao.DaoCity(conex)

#insertar
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