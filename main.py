import jinja2
from ast import Call
from telegram import *
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from src.connection.rds import read_songs
from src.platforms_integration.song_link import SELECTED_PLATFORMS
from config import API_KEY


# https://docs.python-telegram-bot.org/en/stable/telegram.ext.filters.html#telegram.ext.filters.Filters

updater = Updater(API_KEY, use_context=True)

user_reply = None
shown_songs = 0

# HTML template
HTML_TEMPLATE = jinja2.Template(
    """
    1) {{artist_1}} - {{title_1}} {% for platform in platforms_1 -%} <a href="{{platform.url}}">{{platform.name}}</a>  {% endfor %}
    2) {{artist_2}} - {{title_2}} {% for platform in platforms_2 -%} <a href="{{platform.url}}">{{platform.name}}</a>  {% endfor %}
    3) {{artist_3}} - {{title_3}} {% for platform in platforms_3 -%} <a href="{{platform.url}}">{{platform.name}}</a>  {% endfor %}
    4) {{artist_4}} - {{title_4}} {% for platform in platforms_4 -%} <a href="{{platform.url}}">{{platform.name}}</a>  {% endfor %}
    5) {{artist_5}} - {{title_5}} {% for platform in platforms_5 -%} <a href="{{platform.url}}">{{platform.name}}</a>  {% endfor %}
    """
)

all_genres = ['Здзіві мяне!', "Фолк", 'Поп', 'Метал', 'Індзі', 'Рэп', 'Рок', 'Электроніка', 'Skip genre']
all_moods = ['Імпрэза', 'Спорт', 'Рамантыка', 'Разбітае сэрцайка', 'Медытацыя','Чыл','У дарозе','Самота','Надзея','Праца\вучоба','Skip mood']
goback = ["Назад"]

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Прывітанне! Я твой музычны бро :) Што паслухаем? Калі не ведаеш, з чаго пачаць — абяры /help",
                             reply_markup=main_menu_keyboard())


def main_menu(update: Update, context: CallbackContext):
    reply = update.callback_query.data
    if reply in all_genres:
        # User selected the genre
        genre = reply
        context.bot.send_message(chat_id=update.effective_chat.id, text=first_menu_message(), reply_markup=first_menu_keyboard())
        print(genre)
    if reply in all_moods or reply == 'more':
        if reply == 'more':
            print("Больш песен")
        else:
            mood = reply
            update.callback_query.answer()
            print(mood)
            songs_df = read_songs(genre="test", mood=None)
            songs = songs_df.to_dict('records')
            n_songs = len(songs)
        n_songs_left = n_songs - shown_songs
        if n_songs_left >= 5:
            html_render = HTML_TEMPLATE.render(
                artist_1=songs[shown_songs+0]['artist'], title_1=songs[shown_songs+0]['title'],
                artist_2=songs[shown_songs+1]['artist'], title_2=songs[shown_songs+1]['title'],
                artist_3=songs[shown_songs+2]['artist'], title_3=songs[shown_songs+2]['title'],
                artist_4=songs[shown_songs+3]['artist'], title_4=songs[shown_songs+3]['title'],
                artist_5=songs[shown_songs+4]['artist'], title_5=songs[shown_songs+4]['title'],
                platforms_1=[{"name": name, "url": url} for name, url in songs[shown_songs+0].items() if name in SELECTED_PLATFORMS],
                platforms_2=[{"name": name, "url": url} for name, url in songs[shown_songs+1].items() if name in SELECTED_PLATFORMS],
                platforms_3=[{"name": name, "url": url} for name, url in songs[shown_songs+2].items() if name in SELECTED_PLATFORMS],
                platforms_4=[{"name": name, "url": url} for name, url in songs[shown_songs+3].items() if name in SELECTED_PLATFORMS],
                platforms_5=[{"name": name, "url": url} for name, url in songs[shown_songs+4].items() if name in SELECTED_PLATFORMS],
            )
            context.bot.send_message(chat_id=update.effective_chat.id, text=html_render, parse_mode="HTML" ,reply_markup=like_buttons())
            shown_songs += 5
    if reply in goback:
        print(reply)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Давай пачнем з выбару жанру. Абяры які-небудзь з наступных:",
                                 reply_markup=main_menu_keyboard())


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
                [InlineKeyboardButton("Назад да жанраў", callback_data="Назад")]
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
                [InlineKeyboardButton('Прапусціць', callback_data='Skip mood')],
                [InlineKeyboardButton('Назад', callback_data="Назад")]
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
