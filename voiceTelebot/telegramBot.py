import telebot

API_TOKEN = '7233898302:AAEU31uXz2IKvzDsdi_yl1yTvNV-dhtWSNg'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
  bot.send_message(message.chat.id, "Я - бот, демонстрирующий команды /start и /help.")

@bot.message_handler(commands=['help'])
def handle_help(message):
  bot.send_message(message.chat.id, "Список доступных команд: \n/start - начать работу с ботом \n/help - получить справку о командах бота\n/reverse - перевернуть текст\n/upper - перевести текст в верхний регистр\n/remove - убрать все гласные буквы\n/count - подсчитать число символов в введенном тексте")

# Обрабатываем команду /reverse

@bot.message_handler(commands=['reverse'])
def handle_reverse(message):
  primary_text = message.text[len('/reverse'):]

  reversed_text = primary_text[::-1]

  bot.send_message(message.chat.id, reversed_text)

# Обрабатываем команду /upper

@bot.message_handler(commands=['upper'])
def handle_upper(message):
  primary_text = message.text[len('/upper'):]

  upper_text = primary_text.upper()

  bot.send_message(message.chat.id, upper_text)


# Обрабатываем команду /remove

@bot.message_handler(commands=['remove'])
def handle_remove(message):
  primary_text = message.text[len('/remove'):]

  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I','O', 'U', 'а', 'е', 'и', 'о', 'ы', 'у', 'я', 'ё', 'ю','э', 'А', 'Е', 'И', 'О', 'У', 'Я', 'Ё', 'Ю', 'Ы', 'Э']

  no_vowels_text = ''.join(char for char in primary_text if char not in vowels)

  bot.send_message(message.chat.id, no_vowels_text)

# Подсчет символов в тексте

@bot.message_handler(commands=['count'])
def handle_count(message):
  initial_text = message.text[len('/count'):]
  letter_count = len(initial_text)

  bot.send_message(message.chat.id, letter_count)

bot.polling(non_stop=True)