import requests

KEY = 'trnsl.1.1.20170731T054820Z.fbbb0d84ece850a3.d12ca7d859f5ac90668fad7f134f33904292744e'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
def translate_me(mytext) :
    '''
    https: // translate.yandex.net / api / v1.5 / tr.json / translate ?
    key = < API - ключ >
    & text = < переводимый текст >
    & lang = < направление перевода >
    & [format = < формат текста >]
    & [options = < опции перевода >]
    & [callback = < имя callback - функции >]

    :param text: <str> text for translation.
    :return: <str> translated text.
    '''

    params = {
        "key" : KEY,
        "text" : mytext,
        "lang" : "en-ru",
    }

    response = requests.get(URL, params=params)
    return response.json()

json = translate_me('cheers!')
print(' '.join(json['text']))