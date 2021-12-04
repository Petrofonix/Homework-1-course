from requests import get, utils


def currency_rates(valute):
    response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))
    content = response.split('<Valute ID=')

    for i in content:
        if valute in i:
            print(f'Валюта: {valute}')
            value = float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))
            print(f'Валюта: {value}')
        if valute not in response:
            print(None)
            break


currency_rates(str(input('Введите валюту (Например USD или EUR): ')))
