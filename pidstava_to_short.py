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

#text = "підг. №66т/КП від 08.01.2024, підг. №67т/КП від 08.01.2024, підг. №68т/КП від 08.01.2024, підг. №453т/КП від 27.06.2024, підг. №454т/КП від 27.06.2024, підг. №455т/КП від 27.06.2024, підг. №456т/КП від 27.06.2024, підг. №457т/КП від 27.06.2024, підг. №458т/КП від 27.06.2024, підг. №562т/КП від 28.07.2024, підг. №563т/КП від 28.07.2024, підг. №564т/КП від 28.07.2024, підг. №565т/КП від 28.07.2024, підг. №566т/КП від 28.07.2024, підг. №567т/КП від 28.07.2024, підг. №568т/КП від 28.07.2024, підг. №569т/КП від 28.07.2024, підг. №570т/КП від 28.07.2024, підг. №571т/КП від 28.07.2024, підг. №572т/КП від 28.07.2024, підг. №573т/КП від 28.07.2024, підг. №574т/КП від 28.07.2024, підг. №575т/КП від 28.07.2024, підг. №577т/КП від 28.07.2024, підг. №578т/КП від 28.07.2024, підг. №579т/КП від 28.07.2024"

np_in = input("Введіть строку:")
print(group_numbers(np_in))
