class Model():
    
    def __init__(self,db):
        self.db = db
        self.db.open()
        self.cursor = self.db.connection.cursor()

    def __del__(self):
        print("Delete model")
        self.db.close()