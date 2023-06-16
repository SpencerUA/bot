import telebot
from telebot import types

# Токен вашего бота, полученный от BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# Создание экземпляра бота
bot = telebot.TeleBot(6128190847:AAF5ypTpAEIJ20q_CsMfjwjyLMz8NXV6nkI)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем клавиатуру с кнопкой
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton(text="Получить ссылку на тест")
    keyboard.add(button)

    # Отправляем приветственное сообщение с клавиатурой
    bot.send_message(message.chat.id, "Привет! Хочешь пройти тест?", reply_markup=keyboard)

# Обработчик нажатия кнопки "Получить ссылку на тест"
@bot.message_handler(func=lambda message: message.text == "Получить ссылку на тест")
def handle_test_link(message):
    # Определяем группу пользователя
    group = determine_user_group(message.from_user.id)

    # Отправляем ссылку на тест в зависимости от группы
    if group == 1:
        bot.send_message(message.chat.id, "Вот ссылка на тест для группы 1: <ссылка_для_группы_1>")
    elif group == 2:
        bot.send_message(message.chat.id, "Вот ссылка на тест для группы 2: <ссылка_для_группы_2>")

# Обработчик нажатия кнопки "Я прошел тест"
@bot.message_handler(func=lambda message: message.text == "Я прошел тест")
def handle_test_completed(message):
# Запрос ID пользователя
bot.send_message(message.chat.id, "Пожалуйста, введите ваш ID, указанный на сайте:")

# Обработчик ввода ID пользователя
@bot.message_handler(func=lambda message: True) # Любое сообщение будет обрабатываться
def handle_user_id(message):
# Получаем ID пользователя и производим начисление награды
user_id = message.text
reward = calculate_reward(user_id)
# Отправляем сообщение с информацией о начисленной награде
bot.send_message(message.chat.id, f"Вам начислена награда: {reward}.")
Функция для определения группы пользователя (здесь просто пример, вы можете заменить ее на вашу логику)
def determine_user_group(user_id):
# Здесь вы можете реализовать логику определения группы пользователя
# Возвращаем 1 или 2 в зависимости от группы пользователя
return 1 if user_id % 2 == 0 else 2

# Функция для расчета награды пользователя (здесь просто пример, вы можете заменить ее на вашу логику)
def calculate_reward(user_id):
# Здесь вы можете реализовать логику расчета награды для пользователя
# Возвращаем сумму награды в зависимости от ID пользователя
return user_id * 10

# Запуск бота
bot.polling()
import telebot
from telebot import types

# Токен вашего бота, полученный от BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения данных о пользователях
users_data = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем клавиатуру с кнопкой
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button = types.KeyboardButton(text="Получить ссылку на тест")
    keyboard.add(button)

    # Отправляем приветственное сообщение с клавиатурой
    bot.send_message(message.chat.id, "Привет! Хочешь пройти тест?", reply_markup=keyboard)

# Обработчик нажатия кнопки "Получить ссылку на тест"
@bot.message_handler(func=lambda message: message.text == "Получить ссылку на тест")
def handle_test_link(message):
    # Определяем группу пользователя
    group = determine_user_group(message.from_user.id)

    # Отправляем ссылку на тест в зависимости от группы
    if group == 1:
        test_link = "ссылка_для_группы_1"
    elif group == 2:
        test_link = "ссылка_для_группы_2"

    # Сохраняем данные о пользователе
    users_data[message.from_user.id] = {
        "group": group,
        "test_link": test_link,
        "completed_test": False
    }

    # Отправляем ссылку на тест
    bot.send_message(message.chat.id, f"Вот ссылка на тест: {test_link}")

# Обработчик нажатия кнопки "Я прошел тест"
@bot.message_handler(func=lambda message: message.text == "Я прошел тест")
def handle_test_completed(message):
    user_id = message.from_user.id

    # Проверяем, что пользователь прошел тест
    if user_id in users_data and not users_data[user_id]["completed_test"]:
        # Обновляем статус прохождения теста
        users_data[user_id]["completed_test"] = True

        # Запрос ID пользователя
        bot.send_message(message.chat.id, "Пожалуйста, введите ваш ID, указанный на сайте:")
    else:
        # Если пользователь уже прошел тест, отправляем сообщение об ошибке
        bot.send_message(message.chat.id, "Вы уже прошли тест!")

# Обработчик ввода ID пользователя
@bot.message_handler(func=lambda message: True)  # Любое сообщение будет обрабатываться
def handle_user_id(message):
    user_id = message.from_user.id

    # Проверяем, что пользователь прошел тест и в
@bot.message_handler(func=lambda message: True) # Любое сообщение будет обрабатываться
def handle_user_id(message):
user_id = message.from_user.id
# Проверяем, что пользователь прошел тест и ввел свой ID
if user_id in users_data and users_data[user_id]["completed_test"]:
    # Получаем введенный пользователем ID
    entered_id = message.text

    # Выполняем начисление награды
    reward = calculate_reward(entered_id)

    # Удаляем данные о пользователе
    del users_data[user_id]

    # Отправляем сообщение с информацией о начисленной награде
    bot.send_message(message.chat.id, f"Вам начислена награда: {reward}.")
else:
    # Если пользователь не прошел тест или не ввел ID, отправляем сообщение об ошибке
    bot.send_message(message.chat.id, "Вы не прошли тест или не ввели свой ID.")
Функция для определения группы пользователя (здесь просто пример, вы можете заменить ее на вашу логику)
def determine_user_group(user_id):
# Здесь вы можете реализовать логику определения группы пользователя
# Возвращаем 1 или 2 в зависимости от группы пользователя
return 1 if user_id % 2 == 0 else 2

Функция для расчета награды пользователя (здесь просто пример, вы можете заменить ее на вашу логику)
def calculate_reward(user_id):
# Здесь вы можете реализовать логику расчета награды для пользователя
# Возвращаем сумму награды в зависимости от ID пользователя
return user_id * 10

Запуск бота
bot.polling()
