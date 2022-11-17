import sqlite3 as sql
import telebot
import random
from telebot import types
from string import ascii_lowercase
import datetime as dt
from dateutil.parser import parse
import dateutil
import pytz
import datetime 

def get_noun(n):
    n = n % 100
    if (n>=5 and n<=20) or n % 5 == 0:
        return "дней"
    elif n % 10 == 1:
        return 'день'
    else: return 'дня'

TOKEN = "5730824028:AAGDJ0lRfU1MeXdrjaBjgcBO6FByWV9SU2A"
bot = telebot.TeleBot(TOKEN)
words = ["merry", "rudolf", "present", "holiday", "reindeer", "sleigh", "candle", "snowman", "chimney", "candy", "cookie", "fireplace", "frosty", "gingerbread", "mittens", "sweater", "snowball", "snowflake", "wintertime", "spirit"]

@bot.message_handler(commands=['launch'])
def launch(message):
    bot.send_message(message.chat.id,"Начинаю подготовку к Новому году!")
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEGc-5jdhfUX1UJGTinRAJVY0Z2czmeygACPRUAAro9YUjnYCB1k-Fj-isE")
    bot.set_chat_title(message.chat.id, "x-mas chat🎆")
    file = open("chat_photo.jpg", 'rb')
    bot.set_chat_photo(message.chat.id,file ) 
    
@bot.message_handler(commands=['ban'])
def ban_user(message):
    bot.send_message(message.chat.id,"В этом году без счастливого рождества")
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEGc7Bjdf_QTHecy_jPPJ9MQLU3AaZSkQACGAIAAoaH-QNooEIj5wZ_MCsE")
    bot.ban_chat_member(message.chat.id, message.from_user.id)
    
@bot.message_handler(commands=['unban'])
def unban_user(message):
    bot.unban_chat_member(message.chat.id, message.from_user.id)
    bot.send_message(message.chat.id,"С возвращением!")
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEGdB1jditBvHCwaiePNsHWd7OFL14mewACIwIAAoaH-QPIoUQz2Si7cisE")
    
@bot.message_handler(commands=['count_admins'])
def count_members(message):
    members_cnt = len(bot.get_chat_administrators(message.chat.id))
    bot.send_message(message.chat.id, str(members_cnt) + " администраторы")
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEGc6xjdf6czvOK1PGG6jKn56ne5GWfoQACEQIAAoaH-QPjllXaLNA_zisE")
    
@bot.message_handler(commands=['count_members'])
def count_members(message):
    members_cnt = bot.get_chat_member_count(message.chat.id)
    bot.send_message(message.chat.id, "Нас уже " + str(members_cnt)+"!")
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEGc6hjdf3yDuYgiVZQZMqcHY6o8SfsSAACHQIAAoaH-QOAjcukDzkn3isE")
    
@bot.message_handler(commands=['promote_me'])
def promote_member(message):
    bot.promote_chat_member(message.chat.id, message.from_user.id, can_manage_chat=True)
    
@bot.message_handler(commands=['kick_yourself'])
def leave_chat(message):
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEGc65jdf944_fmeGv6QP5jqO38Z3wcLwACDwIAAoaH-QOMp0Mi5DOZXCsE")
    bot.leave_chat(message.chat.id)

@bot.message_handler(commands=['game'])
def play_hangman(message):
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEGdBljdiniF4Rs3-wKwnyG7rcgxOQDKQACGwIAAoaH-QNkeLJVG7lZQCsE")
    bot.send_message(message.chat.id, "Давай сыграем в виселицу на английском. Все слова будут связаны с Новым годом и Рождеством!☃️ Игру пришлю тебе в лс")
    bot.send_animation(message.from_user.id,"https://avatars.dzeninfra.ru/get-zen_doc/1811900/pub_5d04806862f9700db603e7d1_5d048730778de80db6095cfe/orig")
    secret_word = words[random.randint(0, 19)] 
    secret_letters = set(secret_word)
    lives = 6
    bot.send_message(message.from_user.id, "You have "+str(lives)+" lives left")
    markup = types.InlineKeyboardMarkup()
    buttons = []
    for c in ascii_lowercase:
        buttons.append(c)    
    markup.row_width = 7
    for i in range(3):
        markup.add(types.InlineKeyboardButton(text=buttons[0 + i*7],callback_data = str(buttons[0 + i*7] in secret_letters)), types.InlineKeyboardButton(text=buttons[1 + i*7],callback_data = str(buttons[1 + i*7] in secret_letters)), types.InlineKeyboardButton(text=buttons[2 + i*7],callback_data = str(buttons[2 + i*7] in secret_letters)), types.InlineKeyboardButton(text=buttons[3 + i*7],callback_data = str(buttons[3 + i*7] in secret_letters)), types.InlineKeyboardButton(text=buttons[4 + i*7],callback_data = str(buttons[4 + i*7] in secret_letters)), types.InlineKeyboardButton(text=buttons[5 + i*7],callback_data = str(buttons[5 + i*7] in secret_letters)), types.InlineKeyboardButton(text=buttons[6 + i*7],callback_data = str(buttons[6 + i*7] in secret_letters))) 
    markup.add(types.InlineKeyboardButton(text=buttons[21],callback_data = str(buttons[21] in secret_letters)), types.InlineKeyboardButton(text=buttons[22],callback_data = str(buttons[22] in secret_letters)), types.InlineKeyboardButton(text=buttons[23],callback_data = str(buttons[23] in secret_letters)), types.InlineKeyboardButton(text=buttons[24],callback_data = str(buttons[24] in secret_letters)), types.InlineKeyboardButton(text=buttons[25],callback_data = str(buttons[25] in secret_letters))) 
    bot.send_message(message.from_user.id,"*-* "*len(secret_word) +" ("+ str(len(secret_word))+")", parse_mode = 'Markdown', reply_markup = markup)
    bot.send_message(message.from_user.id,secret_word)
    
    
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "True":
        #bot.answer_callback_query(call.id,call.message)
        #bot.send_message(call.from_user.id, call.message.text)
        bot.send_message(call.from_user.id, call.inline_message_id)
    elif call.data == "False":
        bot.answer_callback_query(call.id, "Answer is No")


@bot.message_handler(commands=['days_till_ny'])
def count_days(message):
    date = dt.datetime.now()
    new_year = dt.datetime(2023, 1, 1, 0, 0, 0)
    diff = (new_year - date).days
    bot.send_message(message.chat.id, "До Нового года осталось " + str(diff)+ " "+ get_noun(diff))
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEGc91jdhC8_hiRWUZui-XhAv6Rqn3vVQACFwIAAoaH-QNP7Ea9Fb5BVysE")  
    
bot.polling(none_stop=True, interval=0)   
