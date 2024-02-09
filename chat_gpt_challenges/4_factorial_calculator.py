def factorial(num):
    for i in range(1, num):
        num = num * i
    return num

if __name__ == "__main__":
    print(factorial(int(input('Fatorial de: '))))