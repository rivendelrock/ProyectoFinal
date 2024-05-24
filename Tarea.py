
#Clase tarea con 2 atributos, el nombre de la tarea y el estado (completada o no)

class Tarea():

    nombre = " "
    estado = "Pendiente"
#Constructor de objeto tarea
    def __init__ (self,nombre):
        self.nombre = nombre
        self.estado= "Pendiente"
 #Mostrar tarea por pantalla   
    def mostrarTarea (self):
        print("Tarea:"+ self.nombre + " ---> " + self.estado)
 #Completar la tarea   1

    def completarTarea (self):
        self.estado = "Completada"