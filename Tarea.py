
#Clase tarea con 2 atributos, el nombre de la tarea y el estado (completada o no) y un método para completar la tarea

class Tarea():

    nombre = " "
    estado = "Pendiente"
#Constructor de objeto tarea
    def __init__ (self,nombre):
        self.nombre = nombre
        self.estado= "Pendiente"

#Completar la tarea
    def completarTarea (self):
        self.estado = "Completada"