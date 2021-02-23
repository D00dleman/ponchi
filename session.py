import json


class Session:
    """
    Класс с данными сессии пользователя
    Лучше хранить только данные, которые можно сереализовать в JSON
    Но при этом можно не париться со скобками и кавычками,
    И работать как с обычным объектом.

    Да, по факту сахар
    Но вся эта библиотека - сахар
    """
    def __init__(self, json_session_data_string):
        """
        Получение строки в JSON
        И сериализация в параметры объекта
        """
        session_data_dict = json.loads(json_session_data_string)
        for i in session_data_dict:
            self.__setattr__(i, session_data_dict[i])

    def create_new_value(self, key, value):
        """
        Создает новый параметр объекта
        """
        self.__setattr__(key, value)

    def delete_value(self, key):
        """
        Удаляет параметр объекта

        ОЧЕНЬ ОПАСНАЯ ШТУКА
        Использовать аккуратно
        Ибо если удалить не то, то будет плохо
        """
        deleted_value = self.__dict__[key]
        del self.__dict__[key]
        return deleted_value

    def parse_self_to_json(self):
        """
        Возвращает десериалезированный в JSON объект
        (строку)
        Для записи в БД
        """
        return json.dumps(self.__dict__)
