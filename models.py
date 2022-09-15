from utils import Id, Date

class User:
    def __init__(self, name: str, last_name: str, birth_day: str):
        self.id = Id().id_
        self.name = name
        self.last_name = last_name
        self.birth_day = Date(birth_day)
        self.age = Date.calculate_age(self.birth_day)
    
    
    @property
    def as_dict(self):
        self.__dict__['birth_day'] = str(self.__dict__['birth_day'])
        return self.__dict__



if __name__ == "__main__":
    obj = User('Aygul', 'Maratova', '12.12.1998')
    print(obj.as_dict)