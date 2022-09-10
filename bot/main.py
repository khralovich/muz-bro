from telegram import *
from telegram.ext import *
from config import API_KEY
from btns import *
from vars import *

# https://docs.python-telegram-bot.org/en/stable/telegram.ext.filters.html#telegram.ext.filters.Filters

updater = Updater(API_KEY, use_context=True)


def start(update: Update, context: CallbackContext):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Прывітанне! Я твой музычны бро :) Што паслухаем? Калі не ведаеш, з чаго пачаць — абяры /help",
                         reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  bot.callback_query.message.edit_text(main_menu_message(),
                          reply_markup=main_menu_keyboard())

def first_menu(bot, update):
  bot.callback_query.message.edit_text(first_menu_message(),
                          reply_markup=first_menu_keyboard())

def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

def error(update, context):
    print(f'Update {update} caused error {context.error}')

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Здзіві мяне!', callback_data='m1')],
              [InlineKeyboardButton('Фолк', callback_data='m2')],
              [InlineKeyboardButton('Поп', callback_data='m3')],
              [InlineKeyboardButton('Метал', callback_data='m3')],
              [InlineKeyboardButton('Індзі рок', callback_data='m3')],
              [InlineKeyboardButton('Рэп', callback_data='m3')],
              [InlineKeyboardButton('Электроніка', callback_data='m3')],
              ]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Рамантычны', callback_data='m1_1')],
              [InlineKeyboardButton('Вясёлы', callback_data='m1_2')],
              [InlineKeyboardButton('Задуменны', callback_data='m1_2')],
              [InlineKeyboardButton('Меланхалічны', callback_data='m1_2')],
              [InlineKeyboardButton('Ідылічны', callback_data='m1_2')],
              [InlineKeyboardButton('Гуллівы', callback_data='m1_2')],
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
  return 'Абяры свой настрой:'



############################# Handlers #########################################
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_error_handler(error)

updater.start_polling()