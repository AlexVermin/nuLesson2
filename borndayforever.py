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
                print('  Не верно, попробуйте ещё раз...')
        else:
            print('  Не является числом, попробуйте ещё раз...')
    mYear = input('Введите год рождения А.С.Пушкина: ')
mDay = None
while True:
    if mDay is None:
        pass
    else:
        if mDay.isdigit():
            nDay = int(mDay)
            if 26 == nDay:
                break
            else:
                print('  Не верно, попробуйте ещё раз...')
        else:
            print('  Не является числом, попробуйте ещё раз...')
    mDay = input('Введите день рождения А.С.Пушкина: ')
print('Верно!')
