from models import User
from mixins import JsonMixin, CreateMixin, ReadMixin, UpdateMixin, DeleteMixin

class CRUD(JsonMixin, CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    _file_name = '/home/fnizamov/Makers/user_project/db.json'
    _model = User


    def help(self):
        print(
            """
            create  - создание записи
            list    - список записей
            details - получение подробной информации по ID
            update  - обновление записи
            delete  - удаление записи
            help    - список команд
            quit    - выход
            """
        )


    def start(self):
        commands = {
            'create': self.create,
            'list': self.list,
            'details': self.get_user_by_id,
            'update': self.update,
            'delete': self.delete,
            'help': self.help
            
        }
        while True:
            try:
                command = input('Введите команду или help для получения списка команд: ').lower().strip()
                if command in commands:
                    commands[command]()
                elif command == 'quit':
                    print('До свидания!')
                    break
                else:
                    print('Вы ввели неверную команду.')
            except KeyboardInterrupt:
                break
            except:
                print('Произошла ошибка!!!')

crud = CRUD()
# crud.create()
# crud.list()
# crud.get_user_by_id()
# crud.update()
# crud.delete()
crud.start()