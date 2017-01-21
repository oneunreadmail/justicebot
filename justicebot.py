import telepot  # библиотека для работы с телеграм-ботами
from configparser import ConfigParser  # библиотека для работы с ini-файлами, прочитать токен
import time
import re  # регулярки для анализа текста

config = ConfigParser()
config.read("settings.ini")  # читаем токен из файла

bot = telepot.Bot(config['MAIN']['token'])

stoplist = [
    "лох", "пидор", "гей", "мудак", "мудило", "хуйло", "дрочер", "лошок", "лошпед", "гондон", "говноед", "чмо",
    "олень", "мразь", "остолоп", "балбес", "олух", "ушлепок", "ушлёпок", "ишак", "дебил"
]

threehundredlist = [
    "триста", "300", "зоо", "три сто", "три ста"
]


def someone_said_the_bad_words(word, string):
    return re.search(r"\b" + word + r"\b", string, re.I)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        for word in stoplist:
            if someone_said_the_bad_words(word, msg["text"]):
                bot.sendMessage(chat_id, "Сам ты " + word + ", " + msg['from']['first_name'])
                break
        for word in threehundredlist:
            if someone_said_the_bad_words(word, msg["text"]):
                bot.sendMessage(chat_id, "Отсоси у тракториста, " + msg['from']['first_name'])
                break
        for word in ["нет"]:
            if someone_said_the_bad_words(word, msg["text"]):
                bot.sendMessage(chat_id, "Пидора ответ, " + msg['from']['first_name'])
                break

bot.message_loop(handle)
while 1:
    time.sleep(10)
