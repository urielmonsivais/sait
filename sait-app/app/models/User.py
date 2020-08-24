
class User():
    id = None
    name = None
    phone = None
    email = None
    password = None
    branch_office = None
    rol = None
    rol_name = None

    branch_name = None

    def collect(self):
        return [
            self.id,
            self.name,
            self.phone,
            self.email,
            self.password,
            self.rol,
            self.branch_name
        ]
        # return {
        #     'id': self.id,
        #     'name': self.name,
        #     'phone': self.phone,
        #     'email': self.email,
        #     'password': self.password,
        #     'rol': self.rol,
        #     'branchName': self.branch_name
        # }

    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.phone = data[2]
        self.email = data[3]
        self.password = data[4]
        self.branch_office = data[5]
        self.rol = data[6]
        self.branch_name = data[7]

        if self.rol == 0:
            self.rol_name = 'SAIT_ADMIN'
        elif self.rol == 1:
            self.rol_name = 'COMPANY_ADMIN'
        else:
            self.rol_name = 'COMPANY_STANDARD'
