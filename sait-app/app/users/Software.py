from app.core.Model import Model
from app.models.Software import Software
from app.models.Provider import Provider
from app.models.Type import Type
from mysql.connector import Error
from enum import Enum


class Softwares(Model):
    cursor = None

    def __init__(self, db):
        super().__init__(db)    
        self.db = db
        self.cursor = self.db.get_connection().cursor()


    def add(self, soft_data):
        try:
            result = self.cursor.execute("INSERT INTO periodo_pago (id, f_inicio, f_termino, f_corte, periodo) values (%s, %s, %s, %s, %s)",(None, soft_data['f_inicio'], soft_data['f_termino'], soft_data['f_corte'], soft_data['periodo']))
            self.db.get_connection().commit()
            periodo_id = self.cursor.lastrowid
            print(periodo_id)
            result = self.cursor.execute(
                "INSERT INTO software (id,nombre, version, vigencia, f_compra, tipo, pago, proveedor, status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (None, soft_data['nombre'], soft_data['version'], soft_data['vigencia'], soft_data['f_compra'], soft_data['tipo'], periodo_id, soft_data['proveedor'],1))
            print(result)
            self.db.get_connection().commit()        
            
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def remove(self, sw):
        try:
            result = self.cursor.execute("UPDATE software SET status=%s WHERE id = %s",(0,sw['software_id']))
            self.db.get_connection().commit()
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def update(self, sw):
        try:
            result = self.cursor.execute(
                "UPDATE software SET nombre=%s, version=%s, vigencia=%s, f_compra=%s, tipo=%s, pago=%s,  proveedor=%s WHERE id = %s",
                (sw['nombre'], sw['version'], sw['vigencia'], sw['compra'], sw['tipo'], sw['pago'], sw['proveedor'], sw['id']))
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
            self.cursor.execute("SELECT s.*, t.nombre, p.nombre FROM software AS s INNER JOIN tipo_sw AS t ON  s.tipo = t.id INNER JOIN proveedor AS p ON s.proveedor=p.id WHERE s.status>=1")
            records = self.cursor.fetchall()            
            return [Software(x) for x in records]
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