import telepot  # core library to work with telegram
from configparser import ConfigParser  # ini-file parser library
import time
import re
from random import choice
from dictionary import dictionary

config = ConfigParser()
config.read("token.ini")  # reading token from file

bot = telepot.Bot(config['MAIN']['token'])


def someone_said_the_bad_words(word, string):
    return re.search(r"\b" + word + r"\b", string, re.I)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        for case in dictionary:
            for words in case["lines"]:
                for word in words:
                    if someone_said_the_bad_words(word, msg["text"]):
                        reply = choice(case["responses"])  # choosing random reply
                        reply = reply.replace("%u", msg['from']['first_name'])  # replacing %u with first name
                        for i in range(len(words)):
                            reply = reply.replace("%"+str(i+1), words[i])  # replacing %i with custom word form
                        bot.sendMessage(chat_id, reply)
                        break

bot.message_loop(handle)
while 1:
    time.sleep(10)
