def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for j in range(2, result):
            if result % j != 0:
                print('Простое')
            else:
                print('Составное')
            break
        return result
    return wrapper

@is_prime
def sum_three(*args):
    summa = sum(args)
    return summa

result = sum_three(2, 3, 6)
print(result)
