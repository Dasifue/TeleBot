from settings import BOT_TOKEN
from settings import URL

from house.parser import main
from house.categories import CATEGORIES, CATEGORIES_ADVANCED

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
        text = f"Hello, {username}! Here you can find new posts form house.kg"
    else:
        text = "Hello, User! Here you can find new posts form house.kg"   

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    menu = InlineKeyboardButton("Menu", callback_data="menu")
    contacts = InlineKeyboardButton("Mail", url="dasifue@gmail.com")
    markup.add(menu)
    markup.add(contacts)
    bot.send_message(message.chat.id, text, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == "menu")
def menu_callback(call):
    message = call.message
    text = "Choose option"
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    back = InlineKeyboardButton("Back to menu", callback_data="back_to_menu")
    markup.add(back)

    for category_list in (CATEGORIES_ADVANCED.keys(), CATEGORIES.keys(),):
        for category in category_list:
            button = InlineKeyboardButton(category, callback_data=category)
            markup.add(button)

    bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=message.message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data in CATEGORIES.keys())
def categories_callback(call):

    message = call.message

    for estate in main(category=CATEGORIES.get(call.data)):
        url = URL + estate.get("url")
        title = estate.get("title")
        address = estate.get("address")
        description = estate.get("description")
        price_dollar = estate.get("price_dollar")
        price_som = estate.get("price_som")
        
        text = f"""
        title: {title};
        address: {address};
        description: {description};
        price in dollars: {price_dollar};
        price in soms: {price_som};
        link: {url}
        """
            
        apartment_markup = InlineKeyboardMarkup()
        apartment_markup.row_width = 1
        button = InlineKeyboardButton(text="Visit site", url=url)
        apartment_markup.add(button)
    
        bot.send_message(message.chat.id, text, reply_markup=apartment_markup)

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    back = InlineKeyboardButton("Back to categories", callback_data="back_to_categories")
    markup.add(back)

    bot.send_message(message.chat.id, "Nothink intresting?", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data in CATEGORIES_ADVANCED.keys())
def categories_advanced_callback(call):
    message = call.message
    text = "Choose option"
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    back = InlineKeyboardButton("Back to categories", callback_data="back_to_categories")
    markup.add(back)

    for room_category in CATEGORIES_ADVANCED.get(call.data).keys():
        button = InlineKeyboardButton(room_category, callback_data=room_category)
        markup.add(button)
    
    bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=message.message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data in CATEGORIES_ADVANCED.get("apartments").keys())
def apartments_callback(call):
    message = call.message

    for apartment in main(room_quantity=call.data, category=CATEGORIES_ADVANCED.get("apartments")):
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
            link: {url}
            """
        else:
            text = f"""
            title: {title};
            address: {address};
            description: {description};
            price in dollars: {price_dollar};
            price in soms: {price_som};
            link: {url}
            """
            
        apartment_markup = InlineKeyboardMarkup()
        apartment_markup.row_width = 1
        button = InlineKeyboardButton(text="Visit site", url=url)
        apartment_markup.add(button)
    
        bot.send_message(message.chat.id, text, reply_markup=apartment_markup)

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    back = InlineKeyboardButton("Back to categoties", callback_data="back_to_categories")
    markup.add(back)

    bot.send_message(message.chat.id, "Nothink intresting?", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data in CATEGORIES_ADVANCED.get("houses").keys())
def houses_callback(call):

    message = call.message

    for house in main(room_quantity=call.data, category=CATEGORIES.get("houses")):
        url = URL + house.get("url")
        title = house.get("title")
        address = house.get("address")
        description = house.get("description")
        price_dollar = house.get("price_dollar")
        price_som = house.get("price_som")
        
        text = f"""
        title: {title};
        address: {address};
        description: {description};
        price in dollars: {price_dollar};
        price in soms: {price_som};
        link: {url}
        """
            
        apartment_markup = InlineKeyboardMarkup()
        apartment_markup.row_width = 1
        button = InlineKeyboardButton(text="Visit site", url=url)
        apartment_markup.add(button)
    
        bot.send_message(message.chat.id, text, reply_markup=apartment_markup)

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    back = InlineKeyboardButton("Back to categories", callback_data="back_to_categories")
    markup.add(back)

    bot.send_message(message.chat.id, "Nothink intresting?", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data in CATEGORIES_ADVANCED.get("country house").keys())
def houses_callback(call):

    message = call.message

    for house in main(room_quantity=call.data, category=CATEGORIES.get("country house")):
        url = URL + house.get("url")
        title = house.get("title")
        address = house.get("address")
        description = house.get("description")
        price_dollar = house.get("price_dollar")
        price_som = house.get("price_som")
        
        text = f"""
        title: {title};
        address: {address};
        description: {description};
        price in dollars: {price_dollar};
        price in soms: {price_som};
        link: {url}
        """
            
        apartment_markup = InlineKeyboardMarkup()
        apartment_markup.row_width = 1
        button = InlineKeyboardButton(text="Visit site", url=url)
        apartment_markup.add(button)
    
        bot.send_message(message.chat.id, text, reply_markup=apartment_markup)

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    back = InlineKeyboardButton("Back to categories", callback_data="back_to_categories")
    markup.add(back)

    bot.send_message(message.chat.id, "Nothink intresting?", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data.startswith("back_to_"))
def back_to__callback(call):
    message = call.message

    if call.data.endswith("menu"):
        send_welcome_message(message)
    elif call.data.endswith("categories"):
        menu_callback(call)



bot.infinity_polling()