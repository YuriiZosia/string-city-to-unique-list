import re

def group_numbers(text):
    # Регулярний вираз для пошуку всіх підг. з номерами і датами
    matches = re.findall(r'підг\. №(\d+)т/КП від (\d{2}\.\d{2}\.\d{4})', text)

    grouped = {}
    # Групуємо підготовки за датою
    for number, date in matches:
        if date not in grouped:
            grouped[date] = []
        grouped[date].append(int(number))

    result = []
    for date, numbers in grouped.items():
        numbers.sort()
        # Групуємо послідовні номери
        grouped_numbers = []
        start = numbers[0]
        prev = numbers[0]

        for i in range(1, len(numbers)):
            if numbers[i] == prev + 1:
                prev = numbers[i]
            else:
                if start == prev:
                    grouped_numbers.append(f'№{start}т/КП')
                else:
                    grouped_numbers.append(f'№{start}-{prev}т/КП')
                start = numbers[i]
                prev = numbers[i]

        if start == prev:
            grouped_numbers.append(f'№{start}т/КП')
        else:
            grouped_numbers.append(f'№{start}-{prev}т/КП')

        result.append(f"підг. {', '.join(grouped_numbers)} від {date}")

    return ', '.join(result)


np_in = input("Введіть строку:")
print(group_numbers(np_in))
