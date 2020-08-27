from app.core.Model import Model
from app.models.Software import Software
from app.models.Service import Service
from app.models.Provider import Provider
from app.models.Type import Type
from mysql.connector import Error
from enum import Enum


class Services(Model):
    cursor = None

    def __init__(self, db):
        super().__init__(db)    
        self.db = db
        self.cursor = self.db.get_connection().cursor()


    def add(self, soft_data):
        try:
            result = self.cursor.execute("INSERT INTO periodo_pago (id, f_inicio, f_termino, f_corte, f_pago, periodo) values (%s, %s, %s, %s, %s, %s)",(None, soft_data['f_inicio'], soft_data['f_termino'], soft_data['f_corte'],soft_data['f_pago'], soft_data['periodo']))
            self.db.get_connection().commit()
            periodo_id = self.cursor.lastrowid            
            result = self.cursor.execute(
                "INSERT INTO servicios (id,nombre, caracteristicas, pago, proveedor, status) values (%s,%s,%s,%s,%s,%s)",
                (None, soft_data['nombre'], soft_data['caracteristicas'], periodo_id, soft_data['proveedor'],1))            
            self.db.get_connection().commit()
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def remove(self, sw):
        try:
            result = self.cursor.execute("UPDATE servicios SET status=%s WHERE id = %s",(0,sw['service_id']))
            self.db.get_connection().commit()
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def update(self, sw):
        try:
            print('data: ',sw)
            print('data to update')
            print(sw)
            r = self.cursor.execute(
                "UPDATE periodo_pago SET f_inicio=%s, f_termino=%s, f_corte=%s, f_pago=%s, periodo=%s WHERE id = %s",
                (sw['f_inicio'],sw['f_termino'],sw['f_corte'],sw['f_pago'],sw['periodo'],sw['pago'])
            )
            self.db.get_connection().commit()
            result = self.cursor.execute(
                "UPDATE servicios SET nombre=%s, caracteristicas=%s, proveedor=%s WHERE id = %s",
                (sw['nombre'], sw['caracteristicas'], sw['proveedor'], sw['service_id']))
            self.db.get_connection().commit()
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def getProviders(self):
        try:
            self.cursor.execute("SELECT * from proveedor")
            records = self.cursor.fetchall()                        
            return [Provider(x) for x in records]
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            pass#self.db.close()

    def getTypes(self):
        try:
            self.cursor.execute("SELECT * from tipo_sw")
            records = self.cursor.fetchall()                        
            return [Type(x) for x in records]
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            pass

    def getAll(self):
        try:
            self.cursor.execute("SELECT s.*, p.nombre, pp.* FROM servicios AS s INNER JOIN proveedor AS p ON s.proveedor=p.id inner JOIN periodo_pago as pp ON s.pago=pp.id WHERE s.status>=1")
            records = self.cursor.fetchall()
            return [Service(x) for x in records]
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            pass#self.db.close()
    
    def getActivos(self):
        try:
            self.cursor.execute("SELECT s.*, p.nombre, pp.* FROM activos AS s INNER JOIN proveedor AS p ON s.proveedor=p.id inner JOIN periodo_pago as pp ON s.pago=pp.id WHERE s.status>=1")
            records = self.cursor.fetchall()
            return [x for x in records]
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            pass#self.db.close()

    def __del__(self):
        try:
            self.db.close()
            if self.cursor:
                self.cursor.close()
        except Exception:
            pass
