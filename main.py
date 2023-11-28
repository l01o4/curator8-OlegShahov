import telebot
bot = telebot.TeleBot('6809079629:AAGb6qg4zZrd1Ph6HgXu3ehRS0QBqeT8YlQ')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуй, котик я кусок мяса. Тебе рассказать о видах мяса?', parse_mode='Markdown')
@bot.message_handler(commands=['да'])
def main(message):
    bot.send_message(message.chat.id, 'Хорошо! Говядина,баранина,свинина,птичье мясо и рыбье мясо', parse_mode='Markdown')
@bot.message_handler(commands=['нет'])
def main(message):
    bot.send_message(message.chat.id, 'Печально! Ну, тогда ешь печеньку!', parse_mode='Markdown')
bot.infinity_polling()
