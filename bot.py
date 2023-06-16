import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Замените <YOUR_BOT_TOKEN> на фактический токен вашего бота
bot = telebot.TeleBot("6128190847:AAF5ypTpAEIJ20q_CsMfjwjyLMz8NXV6nkI")

# Список ссылок на тесты для каждой группы респондентов
links_group1 = ["https://example.com/test1"]
links_group2 = ["https://example.com/test3"]

@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем клавиатуру с кнопкой "Пройти тест"
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Пройти тест", callback_data='start_test'))
    
    # Отправляем приветственное сообщение с кнопкой
    bot.reply_to(message, "Привет! Хочешь пройти тест?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'start_test')
def handle_start_test(callback_query):
    # Определяем группу, к которой принадлежит респондент
    user_id = callback_query.from_user.id
    group_number = user_id % 2  # Простое распределение по остатку от деления
    
    # Получаем случайную ссылку на тест из соответствующей группы
    if group_number == 0:
        test_link = random.choice(links_group1)
    else:
        test_link = random.choice(links_group2)
    
    # Отправляем респонденту ссылку на тест
    bot.send_message(user_id, f"Вот ссылка для прохождения теста: {test_link}")
    bot.send_message(user_id, "Пожалуйста, пройдите тест по ссылке.")
    
@bot.callback_query_handler(func=lambda call: call.data == 'test_completed')
def handle_test_completed(callback_query):
    user_id = callback_query.from_user.id
    bot.send_message(user_id, "Спасибо, что прошли тест! Ваш результат был успешно записан.")
    
    # Отправляем уведомление администратору
    admin_id = <ADMIN_USER_ID>  # Замените <ADMIN_USER_ID> на фактический ID администратора
    bot.send_message(admin_id, f"Респондент с ID {user_id} успешно прошел тест.")

# Запускаем бота
bot.polling()
