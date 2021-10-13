sec_num = int(input('Введите число секунд:'))

if sec_num < 60:
    print ('сек:', sec_num, ';')
elif 60 <=sec_num <= 3540:
    min_num = sec_num // 60
    sec_num = sec_num % 60
    print ('мин:', min_num, ';', 'сек:', sec_num, ';')
elif 3600 <= sec_num <= 86399:
    hr_num = sec_num // 3600
    min_num = (sec_num % 3600) // 60
    sec_num = sec_num % 60
    print ('час:', hr_num,';', 'мин:', min_num, ';', 'сек:', sec_num, ';')
else:
    day_num = sec_num // 86400
    hr_num = (sec_num // 3600) % 24
    min_num = (sec_num % 3600) // 60
    sec_num = sec_num % 60
    print ('дн:', day_num, ';' 'час:', hr_num,';', 'мин:', min_num, ';', 'сек:', sec_num, ';')
