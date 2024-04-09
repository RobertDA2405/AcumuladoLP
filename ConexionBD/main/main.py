import os
from dao.daoConnection import Connection, DaoCity, DaoJobs, DaoEmployees
from models.clases import City, Jobs, Employees

os.system('cls')

conex = Connection("localhost", "root", "", "bdregisters")
conex.connect()


#########################################################################################

def insertarCiudad():
    nombre = input("Digita el nombre de la Ciudad ")
    ciudad = City(0, nombre, 1 )
    daoC = DaoCity(conex)
    daoC.insert(ciudad)

def mostrarCiudades():
    daoC = DaoCity(conex)
    registros = daoC.get_all()
    for c in registros:
        print(c)

def mostrarCiudadporID():
    daoC = DaoCity(conex)
    id = input("Inserta el id de la ciudad que quieres ver: ")
    ciudad = City(id=id)
    registI = daoC.get_by_id((ciudad.id,))
    print(registI)

def editarCiudad():
    daoC = DaoCity(conex)
    id= input("Inserta el id de la ciudad a modificar: ")
    nombre = input("Inserta nombre: ")
    ciudad = City(id, nombre)
    registU = daoC.update(ciudad)

def eliminarCiudad():
    daoC = DaoCity(conex)
    id = input("Inserta el id de la ciudad a eliminar: ")
    ciudad = City(id=id)
    registE = daoC.delete((ciudad.id,))

#########################################################################################

def insertarEmpleos():
    nombre = input("Digita el nombre del empleo:  ")
    empleo = Jobs(0, nombre, 1 )
    daoJ = DaoJobs(conex)
    daoJ.insert(empleo)

def mostrarEmpleos():
    daoJ = DaoJobs(conex)
    registros = daoJ.get_all()
    for j in registros:
        print(j)

def mostrarEmpleoporID():
    daoJ = DaoJobs(conex)
    id = input("Inserta el id del empleo que quieres ver: ")
    empleo = Jobs(id=id)
    registI = daoJ.get_by_id((empleo.id,))
    print(registI)

def editarEmpleo():
    daoJ = DaoJobs(conex)
    id= input("Inserta el id del empleo a modificar: ")
    nombre = input("Inserta el nombre: ")
    empleo = Jobs(id, nombre)
    registU = daoJ.update(empleo)

def eliminarEmpleo():
    daoJ = DaoJobs(conex)
    id = input("Inserta el id del empleo a eliminar: ")
    empleo = Jobs(id=id)
    registE = daoJ.delete((empleo.id,))

#########################################################################################

def insertarEmpleado():
    nombre = input("Digita el nombre del empleo:  ")
    empleado = Employees(0, nombre, 1 )
    daoJ = DaoEmployees(conex)
    daoJ.insert(empleado)

def mostrarEmpleados():
    daoE = DaoEmployees(conex)
    registros = daoE.get_all()
    for e in registros:
        print(e)

def mostrarEmpleadosporID():
    daoE = DaoEmployees(conex)
    id = input("Inserta el id del empleado que quieres ver: ")
    empleado = Jobs(id=id)
    registI = daoE.get_by_id((empleado.id,))
    print(registI)

def editarEmpleado():
    daoE = DaoEmployees(conex)
    id= input("Inserta el id del empleado a modificar: ")
    nombre = input("Inserta el nombre: ")
    empleado = Employees(id, nombre)
    registU = daoE.update(empleado)

def eliminarEmpleado():
    daoE = DaoEmployees(conex)
    id = input("Inserta el id del empleado a eliminar: ")
    empleado = Employees(id=id)
    registE = daoE.delete((empleado.id,))



# Función principal del menú
def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al menú de la aplicación:")
        print("1. Ver y gestionar Ciudades")
        print("2. Ver y gestionar Empleos")
        print("3. Ver y gestionar Empleados")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_ciudades()
        elif opcion == "2":
            menu_empleos()
        elif opcion == "3":
            menu_empleados()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


# Menú para ciudades
def menu_ciudades():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menú de Ciudades:")
        print("1. Insertar Ciudad")
        print("2. Mostrar Ciudades")
        print("3. Mostrar Ciudad por ID")
        print("4. Editar Ciudad")
        print("5. Eliminar Ciudad")
        print("6. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            insertarCiudad()
        elif opcion == "2":
            mostrarCiudades()
            input("Presiona Enter para continuar...")
        elif opcion == "3":
            mostrarCiudadporID()
            input("Presiona Enter para continuar...")
        elif opcion == "4":
            editarCiudad()
        elif opcion == "5":
            eliminarCiudad()

        os.system('cls' if os.name == 'nt' else 'clear')
        
        if opcion == "6":
            break


# Menú para empleos
def menu_empleos():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menú de Empleos:")
        print("1. Insertar Empleo")
        print("2. Mostrar Empleos")
        print("3. Mostrar Empleo por ID")
        print("4. Editar Empleo")
        print("5. Eliminar Empleo")
        print("6. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            insertarEmpleos()
        elif opcion == "2":
            mostrarEmpleos()
            input("Presiona Enter para continuar...")
        elif opcion == "3":
            mostrarEmpleoporID()
            input("Presiona Enter para continuar...")
        elif opcion == "4":
            editarEmpleo()
        elif opcion == "5":
            eliminarEmpleo()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if opcion == "6":
            break


# Menú para empleados
def menu_empleados():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menú de Empleados:")
        print("1. Insertar Empleado")
        print("2. Mostrar Empleados")
        print("3. Mostrar Empleado por ID")
        print("4. Editar Empleado")
        print("5. Eliminar Empleado")
        print("6. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            insertarEmpleado()
        elif opcion == "2":
            mostrarEmpleados()
            input("Presiona Enter para continuar...")
        elif opcion == "3":
            mostrarEmpleadosporID()
            input("Presiona Enter para continuar...")
        elif opcion == "4":
            editarEmpleado()
        elif opcion == "5":
            eliminarEmpleado()

        os.system('cls' if os.name == 'nt' else 'clear')
        
        if opcion == "6":
            break

menu_principal()