# -*- coding: utf-8 -*-
import config
import telebot
from telebot import apihelper
#apihelper.proxy = {'https':'https://79.120.177.106:8080'}
bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=["text"])
def repeating_messages(message):
	bot.send_message(message.chat.id, message.text)
if __name__ == '__main__':
		bot.polling(none_stop=True)
