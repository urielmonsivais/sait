class Service():    
    def __init__(self, d):
        self.id = d[0]
        self.nombre = d[1]
        self.caracteristicas = d[2]
        self.pago = d[3]
        self.proveedor = d[4]

        self.provider_name = d[6]
        #relation ship with payment periods
        self.f_inicio = d[8]
        self.f_termino = d[9]
        self.f_corte = d[10]
        self.f_pago = d[11]
        self.periodo = d[12]