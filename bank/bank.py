import account_buy
def main():
    rate = int(input('Введите ставку\n'))
    money = int(input('Введите сумму\n'))
    period = int(input('Введите период\n'))
    result = account_buy.calculate_income(rate,period,money)
    print('Ваша ставка: ',rate,'\n'+'Период: ',period,'\n''Ваша сумма: ',money,'\n''Результат:',result)
if __name__ == '__main__':
    main()

