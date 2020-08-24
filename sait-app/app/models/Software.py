class Software():
        
    def __init__(self, data):
        print("data: ")
        print(data)
        
        self.id = data[0]
        self.nombre = data[1]
        self.version = data[2]
        self.vigencia = data[3]
        self.f_compra = data[4]
        self.tipo = data[5]
        self.pago = data[6]
        self.proveedor = data[7]

        self.type_name = data[9]
        self.provider_name = data[10]