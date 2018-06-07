# -*- coding: utf-8 -*-
import config
import telebot
import datetime
from telebot import apihelper
from telebot import types
apihelper.proxy = {'https':'https://35.199.64.211:80'}

bot = telebot.TeleBot(config.token)
#def datefun():
#	now = datetime.datetime.now
#	time1now = datetime.datetime.time()
#	return time1now

@bot.message_handler(content_types=["text"])
def repeating_messages(message):
	if message.text=="/help":
		bot.send_message(message.chat.id,"List of commands")
	if message.text=="/data":
		bot.send_message(message.chat.id,datetime.datetime.today().strftime("%d/%m/%y %H:%M"))
if __name__ == '__main__':
		bot.polling(none_stop=True)
