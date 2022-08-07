def main():
    """2. Пользователь вводит время в секундах.
   Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
   Используйте форматирование строк."""

    seconds_str = input("Input seconds: ")
    seconds = int(seconds_str) if seconds_str.isdigit() else 0
    hours = int(seconds // 3600)
    minutes = int((seconds - hours * 3600) // 60)
    seconds = seconds % 60
    print(f"{(hours % 24) :02}:{minutes :02}:{seconds :02}")


if __name__ == '__main__':
    main()
