import telebot

API_TOKEN = '7238433911:AAEJT2TbK_-1gFAr-n1DetdZLXkL23qhc8o'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)

def echo_message(message):
  bot.reply_to(message, message.text)


if __name__ == '__main__':
  print("Бот запущен и готов к работе");
  bot.polling(none_stop=True)