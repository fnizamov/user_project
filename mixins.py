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

class UpdateMixin:
    def update(self):
        model = self._model

        data = self.get_db_content()
        user = self.get_user_by_id()
        if user is not None:
            data['users'].remove(user)
            name = input('Введите имя: ') or user['name']
            last_name = input('Введите фамилию: ') or user['last_name']
            birth_day = input('Введите дату рождения: ') or user['birth_day']

            new_user = model(name = name, last_name = last_name, birth_day = birth_day)
            new_user.__dict__['id'] = user['id']
            data['users'].append(new_user.as_dict)
            self.write_to_db(data)
            print('Данные успешно обновлены.')
        else:
            print('Указанный ID не найден.')

class DeleteMixin:
    def delete(self):
        data = self.get_db_content()
        user = self.get_user_by_id()
        if user is not None:
            data['users'].remove(user)
            data.update(counter=len(data['users']))
            self.write_to_db(data)
            print('Пользователь успешно удален!')
        else:
            print('Указанный ID не найден.')