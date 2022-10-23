from nturl2path import url2pathname
import telebot
from telebot import types

bot = telebot.TeleBot('5511420009:AAGZ3Jz6VuA0KpIamxL-CnoloVxpneLrcMo')

@bot.message_handler(commands=['start'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Black King Bar', url='https://holder-hash.github.io/black-king-bar/'))
    markup.add(types.InlineKeyboardButton('Clicker', url='https://holder-hash.github.io/web-clicker-js/'))
    bot.send_message(message.chat.id, 'Выберите сайт:', reply_markup=markup)

bot.polling(none_stop=True,interval=0)