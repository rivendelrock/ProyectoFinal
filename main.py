from Tarea import Tarea


#Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione
# una lista de tareas pendientes. El programa deberá permitir al usuario realizar las siguientes
# operaciones:
# • Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a
# la lista de tareas pendientes.
# • Marcar una tarea como completada: El programa deberá permitir al usuario marcar una
# tarea como completada, dada su posición en la lista.
# • Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas
# pendientes, numeradas y mostrando su estado (completada o pendiente).
# • Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista,
# dada su posición.

def menu():
    print ("Escoge una opción:\n")
    print ("1. Agregar una tarea.\n")
    print ("2. Marcar una tarea como completada.\n")
    print ("3. Mostrar todas las tarea.\n")
    print ("4. Eliminar una tarea.\n")
    print ("5. Fin.\n")
    entrada = input ()
    return entrada

listaTareas = list()
contador = 0

def agregarTarea():
    
       print ("Introduzca el nombre de la tarea pendiente a agregar")
       nuevaTarea = input()
       tarea1 = Tarea (nuevaTarea)
       try:
            index = listaTareas.index(None)
            listaTareas[index] = tarea1
       except:
            listaTareas.append(tarea1)
       finally:
            print("\nTarea insertada correctamente. Pulsa cualquier tecla para continuar:")
            a = input()
            casos ()

def completarTarea():
       print ("Introduzca el nombre de la tarea que desea completar")
       try:
           nombre = input()
           existe = False
           for i in listaTareas:
                
                if i.nombre == nombre:
                    i.completarTarea()
                    existe = True
                    print ("La tarea se ha completado. Pulsa intro para continuar:")
                    a= input()
                    break
           if existe == False:
                    print ("La tarea no existe")
                    a = input()
       except:
            print ("Error al completar la tarea")
            a = input()
       finally: 
            casos()

def mostrarTareas():
      for i in listaTareas:
            print (i.mostrarTarea())
      print("\nPulsa intro para continuar:")
      a = input()
      casos ()
def eliminarTarea():
       print ("Introduzca el nombre de la tarea que desea eliminar")
       try:
            nombre = input()
            existe = False
            for i in listaTareas:
                if i.nombre == nombre:
                    listaTareas.remove(i)
                    existe = True
                    print ("La tarea se ha eliminado correctamente. Pulsa intro para continuar:")
                    a= input()
                    break
            if existe == False:
                print ("\nLa tarea no existe.")
       except:
            print ("\nError al borrar la tarea")
            a = input()
       finally: 
            casos ()

def casos ():   
    respuesta = menu()   
    if respuesta == "1": 
        agregarTarea()
    elif respuesta == "2":
        completarTarea()
    elif respuesta == "3":
        mostrarTareas()
    elif respuesta == "4":
        eliminarTarea()
    elif respuesta == "5":
        print ("Terminando Programa")
    else:
        print("Número inválido")
        casos()

casos()