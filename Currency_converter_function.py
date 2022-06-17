import sys

from Exchange_Rate_and_Balance import get_currency_dollar_uah, get_currency_uah_dollar, get_balance, save_balance


def rate_output(currency):
    balance = get_balance()

    if currency == 'USD':
        currency = f'1 USD to UAH: {get_currency_dollar_uah()}, USD BALANCE is {balance["usd"]}'
        return currency
    elif currency == 'UAH':
        currency = f'1 UAH to USD: {get_currency_uah_dollar()}, UAH BALANCE is {balance["uah"]}'
        return currency
    else:
        print(f'Sorry, we do not exchange this {currency}.\nBye', )
        return sys.exit()


def exchange_currency_usd_uah():
    balance = get_balance()
    currency = get_currency_dollar_uah()

    sell_dollars = int(input('How many dollars do you want to sell? '))
    trade = sell_dollars * currency
    if trade < balance["uah"]:
        balance["usd"] -= sell_dollars
        balance["uah"] += trade
        save_balance(balance)
        print(f'EXCHANGE USD {sell_dollars}\nUAH {trade}, RATE {currency}')
        print(f'USD BALANCE - {balance["usd"]}, UAH BALANCE - {balance["uah"]}')
    else:
        print(f'UNAVAILABLE, REQUIRED BALANCE UAH {trade}, BALANCE is {balance["uah"]}')


def exchange_currency_uah_usd():
    balance = get_balance()
    currency = get_currency_uah_dollar()
    sell_uah = int(input('How many hryvnas do you want to sell? '))
    trade = sell_uah * currency
    if trade < balance["usd"]:
        balance["usd"] += trade
        balance["uah"] -= sell_uah
        save_balance(balance)
        print(f'EXCHANGE UAH {sell_uah}\nUSD {trade}, RATE {currency}')
        print(f'USD BALANCE - {balance["usd"]}, UAH BALANCE - {balance["uah"]}')
    else:
        print(f'UNAVAILABLE, REQUIRED BALANCE USD {balance["usd"] }, BALANCE is {trade}')


course = rate_output(input('What currency do you choose? USD or UAH'))
print(course)
answer = input('Would you like to use the currency exchange service? Y/N')
while answer == 'Y' or answer == 'N':
    while answer == 'Y':
        exchange_currency = (input('What currency do you want to exchange? '
                                   '\nUAH to USD or USD to UAH '))
        if exchange_currency == 'USD to UAH':
            exchange_currency_usd_uah()
            answer = input('Would you like to use the currency exchange service? Y/N')
        elif exchange_currency == 'UAH to USD':
            exchange_currency_uah_usd()
            answer = input('Would you like to use the currency exchange service? Y/N')
        else:
            print('Incorrect exchange')
    if answer == 'N':
        print('STOP \nSERVICE STOPPED')
        break
    else:
        print('Incorrect answer')
