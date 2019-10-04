mYear = None
while True:
    if mYear is None:
        pass
    else:
        if mYear.isdigit():
            nYear = int(mYear)
            if 1799 == nYear:
                break
            else:
                print('  Не верно!')
        else:
            print('  Не является числом, попробуйте ещё раз...')
    mYear = input('Введите год рождения А.С.Пушкина: ')
print('Верно!')
