class Company():
    def __init__(self, data):
        self.id = data[0]
        self.nombre = data[1]
        self.rfc = data[2]
        self.razon_social = data[3]
        
        self.sucursal = data[4]
        self.ciudad = data[5]

        self.cp = data[6]
        self.telefono = data[7]