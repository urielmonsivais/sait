class BranchOffice(object):
    def __init__(self, id, name, city, cp, phone,rfc, bussiness_name, company, users=None):
        self.id = id
        self.name = name
        self.city = city
        self.cp = cp
        self.phone = phone
        self.rfc = rfc
        self.bussiness_name = bussiness_name
        self.company = company
        self.users = users
