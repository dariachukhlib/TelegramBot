import telebot

bot = telebot.TeleBot('5720291546:AAGEcR4j5A6o1RD7pujAU9Hqqtt38k0xOTQ')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Hello':
         bot.send_message(message.chat.id, 'Hello for you too', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Your ID: { message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        bot.send_message(message.chat.id)
    else:
        bot.send_message(message.chat.id, 'I dont understand you', parse_mode='html')

bot.polling(none_stop=True)