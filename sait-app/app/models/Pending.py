class Pending():
    def __init__(self,d):
        self.id = d[0]
        self.nombre = d[1]
        self.version = d[2]
        self.vigencia = d[3]
        self.f_compra = d[4]
        self.tipo = d[5]
        self.pago = d[6]
        
        self.f_pago = d[13]
    