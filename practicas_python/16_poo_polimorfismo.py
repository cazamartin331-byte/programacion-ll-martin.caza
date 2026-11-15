# Práctica 16: POO - polimorfismo
# Autor: Martin Caza


class Pago:
    def procesar(self, monto):
        raise NotImplementedError("Cada tipo de pago define su proceso")


class PagoEfectivo(Pago):
    def procesar(self, monto):
        return f"Pago en efectivo de ${monto:.2f} recibido"


class PagoTarjeta(Pago):
    def procesar(self, monto):
        comision = monto * 0.03
        return f"Pago con tarjeta de ${monto:.2f} (comisión ${comision:.2f})"


class PagoTransferencia(Pago):
    def procesar(self, monto):
        return f"Transferencia de ${monto:.2f} pendiente de verificación"


# Mismo método, comportamiento distinto según el objeto
pagos = [PagoEfectivo(), PagoTarjeta(), PagoTransferencia()]
for pago in pagos:
    print(pago.procesar(25))
