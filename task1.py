def main():
    """1. Поработайте с переменными, создайте несколько, выведите на экран.
    Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран."""

    name = input("Input your name: ")
    age = input('input you age: ')
    age = int(age) if age.isdigit() else 0
    print(f"Your name is {name}. Your age {age}")


if __name__ == '__main__':
    main()
