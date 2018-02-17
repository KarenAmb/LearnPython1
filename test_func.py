def get_vat(price, vat_rate):
    if price > 0:
        vat = price / 100 * vat_rate
        price_no_vat = price - vat
        print(price_no_vat)
    else:
        print('price is wrong')


price1 = -100
vat_rate = 18
get_vat(price1, vat_rate)


def get_summ(one, two, delimeter=' '):
    string1 = str(one) + str(delimeter) + str(two)
    print(string1.upper())


get_summ('privet', 'andrey')
