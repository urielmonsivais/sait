from app.core.Model import Model
from app.models.Provider import Provider
from mysql.connector import Error


class Providers(Model):
    cursor = None

    def __init__(self, db):
        super().__init__(db)
        self.db = db
        self.cursor = self.db.get_connection().cursor()

    def add(self, p_data):
        try:
            result = self.cursor.execute(
                "INSERT INTO proveedor (id,	nombre,	rfc, telefono,	marca,status) values (%s,%s,%s,%s,%s,%s)",
                (None, p_data['nombre'], p_data['rfc'], p_data['telefono'], p_data['marca'],1))
            self.db.get_connection().commit()
                  
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def remove(self, p_data):
        try:
            result = self.cursor.execute("UPDATE proveedor SET status=%s WHERE id = %s",(0,p_data['proveedor_id']))
            self.db.get_connection().commit()
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def update(self, p_data):
        try:
            result = self.cursor.execute(
                "UPDATE proveedor SET nombre=%s, rfc=%s, telefono=%s, marca=%s WHERE id = %s",
                (p_data['nombre'], p_data['rfc'], p_data['telefono'], p_data['marca'], p_data['proveedor_id']))
            self.db.get_connection().commit()
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def getAll(self):
        try:
            self.cursor.execute("SELECT * FROM proveedor WHERE proveedor.status>=1")
            records = self.cursor.fetchall()
            return [Provider(x) for x in records]
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def __del__(self):
        try:
            if self.cursor:
                self.cursor.close()
        except Exception:
            pass
