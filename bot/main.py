from ast import Call
from telegram import *
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler
from config import API_KEY
# from btns import *
# from vars import *

# https://docs.python-telegram-bot.org/en/stable/telegram.ext.filters.html#telegram.ext.filters.Filters

updater = Updater(API_KEY, use_context=True)


def start(update: Update, context: CallbackContext):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Прывітанне! Я твой музычны бро :) Што паслухаем? Калі не ведаеш, з чаго пачаць — абяры /help",
                         reply_markup=main_menu_keyboard())

# def main_menu(bot, update):
#   bot.callback_query.message.edit_text(main_menu_message(),
#                           reply_markup=main_menu_keyboard())

def main_menu(update: Update, context: CallbackContext):
  genre = update.callback_query.data
  print(genre)
  update.callback_query.message.edit_text(main_menu_message(),
                          reply_markup=main_menu_keyboard())


def first_menu(bot, update):
  bot.callback_query.message.edit_text(first_menu_message(),
                          reply_markup=first_menu_keyboard())


def error(update, context):
    print(f'Update {update} caused error {context.error}')

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Здзіві мяне!', callback_data='Здзіві мяне')],
              [InlineKeyboardButton('Фолк', callback_data='Фолк')],
              [InlineKeyboardButton('Поп', callback_data='Поп')],
              [InlineKeyboardButton('Метал', callback_data='Метал')],
              [InlineKeyboardButton('Індзі рок', callback_data='Індзі рок')],
              [InlineKeyboardButton('Рэп', callback_data='Рэп')],
              [InlineKeyboardButton('Электроніка', callback_data='Электроніка')],
              ]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Імпрэза', callback_data='m1_1')],
              [InlineKeyboardButton('Спорт', callback_data='m1_2')],
              [InlineKeyboardButton('Рамантыка', callback_data='m1_2')],
              [InlineKeyboardButton('Разбітае сэрцайка', callback_data='m1_2')],
              [InlineKeyboardButton('Медытацыя', callback_data='m1_2')],
              [InlineKeyboardButton('Чыл', callback_data='m1_2')],
              [InlineKeyboardButton('У дарозе', callback_data='m1_2')],
              [InlineKeyboardButton('Самота', callback_data='m1_2')],
              [InlineKeyboardButton('Надзея', callback_data='m1_2')],
              [InlineKeyboardButton('Праца\вучоба', callback_data='m1_2')],
              [InlineKeyboardButton('Іншы', callback_data='m1_2')],
              [InlineKeyboardButton('Назад', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)



############################# Helpers #########################################


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Абяры каманду:
    /info — Агульная інфармацыя пра бота
    """)

def info(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Мы зрабілі гэты бот, каб ты мог/магла атрымліваць асалоду ад крутой беларускай музыкі ў любой кропцы свету. Распавядзі нам пра свой настрой і свае ўлюбёныя жанры і пачнем! Скарыстайся з кнопак, каб абраць жанр:",
                             reply_markup=main_menu_keyboard())





############################# Messages #########################################
def main_menu_message():
  return 'Абяры стыль музыкі, якую хочаш паслухаць:'

def first_menu_message():
  return 'Абяры настрой, які адпавядае сітуацыі, а мы паклапоцімся пра музыку:'



############################# Handlers #########################################
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_error_handler(error)

updater.start_polling()