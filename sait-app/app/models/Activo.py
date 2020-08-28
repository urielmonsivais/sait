#id	nombre	caracteristica	marca	modelo	no_serie	garantia	pago	proveedor	status	
class Activo():    
    def __init__(self, d):
        self.id = d[0]
        self.nombre = d[1]
        self.caracteristicas = d[2]
        self.marca = d[3]
        self.modelo = d[4]
        self.no_serie = d[5]
        self.garantia = d[6]
        self.pago = d[7]
        self.proveedor = d[8]

        self.provider_name = d[10]
        #relation ship with payment periods
        self.f_inicio = d[12]
        self.f_termino = d[13]
        self.f_corte = d[14]
        self.f_pago = d[15]
        self.periodo = d[16]