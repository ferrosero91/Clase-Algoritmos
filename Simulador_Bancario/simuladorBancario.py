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


#METODOS
#consignar cuenta corriente
#calcular saldo total
#Pasar de ahorro a corriente
    
def ConsignarCuentaCorriente(self, monto):

    return self.corriente.Consignar(monto)

def CalcularSaldoTotal():

    return "Su saldo total es "+ (self.ahorros.saldo + self.corriente.saldo)

def PasarAhorroCorriente():
    return 0 



#Consultar saldo corriente
#retirar todo
#duplicar ahorro


