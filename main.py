import telebot
from telebot import types

bot = telebot.TeleBot('1474069019:AAGPrloywp4Te6OwRJSJPS8vMusdSxLigLk');

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id == 866525795:
        name = "Вітаю повелителю!"
        bot.send_message(message.chat.id, name)
        #bot.send_photo(message.chat.id, "https://i.pinimg.com/originals/38/64/bc/3864bc12053a5b3cd101dcee543dfc44.png", caption=name)
    elif message.from_user.last_name==None:
        name = f"Вітаю {message.from_user.first_name}!"
        bot.send_message(message.chat.id, name)
    else:
        name = f"Вітаю  {message.from_user.first_name} { message.from_user.last_name} !"
        bot.send_message(message.chat.id, name)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    hello = types.KeyboardButton("Почати гру")
    markup.add(hello)
    bot.send_message(message.chat.id, "Натисніть що почати гру.", reply_markup=markup)

@bot.message_handler(ext=['Почати гру'])
# def play(message):


@bot.message_handler(commands=['myid'])
def myid(message):
    bot.send_message(message.chat.id, "Your id: " + str(message.chat.id))

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_photo(message.chat.id, "https://memepedia.ru/wp-content/uploads/2020/09/kloun.jpg")

bot.polling(none_stop=True)