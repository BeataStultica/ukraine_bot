import telebot
import random
bot = telebot.TeleBot('1592401896:AAFMU7f-u1LSHeJocnJknQfVsVCiSi2RVTs')

@bot.message_handler(content_types=[
    "new_chat_members"
])


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




bot.polling()
