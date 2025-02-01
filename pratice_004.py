class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular # Atributo público
        self.__saldo = saldo    # Atributo privado
        
     # Metodos publicos para acceder con (getter)   
    def  consultar_saldo(self):
        return self.__saldo
    
    # Metodos publicos para acceder con (setter) 
    def deposito(self, monto):
        if monto > 0:
            self.__saldo += monto
            
    def retiro(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto        
              
    def verificacion(self):
        print(f"El saldo de la cuenta de {self.titular} es: {self.__saldo}") 
              
#uso de la clase

cuenta = CuentaBancaria("Juan", 1000)
print(cuenta.consultar_saldo())
cuenta.deposito(3000)
print(cuenta.consultar_saldo())

cuenta.retiro(820)
cuenta.retiro(800)

print(cuenta.consultar_saldo())

cuenta.verificacion()

