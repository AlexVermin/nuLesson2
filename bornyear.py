mYear = None
while not (mYear is not None and mYear.isdigit()):
    if mYear is not None:
        print('  Не является числом, попробуйте ещё раз...')
    mYear = input('Введите год рождения А.С.Пушкина: ')
mYear = int(mYear)
if 1799 == mYear:
    print('Верно!')
else:
    print('Не верно!')
