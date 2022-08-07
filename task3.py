def main():
    """3. Узнайте у пользователя число n.
    Найдите сумму чисел n + nn + nnn.
    Например, пользователь ввёл число 3.
    Считаем 3 + 33 + 333 = 369."""

    n = input("Input n: ")
    if n.isdigit() and len(n) < 2:
        result = sum([int(n), int(n*2), int(n*3)])
        print(result)
    else:
        print('input incorrect')


if __name__ == '__main__':
    main()
