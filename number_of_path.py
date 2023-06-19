date = input('Введите дату рождения в формате ДД.ММ.ГГГГ:')


def calculation(date):
    numbers = list(date)
    numbers.pop(2)
    numbers.pop(4)
    total = 0
    for i in numbers:
        num = int(i)
        total += num
    if total < 10 or (total % 10 == total // 10):
        print(total)
    else:
        print(total % 10 + total // 10)


calculation(date)
