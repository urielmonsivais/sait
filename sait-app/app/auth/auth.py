class Auth():
    
    def __init__(self, session,g ,db):        
        self.session = session
        self.g = g
        self.db = db
        self.db.open()        
    
    def check_session(self):
        if 'current_user' in self.session:
            return self.session['current_user']
        return None
    
    def check_user(self, user, pwd):
        try:
            if self.db.is_connected() is None:
                self.db.open()                
            sql = '''SELECT * FROM usuarios WHERE correo=%s AND pass=%s'''            
            cursor = self.db.get_connection().cursor(buffered=True)
            result = cursor.execute(sql,(user,pwd))
            data = cursor.fetchone()            
            if data is None:
                return False            
            self.session['current_user'] = data
            self.g.user = data
            cursor.close()
            return True
        except Exception as e:
            print("error auth: ")
            print(e)
            
    def logout(self):
        self.session['current_user'] = None
        self.session.clear()
        
    def __del__(self):
        try:
            self.db.close()
        except Exception:
            pass