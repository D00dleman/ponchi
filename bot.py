"""
Ну это обычный бот на pytelegrambotapi
"""

import telebot
import ponchi.config as cfg
import ponchi.botHandler as botHandler


if cfg.token == "":
    print("Add token to config")
    exit()
else:
    bot = telebot.TeleBot(cfg.token)


# Лямбда нужна, чтобы обрабатывать любое сообщеие
@bot.message_handler(func=lambda x: True)
def message(msg):
    botHandler.update(msg, bot)


bot.polling(none_stop=True)
