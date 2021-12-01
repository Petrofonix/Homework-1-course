from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=False):
    jokes_list = []
    for i in range (0, n):
        if len(nouns) == 0:
            break
        nouns_enter = choice(nouns)
        adverbs_enter = choice(adverbs)
        adjectives_enter = choice(adjectives)
        jokes_list.append(f'{nouns_enter} {adverbs_enter} {adjectives_enter}')
        if repeat:
            nouns.remove(nouns_enter)
            adverbs.remove(adverbs_enter)
            adjectives.remove(adjectives_enter)
    return jokes_list


print (get_jokes(int(input('Введите колличество шуток: ')), True))
