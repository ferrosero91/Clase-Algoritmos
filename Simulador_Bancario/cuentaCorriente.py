#Codigo clase
class CuentaCorriente:
    #atributos
    saldo = 0

def ConsultarSaldoCorriente(self):
    return self.saldo

def ConsignarCorriente(self, monto):
    return self.saldo + monto

def retirar (self, monto):
    if monto <= self.saldo:
        self.saldo = self.saldo - monto
        return "El retiro fue exitoso, el nuevo saldo es de " + self.saldo

