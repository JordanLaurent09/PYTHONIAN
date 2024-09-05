import telebot
from openai import OpenAI

# Инициализация клиента OpenAI
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Инициализация бота с токеном
bot = telebot.TeleBot("7233898302:AAEU31uXz2IKvzDsdi_yl1yTvNV-dhtWSNg")

# Словарь для хранения истории сообщений для каждого пользователя
user_messages = {}

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    user_text = message.text

    # Инициализация истории сообщений для нового пользователя
    if chat_id not in user_messages:
        user_messages[chat_id] = []

    # Добавляем сообщение пользователя в историю
    user_messages[chat_id].append({"role": "user", "content": user_text})

    # Получаем ответ от модели
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106", messages=user_messages[chat_id]
    )

    # Извлекаем ответ модели
    assistant_message = chat_completion.choices[0].message.content

    # Отправляем ответ обратно пользователю
    bot.send_message(chat_id, assistant_message)

    # Добавляем ответ модели в историю
    user_messages[chat_id].append({"role": "assistant", "content": assistant_message})

# Запуск бота
bot.polling()
