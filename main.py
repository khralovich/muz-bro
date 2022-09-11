from ast import Call
from telegram import *
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from config import API_KEY

# https://docs.python-telegram-bot.org/en/stable/telegram.ext.filters.html#telegram.ext.filters.Filters

updater = Updater(API_KEY, use_context=True)

genre = None
mood = None


# HTML szablon

all_genres = ['Здзіві мяне!', "Фолк", 'Поп', 'Метал', 'Індзі', 'Рэп', 'Рок', 'Электроніка', 'Skip genre']
all_moods = ['Імпрэза', 'Спорт', 'Рамантыка', 'Разбітае сэрцайка', 'Медытацыя','Чыл','У дарозе','Самота','Надзея','Праца\вучоба','Skip mood']

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Прывітанне! Я твой музычны бро :) Што паслухаем? Калі не ведаеш, з чаго пачаць — абяры /help",
                             reply_markup=main_menu_keyboard())



def main_menu(update: Update, context: CallbackContext):
    reply = update.callback_query.data
    if reply in all_genres:
        genre = reply
        context.bot.send_message(chat_id=update.effective_chat.id, text=first_menu_message(), reply_markup=first_menu_keyboard())
        print(genre)
    if reply in all_moods:
        mood = reply
        update.callback_query.answer()
        print(mood)
        context.bot.send_message(chat_id=update.effective_chat.id, text="<u>Тут будзе ХТМЛ</u>", parse_mode="HTML" ,reply_markup=like_buttons())




def error(update, context):
    print(f'Update {update} caused error {context.error}')


############################ Keyboards #########################################
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Здзіві мяне!', callback_data='Здзіві мяне!')],
                [InlineKeyboardButton('Фолк', callback_data='Фолк')],
                [InlineKeyboardButton('Поп', callback_data='Поп')],
                [InlineKeyboardButton('Метал', callback_data='Метал')],
                [InlineKeyboardButton('Індзі', callback_data='Індзі')],
                [InlineKeyboardButton('Рэп', callback_data='Рэп')],
                [InlineKeyboardButton('Рок', callback_data='Рок')],
                [InlineKeyboardButton('Электроніка', callback_data='Электроніка')],
                [InlineKeyboardButton('Прапусціць', callback_data="Skip genre")]
                ]
    return InlineKeyboardMarkup(keyboard)

def like_buttons():
    keyboard = [[InlineKeyboardButton("Хачу яшчэ", callback_data="more")],
                [InlineKeyboardButton("Назад да жанраў", callback_data="back")]
                ]

    return InlineKeyboardMarkup(keyboard)



def first_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Імпрэза', callback_data='Імпрэза')],
                [InlineKeyboardButton('Спорт', callback_data='Спорт')],
                [InlineKeyboardButton('Рамантыка', callback_data='Рамантыка')],
                [InlineKeyboardButton('Разбітае сэрцайка', callback_data='Разбітае сэрцайка')],
                [InlineKeyboardButton('Медытацыя', callback_data='Медытацыя')],
                [InlineKeyboardButton('Чыл', callback_data='Чыл')],
                [InlineKeyboardButton('У дарозе', callback_data='У дарозе')],
                [InlineKeyboardButton('Самота', callback_data='Самота')],
                [InlineKeyboardButton('Надзея', callback_data='Надзея')],
                [InlineKeyboardButton('Праца\вучоба', callback_data='Праца\вучоба')],
                [InlineKeyboardButton('Прапусціць', callback_data='Skip')],
                [InlineKeyboardButton('Назад', callback_data="Skip mood")]
    ]
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
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_error_handler(error)
updater.start_polling()
