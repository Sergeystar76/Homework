def decorator(func):
    def wapper(*args):
        result = func(*args)
        for j in range(2, result):
            if result % j != 0:
                print('Простое')
            else:
                print('Составное')
            break
        return result
    return wapper

@decorator
def sum_three(*args):
    summa = sum(args)
    return summa

result = sum_three(2, 3, 6)
print(result)
