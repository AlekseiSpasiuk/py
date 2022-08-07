def main():
    """4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
    Для решения используйте цикл while и арифметические операции."""

    number = input("Input number: ")
    number = int(number) if number.isdigit() else 0
    max_digit = 0
    while number:
        last_digit = number % 10
        number //= 10
        if max_digit < last_digit:
            max_digit = last_digit
    print(f"Max digit {max_digit}")


if __name__ == '__main__':
    main()
