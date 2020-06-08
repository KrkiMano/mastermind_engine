import random

holder = []


def number_guess():
    while True:
        user_num = input('Введи четырёхзначное число c неповторяющимися цифрами: ')
        if user_num[0] == '0':
            continue
        elif len(set(user_num)) == 4:
            break
    return user_num


def get_number():
    global holder
    holder = []
    a = str(random.randint(1, 9))
    holder.append(a)
    while True:
        a = str(random.randint(0, 9))
        if a not in holder:
            holder.append(a)
        if len(holder) == 4:
            break
    return holder


def check_number(user_guess):
    global holder
    cows, bulls = 0, 0
    for num, x in enumerate(holder):
        if str(user_guess[num]) == str(holder[num]):
            bulls += 1
        elif str(user_guess[num]) in str(holder):
            cows += 1
    return bulls, cows

print('Давай поиграем в игру "Быки и Коровы".')

while True:
    print('Компьютер загадал число из 4 цифр:')
    get_number()
    count = 0
    bulls, cows = 0, 0
    while bulls < 4:
        count += 1
        user_guess = number_guess()
        bulls, cows = check_number(user_guess)
        print('быки -', bulls, ',', 'коровы -', cows)
    print('Ты выиграли игру за', count, 'ход.', '\nХочешь еще партию?')
    final_question = input('Ответ: [д]a или [н]ет?')
    if final_question == 'д':
        get_number()
        continue
    else:
        break
