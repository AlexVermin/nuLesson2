# Евгений Кафельников - 1974
# Икер Касильяс - 1981
# Михаэль Шумахер - 1969
# Хелена Бонем Картер - 1966
# Том Йорк - 1968
# Киану Ривз - 1964
# Элвис Пресли - 1977
cntTotal = 7
cnt = 0
while True:
    cnt = 0
    # q1
    mYear = None
    while True:
        if mYear is not None:
            if mYear.isdigit():
                nYear = int(mYear)
                if 1974 == nYear:
                    cnt += 1
                break
            else:
                print('  Введённое значение не является числом, попробуйте снова...')
        mYear = input('Год рождения теннисиста Евгения Кафельникова: ')
    # q2
    mYear = None
    while True:
        if mYear is not None:
            if mYear.isdigit():
                nYear = int(mYear)
                if 1981 == nYear:
                    cnt += 1
                break
            else:
                print('  Введённое значение не является числом, попробуйте снова...')
        mYear = input('Год рождения вратаря Икера Касильяса: ')
    # q3
    mYear = None
    while True:
        if mYear is not None:
            if mYear.isdigit():
                nYear = int(mYear)
                if 1969 == nYear:
                    cnt += 1
                break
            else:
                print('  Введённое значение не является числом, попробуйте снова...')
        mYear = input('Год рождения автогонщика Михаэля Шумахера: ')
    # q4
    mYear = None
    while True:
        if mYear is not None:
            if mYear.isdigit():
                nYear = int(mYear)
                if 1966 == nYear:
                    cnt += 1
                break
            else:
                print('  Введённое значение не является числом, попробуйте снова...')
        mYear = input('Год рождения актрисы Хелены Бонем Картер: ')
    # q5
    mYear = None
    while True:
        if mYear is not None:
            if mYear.isdigit():
                nYear = int(mYear)
                if 1968 == nYear:
                    cnt += 1
                break
            else:
                print('  Введённое значение не является числом, попробуйте снова...')
        mYear = input('Год рождения солиста группы Radiohead Тома Йорка: ')
    # q6
    mYear = None
    while True:
        if mYear is not None:
            if mYear.isdigit():
                nYear = int(mYear)
                if 1964 == nYear:
                    cnt += 1
                break
            else:
                print('  Введённое значение не является числом, попробуйте снова...')
        mYear = input('Год рождения актера Киану Ривза: ')
    # q7
    mYear = None
    while True:
        if mYear is not None:
            if mYear.isdigit():
                nYear = int(mYear)
                if 1977 == nYear:
                    cnt += 1
                break
            else:
                print('  Введённое значение не является числом, попробуйте снова...')
        mYear = input('Год рождения певца Элвиса Пресли: ')
    # Вывод результатов:
    print('------------------------------------------------')
    print('|  Итоги очердного раунда викторины            |')
    print('------------------------------------------------')
    print('|  Правильных ответов         |   %8d     |' % cnt)
    print('|  Неверных ответов           |   %8d     |' % (cntTotal - cnt))
    print('|  Процент правильных ответов |   %8.1f     |' % (cnt/cntTotal*100))
    print('|  Процент неверных ответов   |   %8.1f     |' % ((cntTotal-cnt)/cntTotal*100))
    print('------------------------------------------------')
    # Поторить?
    mRepeat = None
    while True:
        if mRepeat is not None:
            if 'Y' == mRepeat or 'N' == mRepeat:
                break
            else:
                print('  Пожалуйста введите допусимое значение...')
        mRepeat = input('Ещё разок? (Y - если хочется повторить, N - выход из программы)')
    if 'N' == mRepeat:
        break;