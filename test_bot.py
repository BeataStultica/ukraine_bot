import telebot
import random
from flask import Flask, request
import logging
import os

bot = telebot.TeleBot('1592401896:AAFMU7f-u1LSHeJocnJknQfVsVCiSi2RVTs')
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

server = Flask(__name__)

@bot.message_handler(content_types=["new_chat_members"])
def foo(message):

    questions={'Хіба ревуть воли':'ясла',
                'Мертві бджоли':'гудуть',
                'Олені олені':'не бриті',
                'Червону руту не шукай ':'вечорами',
                'Щедрий вечір ':'тобі',
                'Твої зелені очі':'дивляться',
                'Така як ти':'буває',
                'Давай виключим світло':'мовчати',
                'Старі фотографії на стіл':'розклади'
                }

    bot.reply_to(message, "Продовжи в Reply "+random.choice(list(questions.keys())))


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://norussianbot.herokuapp.com/bot")
    return "?", 200
server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
