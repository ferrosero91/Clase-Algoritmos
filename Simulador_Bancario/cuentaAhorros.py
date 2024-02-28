#Codigo clase
class CuentaAhorros:
    #Atributos
    saldo = 0
    interesMensual = 0


'''-------------------------------------------------
#metodos

-------------------------------------------------'''
def Consignar (self, monto):
    self.saldo = self.saldo + monto
    return "Valor consignado correctamente, Su nuevo saldo es" + self.saldo


def darinteres (self):
    interes = self.saldo * self.interesMensual
    nsaldo = self.saldo + self.interes
    return "El nuevo saldo es de " + self.nsaldo

def retirar (self, monto):
    if monto <= self.saldo:
        self.saldo = self.saldo - monto
        return "El retiro fue exitoso, el nuevo saldo es de " + self.saldo


