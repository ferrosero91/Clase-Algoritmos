from Fecha import Fecha

class Empleado:
    #Atributos
    nombre = ""
    apellido = ""
    ''' ----------------------------------
    # sexo 1= masculino 2= femenino
    -----------------------------------'''
    sexo = 0
    salario = 0
    '''---------------------------------------------
    #Asociaciones
    ----------------------------------------'''

    fechaNacimiento=Fecha()
    fechaIngreso=Fecha()

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
    
    def DuplicarSalario(self):
        #aqui va el codigo 
        # asignacion forma 1
        #self.salario = self.salario * 2
        #Asignacion numero 2
        self.salario *= 2

    def CalcularSalarioAnual (self):
        #metodo 1
        salarioAnual = self.salario*12
        return salarioAnual
        #metodo 2
        #return self.salario*12
    

    def ConsultarDiaCumpleaños(self):
        return "El dia de su cumpleaños es: " + self.fechaNacimiento.ConsultarDia()
    
    def CalcularImpuesto(self):
    #Forma 1
     total=self.CalcularSalarioAnual()
     return total * 19.5/100

     #forma 2
    # return self.CalcularSalarioAnual()*0.195
      
    

    




    




    
    

        
    