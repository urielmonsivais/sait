from app.core.Model import Model
from app.models.User import User
from mysql.connector import Error
from enum import Enum


class Rols(Enum):
    SYSTEM = 0
    COMPANY_ADMIN = 1
    COMPANY_STANDARD = 2


class Users(Model):
    cursor = None

    def __init__(self, db):
        super().__init__(db)
        self.db = db
        self.cursor = self.db.get_connection().cursor()

    def add(self, user_data):
        try:
            result = self.cursor.execute(
                "INSERT INTO sucursal (id,nombre, ciudad, cp, rfc, razon_social, empresa) values (%s,%s,%s,%s,%s,%s,%s)",
                (None, user_data['branch_office'], 2, 0, '312', '213132', 1))
            self.db.get_connection().commit()
            
            c = self.db.get_connection().cursor(buffered=True)
            c.execute("select id from sucursal order by id desc")
            branch_id = c.fetchone()[0]
            self.cursor.execute(
                "INSERT INTO usuarios (id,nombre, telefono, correo, pass, sucursal, rol,status) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                (None, user_data['name'], user_data['phone'], user_data['email'], user_data['password'], branch_id, user_data['rol'],1))
            self.db.get_connection().commit()
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def remove(self, d):
        try:
            result = self.cursor.execute("UPDATE usuarios SET status=%s WHERE id = %s",(0,d['user_id']))
            self.db.get_connection().commit()
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def update(self, d):
        try:
            result = self.cursor.execute(
                "UPDATE usuarios SET nombre=%s, telefono=%s, correo=%s, pass=%s, rol=%s WHERE id = %s",
                (d['name'], d['phone'], d['email'], d['password'], d['rol'], d['user_id']))
            self.db.get_connection().commit()
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            self.db.close()

    def getAll(self):
        try:
            self.cursor.execute(
                "SELECT usuarios.*, sucursal.nombre FROM usuarios INNER JOIN sucursal on usuarios.sucursal = sucursal.id WHERE usuarios.status>=1")
            records = self.cursor.fetchall()
            return [User(x) for x in records]
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
