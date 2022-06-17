import sys

from Exchange_Rate_and_Balance import get_currency_dollar_uah, get_currency_uah_dollar, \
    get_balance, save_balance


def rate_output(currency):
    balance = get_balance()
    course_dollar = get_currency_dollar_uah()
    course_uah = get_currency_uah_dollar()
    if currency == 'USD':
        currency = f'1 USD to UAH: {course_dollar}, USD BALANCE is {balance["usd"]}'
        return currency
    elif currency == 'UAH':
        currency = f'1 UAH to USD: {course_uah}, UAH BALANCE is {balance["uah"]}'
        return currency
    else:
        print(f'Sorry, we do not exchange this {currency}.\nBye', )
        return sys.exit()


# answer = input('Would you like to use the currency exchange service? Y/N')
course = rate_output(input('What currency do you choose? USD or UAH'))
print(course)
answer = input('Would you like to use the currency exchange service? Y/N')

while answer == 'Y' or answer == 'N':
    while answer == 'Y':
        exchange = input('What currency do you want to exchange? UAH to USD or USD to UAH ')
        if exchange == 'USD to UAH':
            currency_exchange = get_currency_dollar_uah()
            balance = get_balance()
            sell_dollars = int(input('How many dollars do you want to sell? '))
            trade = sell_dollars * currency_exchange
            if trade < balance["uah"]:
                balance["usd"] -= sell_dollars
                balance["uah"] += trade
                save_balance(balance)
                print(f'EXCHANGE USD {sell_dollars}\nUAH {trade}, RATE {currency_exchange}')
                print(f'USD BALANCE - {balance["usd"]}, UAH BALANCE - {balance["uah"]}')
                answer = input('Would you like to use the currency exchange service? Y/N')
            else:
                print(f'UNAVAILABLE, REQUIRED BALANCE UAH {trade}, BALANCE is {balance["uah"]}')
                answer = input('Would you like to use the currency exchange service? Y/N')
        if exchange == 'UAH to USD':
            currency_exchange = get_currency_dollar_uah()
            balance = get_balance()
            sell_uah = int(input('How many hryvnas do you want to sell? '))
            trade = sell_uah * currency_exchange
            if trade < balance["usd"]:
                balance["usd"] += sell_uah
                balance["uah"] -= trade
                save_balance(balance)
                print(f'EXCHANGE UAH {sell_uah}\nUSD {trade}, RATE {currency_exchange}')
                print(f'USD BALANCE - {balance["usd"]}, UAH BALANCE - {balance["uah"]}')
                answer = input('Would you like to use the currency exchange service? Y/N')
            else:
                print(f'UNAVAILABLE, REQUIRED BALANCE USD {balance["usd"]}, BALANCE is {trade}')
                answer = input('Would you like to use the currency exchange service? Y/N')
    if answer == 'N':
        print('STOP \nSERVICE STOPPED')
    break
else:
    print('Incorrect answer')
    answer = input('Would you like to use the currency exchange service? Y/N')
