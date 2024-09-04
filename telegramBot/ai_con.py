from openai import OpenAI

client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

def chat_with_model():
    messages = []

    while True:
        user_input = input("Вы: ")

        if user_input.lower() in ["exit", "quit", "выход"]:
            print("Чат завершен.")
            break

        # Добавляем сообщение пользователя в историю
        messages.append({"role": "user", "content": user_input})

        # Получаем ответ от модели
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106", messages=messages
        )

        # Извлекаем ответ модели
        assistant_message = chat_completion.choices[0].message.content
        print("Бот:", assistant_message)

        # Добавляем ответ модели в историю
        messages.append({"role": "assistant", "content": assistant_message})

if __name__ == "__main__":
    chat_with_model()