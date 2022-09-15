import uuid
import datetime


class Id:
    def __init__(self) -> None:
        self._id = self.generate_id()


    @staticmethod
    def generate_id():
        return str(uuid.uuid4())

    @property
    def id_(self):
        return self._id



class Date:
    __KG_DATE_FORMAT = '%d.%m.%Y'


    def __init__(self, date) -> None:
        self.date = self.format_date(date)
        self.age = self.calculate_age()

    @classmethod
    def format_date(cls, date: str) -> datetime:
        'DD.MM.YYYY'
        d = datetime.datetime.strptime(date, cls.__KG_DATE_FORMAT)
        return d

    def calculate_age(self):
        age = (datetime.datetime.now() - self.date).days // 365
        return age

    def __str__(self):
        return self.date.strftime(self.__KG_DATE_FORMAT)

    def __repr__(self):
        return self.date.strftime(self.__KG_DATE_FORMAT)

if __name__ == '__main__':
    id_obj = Id()
    # print(id_obj.id_)
    date_obj = Date('29.12.1988')
    print(date_obj.age)
    print(date_obj.date)
    print(date_obj)
