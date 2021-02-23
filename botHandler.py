import ponchi.db as db
import ponchi.session as session
import ponchi.config as cfg


def update(msg, bot):
    """
    Код обработки сессии
    """

    # получение данных чата из базы
    chat_data = db.get_chat_data(str(msg.chat.id))

    # Если чат новый, то вместо данных вернется None
    # В этом случае создается пользователь
    # И выставляются пустые данные
    if chat_data == None:
        chat_data = db.create_chat(str(msg.chat.id))

    # Преобразование данных из JSON в объект данных сессии
    chat_session_data = session.Session(chat_data.session_data)

    # Выполнение текущей функции
    # И получение следующей
    next_function = getattr(
        cfg.app,
        chat_data.next_function
    )(
        msg, 
        bot, 
        chat_session_data
    )

    # Если вернулась функция
    if type(next_function) == type(lambda: None):
        # То получения ее имени
        next_function = next_function.__name__

    # Обновление данных о сесси
    db.update_chat_data(
        str(msg.chat.id),
        next_function,
        # Парсинг данных о сессии в JSON
        chat_session_data.parse_self_to_json()
    )
