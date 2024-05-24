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

#Menu de opciones que se muestran por patalla
def menu():
    print ("Escoge una opción:\n")
    print ("1. Agregar una tarea.\n")
    print ("2. Marcar una tarea como completada.\n")
    print ("3. Mostrar todas las tarea.\n")
    print ("4. Eliminar una tarea.\n")
    print ("5. Fin.\n")
    entrada = input ()
    return entrada
#Declaramos una lista de tareas vacía
listaTareas = list()

#En este método agregamos una tarea al primer espacio vacío de la lista o al final. 
def agregarTarea():
    
       print ("Introduzca el nombre de la tarea pendiente a agregar:")
       nuevaTarea = input()
       tarea1 = Tarea (nuevaTarea)
       try:
            index = listaTareas.index(None)
            listaTareas[index] = tarea1
       except:
            listaTareas.append(tarea1)
       finally:
            print("\nTarea insertada correctamente.")
            mostrarTareas()
            casos ()
#Método para completar una tarea. Recorre la lista para ver si existe el nombre introducido, si lo encuentra, llama a la función
#para completar la tarea, si no lo encuentra, envía un mensaje de que la tarea no existe. Tras finalizar vuelve al menu. 
def completarTarea():
       print ("Introduzca el nombre de la tarea que desea completar")
       try:
           nombre = input()
           existe = False
           for i in listaTareas:
                
                if i.nombre == nombre:
                    i.completarTarea()
                    existe = True                    
                    print ("La tarea se ha completado. ")
                    mostrarTareas()
                    break
           if existe == False:
                    print ("La tarea no existe")
                    a = input()
       except:
            print ("Error al completar la tarea")
            a = input()
       finally: 
            casos()
#Función que recorre la lista de tareas y las muestra junto a su estado (completado o pendiente)
def mostrarTareas():
      for i in listaTareas:
            print ("Tarea:"+ i.nombre + " ---> " + i.estado)
      print("\nPulsa intro para continuar:")
      a = input()
      casos ()

#Función que elimina una tarea. Recorre el array comparandolo con el nombre introducido por el usuario. Si encuentra la tarea 
#la borra y romple el bucle. Si no la encuentra muestra un mensaje por pantalla de que la tarea no se encontrado.
def eliminarTarea():
       print ("Introduzca el nombre de la tarea que desea eliminar")
       try:
            nombre = input()
            existe = False
            for i in listaTareas:
                if i.nombre == nombre:
                    listaTareas.remove(i)
                    existe = True
                    print ("La tarea se ha eliminado correctamente.")
                    mostrarTareas()
                    a= input()
                    break
            if existe == False:
                print ("\nLa tarea no existe.")
       except:
            print ("\nError al borrar la tarea")
            a = input()
       finally: 
            casos ()
#Esta función muestra el menu y recoge la respuesta que introduce el usuario. Dependiendo de la respuesta le envía a la
#opción correspondiente. Si la respuesta introducida no es válida muestra un error por pantalla y vuelve a llamar al menu. 
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
        print("La opción introducida no es válida.")
        casos()
#Se llama a la función casos para comenzar el programa. 
casos()