def add_everything_up(a, b):
    try:
        summa = round((a + b), 3)
        return summa
    except(TypeError):
        summa = str(a) +str(b)
        return summa







print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))