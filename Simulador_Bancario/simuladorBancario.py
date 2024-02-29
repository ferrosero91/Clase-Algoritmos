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
#Pasar todo el saldo de ahorro a corriente
    
def ConsignarCuentaCorriente(self, monto):

    return self.corriente.Consignar(monto)

def ConsignarCuentaAhorros(self, monto):
    return self.ahorros.Consignar(monto)

def CalcularSaldoTotal():

    return "Su saldo total es "+ (self.ahorros.saldo + self.corriente.saldo)

def transferir_a_corriente(self):
        monto_a_transferir = self.ahorros.saldo()
        self.ConsignarCuentaCorriente(monto_a_transferir)
        return self.corriente.saldo()

   



#Consultar saldo corriente
#retirar todo
#duplicar ahorro


