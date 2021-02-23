import ponchi.config as cfg
from pony.orm import *
import pony
from ponchi.timer import Timer

# Создание объекта таймера для коммитов в БД
timer = Timer(cfg.time_to_commit_db)


# Нужно было как-то коммитить в БД
# И я не придумал ничего лучше,
# Чем декоратор с таймером
def timer_to_commit_db(func):
    def committer(*args, **kwargs):
        # Он просто раз какое-то время возвращает True
        # И делает коммит в базу
        if timer.time_out():
            db.commit()
        # И вызывает функцию
        return func(*args, **kwargs)

    return committer


db = Database(**cfg.db)


# Просто таблица в БД
# Выбрал ORM, ибо было лень писать запросы под все БД
# Хоть они и были простыми
# А пони потому, что не осилил алхимию
class Chats(db.Entity):
    chat_id = Required(str)
    next_function = Required(str, default='start')
    session_data = Required(str, default='{}')


db.generate_mapping(create_tables=True)


@timer_to_commit_db
def create_chat(chat_id: str):
    """
    Создание чата по chat id
    """
    with pony.orm.db_session:
        temp_chat = Chats(chat_id=chat_id)
    return temp_chat


@timer_to_commit_db
def get_chat_data(chat_id: str):
    """
    Получение данных чата по chat id
    """
    with pony.orm.db_session:
        tmp = Chats.get(chat_id=chat_id)
    return tmp


@timer_to_commit_db
def update_chat_data(chat_id: str, function_name: str, session_data: str):
    """
    Обновление данных чата
    """
    with pony.orm.db_session:
        edited_chat = Chats.get(chat_id=chat_id)
        edited_chat.next_function = function_name
        edited_chat.session_data = session_data
    return edited_chat
