def main():
    """5. Запросите у пользователя значения выручки и издержек фирмы.
    Определите, с каким финансовым результатом работает фирма.
    Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
    Выведите соответствующее сообщение.
    6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
    Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника."""

    revenue = input("Введите выручку $: ")
    revenue = int(revenue) if revenue.isdigit() else 0
    costs = input("Введите затраты $: ")
    costs = int(costs) if costs.isdigit() else 0
    profit = revenue - costs
    if profit > 0:
        profitability = (profit / revenue) * 100
        print(f"Прибыль составила {profit}$")
        print(f"Рентабельность {profitability}%")
        number_of_employees = input("Введите количество работников ")
        number_of_employees = int(number_of_employees) if number_of_employees.isdigit() else 0
        if number_of_employees:
            profit_per_employee = profit / number_of_employees
            print(f"Прибыль на одного работника составила {profit_per_employee}$")
        else:
            print(f"Некорректно ввели количество работников")
    elif profit == 0:
        print(f"Сработали в {profit}")
    else:
        print(f"Убыток составил {profit * -1}$")


if __name__ == '__main__':
    main()
