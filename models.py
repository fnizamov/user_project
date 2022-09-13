from utils import Id, Date

class User:
    def __init__(self, name: str, last_name: str, birth_day: str):
        self.__id = Id().id_
        self._name = name
        self._last_name = last_name
        self._birth_day = Date(birth_day)
        self.age = Date.calculate_age(self._birth_day)