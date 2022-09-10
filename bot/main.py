from telegram import *
from telegram.ext import *
from config import API_KEY
from btns import *

# https://docs.python-telegram-bot.org/en/stable/telegram.ext.filters.html#telegram.ext.filters.Filters

updater = Updater(API_KEY, use_context=True)
dispatcher = updater.dispatcher

def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton("Здзіві мяне!"),
                KeyboardButton("Рэп"),
                KeyboardButton("Фолк")],
               [KeyboardButton("Поп"),
                KeyboardButton("Альт рок"),
                KeyboardButton("Метал")],
               [KeyboardButton("Індзі рок"),
                KeyboardButton("Электроніка"),
                KeyboardButton("->")]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Прывітанне! Я твой музычны бро :) Што паслухаем? Калі не ведаеш, з чаго пачаць — абяры /help",
                             reply_markup=ReplyKeyboardMarkup(buttons))


def messageHandler(update: Update, context: CallbackContext):
    if "Здзіві мяне!" in update.message.text:
        text = keysOutput["Здзіві мяне!"]
    if "Рэп" in update.message.text:
        text = keysOutput["Рэп"]
    if "Электроніка" in update.message.text:
        text = keysOutput["Электроніка"]
    if text:
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Абяры каманду:
    /info — Агульная інфармацыя пра бота
    """)

def info(update: Update, context: CallbackContext):
    update.message.reply_text("Мы зрабілі гэты бот, каб ты мог/магла атрымліваць асалоду ад крутой беларускай музыкі ў любой кропцы свету. Распавядзі нам пра свой настрой і свае ўлюбёныя жанры і пачнем! Скарыстайся з кнопак, каб абраць жанр:")


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('info', info))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))


updater.start_polling()