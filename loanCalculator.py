__author__ = 'nickyuan'


def loan(cash, rate, periods):
    # rate 单位为日利率
    # periods 单位为月
    # cash 单位为万
    interesttot = 0
    totalpay = 0
    print('********************等额本金********************')
    for i in range(1, periods + 1):
        cashper = cash/periods
        interest = (cash - cashper * (i - 1)) * rate * 30 * 0.01
        totalper = cashper + interest
        left = cash - cashper * i
        interesttot += interest
        totalpay += totalper
        print('本金' + '        ' + '利息' + '  ' + '利息+本金' + '    ' + '剩余','\n',
          ('%d' + '      ' + '%d' + '    ' + '%d' + '       ' + '%d') % (cashper, interest, totalper, left))
    print('********************你知道的********************')


if __name__ == '__main__':
    main = loan(60000, 0.035, 10)