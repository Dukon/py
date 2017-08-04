#!/usr/bin/env python
# -*- coding: utf-8 -*-

import osa
#import suds

#import client

url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'

client1 = osa.client.Client(url)
print(client1.types)

response1 = client1.service.ConvertTemp(Temperature=15.00, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')

print(response1)

client2 = osa.client.Client(url)

response2 = client2.service.ConvertTemp(Temperature=15.00, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')

print(response2)

url2 ='https://fx.currencysystem.com/webservices/currencyserver4.asmx?wsdl'

client3 = osa.client.Client(url2)
response3 = client3.service.Currencies()
print(response3.split(' , '))

response4 = client3.service.ConvertToNum(fromCurrency='EUR', toCurrency='RUB',amount=10.00, rounding=False)
print(response4)


test = [(120.00, 'USD'), (23.00, 'EUR')]
def count_exp(sums):
    url3 = 'https://fx.currencysystem.com/webservices/currencyserver4.asmx?wsdl'
    client = osa.client.Client(url3)
    resp = 0
    for amount, currency in sums:
        resp += client.service.ConvertToNum(fromCurrency=currency, toCurrency='RUB',amount=amount, rounding=True)
    return resp


print(count_exp(test))

#response5 = client3.service.ConvertToStr(fromCurrency='EUR', toCurrency='RUB',amount=20.00, rounding=False)
#print(response5)

