import telebot

API_TOKEN = '7233898302:AAEU31uXz2IKvzDsdi_yl1yTvNV-dhtWSNg'

bot = telebot.TeleBot(API_TOKEN)

#Обработчик для сообщений с текстом "привет"
@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def greet(message):
  bot.reply_to(message, "Привет, товарищ!")

#Обработчик для сообщений с текстом "как дела"
@bot.message_handler(func=lambda message: message.text.lower() == "как дела")
def ask_how_are_you(message):
  bot.reply_to(message, "Отлично, товарищ полковник!")

#Запуск бота
if __name__ == "__main__":
  print("Бот запущен.")
  bot.polling(none_stop=True)