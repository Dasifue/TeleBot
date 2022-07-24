from settings import BOT_TOKEN
from settings import URL


from apartments import main
from apartments import apartment_categories

import telebot

from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    username = message.__dict__.get("chat").__dict__.get("username")

    if username:
        text = f"Hello, {username}!"
    else:
        text = "Hello, User!"   

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    menu = InlineKeyboardButton("Menu", callback_data="menu")
    contacts = InlineKeyboardButton("Me", callback_data="me")
    markup.add(menu)
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "menu")
def menu_callback(call):
    message = call.message
    text = "Choose option"
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    back = InlineKeyboardButton("Back to menu", callback_data="back_to_menu")
    markup.add(back)

    for category in apartment_categories.keys():
        button = InlineKeyboardButton(category, callback_data=category)
        markup.add(button)

    bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in apartment_categories.keys())
def apartment_categories_callback(call):
    message = call.message

    for apartment in main(call.data):
        url = URL + apartment.get("url")
        title = apartment.get("title")
        address = apartment.get("address")
        description = apartment.get("description")
        price_dollar = apartment.get("price_dollar")
        price_som = apartment.get("price_som")
        residential_complex = apartment.get("residential_complex_title")
        
        if residential_complex:
            residential_complex_title = residential_complex
            text = f"""
            title: {title};
            residential complex: {residential_complex_title};
            address: {address};
            description: {description};
            price: {price_dollar};
            price in soms: {price_som};
            """
        else:
            text = f"""
            title: {title};
            address: {address};
            description: {description};
            price in dollars: {price_dollar};
            price in soms: {price_som};
            """
            
        apartment_markup = InlineKeyboardMarkup()
        apartment_markup.row_width = 1
        button = InlineKeyboardButton(text="Visit site", url=url)
        apartment_markup.add(button)
    
        bot.send_message(message.chat.id, text, reply_markup=apartment_markup)

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    next_page = InlineKeyboardButton("Next page", callback_data="next")
    previous_page = InlineKeyboardButton("Previous page", callback_data="previous")
    back = InlineKeyboardButton("Back to room quantity", callback_data="back_to_rooms")
    markup.add(next_page)
    markup.add(previous_page)
    markup.add(back)

    bot.send_message(message.chat.id, "Nothink intresting?", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data.startswith("back_to_"))
def back_to__callback(call):
    message = call.message

    if call.data.endswith("menu"):
        send_welcome_message(message)
    elif call.data.endswith("rooms"):
        menu_callback(call)

bot.infinity_polling()