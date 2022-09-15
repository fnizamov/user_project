import json
from pprint import pprint

class JsonMixin:
    def get_db_content(self):
        try:
            with open(self._file_name, 'r') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return {'users': [], 'counter': 0}

    def write_to_db(self, data):
        with open(self._file_name, 'w') as file:
            json.dump(data, file, indent=4)


class CreateMixin:
    def create(self):
        name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        birth_day = input('Введите дату рождения: ')
        model = self._model(name=name, last_name=last_name, birth_day=birth_day)
        data = self.get_db_content()
        data['users'].append(model.as_dict)
        data.update(counter=len(data['users']))
        self.write_to_db(data)
        print('Пользователь успешно добавлен!')



class ReadMixin:
    def list(self):
        data = self.get_db_content()
        pprint(data)

    def get_user_by_id(self):
        user_id = input('Введите ID: ')
        data = self.get_db_content()
        users = data['users']
        res = list(filter(lambda x: x['id'] == user_id, users))
        pprint(res[0] if res else 'Указанный ID не найден')
        return res[0] if res else None