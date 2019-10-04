mYear = None
while not (mYear is not None and mYear.isdigit()):
    if mYear is not None:
        print('  Не является числом, попробуйте ещё раз...')
    mYear = input('Введите год рождения А.С.Пушкина: ')
mYear = int(mYear)
if 1799 == mYear:
    mDay = None
    while not (mDay is not None and mDay.isdigit()):
        if mDay is not None:
            print('  Не является числом, попробуйте ещё раз...')
        mDay = input('Введите день рождения А.С.Пушкина: ')
    mDay = int(mDay)
    if 26 == mDay:
        print('Верно!')
    else:
        print('Не верный день рождения!')
else:
    print('Не верный год рождения!')
