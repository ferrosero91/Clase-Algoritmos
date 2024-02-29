from cuentaAhorros import CuentaAhorros
from cuentaCorriente import CuentaCorriente
from CDT import CDT

#Codigo clase
class SimuladorBancario:
    #Atributos
    cedula = ""
    nombres = ""
    mesActual = 0

#ASOCIACIONES

corriente=CuentaCorriente()
ahorros=CuentaAhorros()
cdt=CDT()

'''
#METODOS
#consignar cuenta corriente
#calcular saldo total
#Pasar todo el saldo de ahorro a corriente

'''

#METODOS PARA CONSIGNAR   
def ConsignarCuentaCorriente(self, monto):

    return self.corriente.ConsignarCorriente(monto)

def ConsignarCuentaAhorros(self, monto):
    return self.ahorros.ConsignarAhorros(monto)

#METODOS PARA CONSULTAR SALDO

def SaldoCorriente(self):
     return self.corriente.ConsultarSaldoCorriente()

def SaldoAhorros(self):
     return self.ahorros.ConsultarSaldoAhorros()

def CalcularSaldoTotal(self):
    return "Su saldo total es "+ (self.SaldoCorriente + self.SaldoAhorros)

#METODO PARA PASAR DE AHORROS A CORRIENTE
def transferir_a_corriente(self):
        monto_a_transferir = self.SaldoAhorros()
        self.ConsignarCuentaCorriente(monto_a_transferir)
        return self.SaldoCorriente()

 #METODO PARA DUPLICAR AHORROS

def DuplicarAhorroCorriente (self):
    self.SaldoCorriente *=2  

def DuplicarAhorroAhorros (self):
    self.SaldoAhorros *=2  



#Consultar saldo corriente
#retirar todo
#duplicar ahorro


