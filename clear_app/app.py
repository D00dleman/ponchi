def start(msg, bot, session):
    bot.send_message(
        msg.chat.id,
        "Hi, {0}.\nYou send: {1}".format(msg.chat.id, msg.text)
    )
    return start
