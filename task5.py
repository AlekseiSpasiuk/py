def main():
    """5. Запросите у пользователя значения выручки и издержек фирмы.
    Определите, с каким финансовым результатом работает фирма.
    Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
    Выведите соответствующее сообщение."""

    revenue = input("Введите выручку $: ")
    revenue = int(revenue) if revenue.isdigit() else 0
    costs = input("Введите затраты $: ")
    costs = int(costs) if costs.isdigit() else 0
    profit = revenue - costs
    if profit > 0:
        print(f"Прибыль составила {profit}$")
    elif profit == 0:
        print(f"Сработали в {profit}")
    else:
        print(f"Убыток составил {profit * -1}$")


if __name__ == '__main__':
    main()
