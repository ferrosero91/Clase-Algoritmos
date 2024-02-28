class Empleado:
    #Atributos
    nombre = ""
    apellido = ""
    ''' ----------------------------------
    # sexo 1= masculino 2= femenino
    -----------------------------------'''
    sexo = 0
    salario = 0

          #metodos
    def CambiarSalario (self, nuevoSalario):
        #aqui va el codigo del metodo
        return 0

    def CambiarEmpleado (self, nNombre, nApellido, nSexo, nSalario):
        #aqui va el codigo del nuevo empleado
        return None
    
    def ConsultarSalario(self):
        #aqui va el codigo del metodo
        return self.salario
    
    def ConsultarNombre(self):
        #aqui va el codigo del metodo
        return self.nombre
    
    def ConsultarApellido(self):
        #aqui va el codigo del metodo
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        #aqui va el codigo del metodo
        return self.nombre + " " + self.apellido
    
    def AumentoSalarial(self):
        nSalario = self.salario*0.05
        nsalario =nSalario + self.salario
        self.salario = nsalario
        return "el nuevo salario es de: " + self.salario



    
    

        
    