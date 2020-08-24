#id	nombre	caracteristica	marca	modelo	no_serie	garantia	pago	proveedor	status	
class Activo():    
    def __init__(self, d):
        self.id = d[0]
        self.nombre = d[1]
        self.caracteristicas = d[2]
        self.marca = d[3]
        self.modelo = d[4]
        self.n_serie = d[5]
        self.garantia = d[6]
        self.pago = d[7]
        self.proveedor = d[8]

        self.provider_name = d[9]
        #relation ship with payment periods
        self.f_inicio = d[10]
        self.f_termino = d[11]
        self.f_corte = d[12]
        self.f_pago = d[13]
        self.periodo = d[14]