# WRITE A PYTHON FUNCTION THAT TAKES AN INTEGER 'N' AS A PARAMETER AND RETURNS THE SUM OF THE FIRST 'N' PRIME NUMBERS

def is_prime_number(number): #Prime number validation function
    if number < 2: 
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_numbers(limit): #Calculate the prime numbers and register it on list
    list_numbers = []
    number = 2

    while len(list_numbers) < limit:
        if is_prime_number(number):
            list_numbers.append(number)
        number += 1

    return list_numbers

def main(): #User interface
    while True:
        limit = 0
        while limit <= 0:
            limit = int(input('Digite um número: '))
        if limit > 1:
            print(f'A soma dos {limit} primeiros números primos corresponde a {sum(prime_numbers(limit))}')
        else:
            print(f'{prime_numbers(limit)} foi o único número encontrado!')

if __name__ == '__main__':
    main()
    