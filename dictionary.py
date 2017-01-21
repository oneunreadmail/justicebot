"""
Regular expressions available, bot will add \b to the left and right of your string and search like this.
%u for first name, %i (i=0..9) for inserting custom response taken from lines[x][i]
"""

dictionary = [{"lines": [
                    ["пидор", "пидора", "пидор[а-яА-Я0-9]{0,4}"],
                    ["полупидор", "полупидора", "полупидор[а-яА-Я0-9]{0,4}"],
                    ["лох", "лоха", "лох[а-яА-Я0-9]{0,2}"],
                    ["лошок", "лошка", "лошк[а-яА-Я0-9]{0,2}", "лошок?"],
                    ["хуй", "хуя", "хуе?", "хуя[а-яА-Я0-9]{0,2}", "хую", "хуи", "хуя?"]],
      "responses": [
                    "От %1 слышу, %u",
                    "Сам ты, %u, %0",
                    "Кто так обзывается, тот сам так называется, %u",
                    "Твоя мамка %0, %u"]},
     {"lines": [
                    ["300", "триста", "зоо", "три стакана", "три столовых"]],
      "responses":  ["Отсоси у тракториста, %u"]},
     {"lines": [
                    ["нет"]],
      "responses": [
                    "Пидора ответ, %u"]}
]
