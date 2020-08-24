from app.models.User import User

class EntityFactory():

    def makeList(self, entity, records)
        collection = []
        if entity == 'User':
            return [User(x) for x in records]

    
