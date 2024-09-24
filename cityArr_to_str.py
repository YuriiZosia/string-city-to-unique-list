def convert_np(np: str) -> str:
    if np == "":
        return ""

    np = np.replace("  ", " ")
    ns = np.split(",")

    seen = set()  # Набір для унікальності
    unique_cities = []

    for city in ns:
        formatted_city = " ".join(
            "-".join(word.capitalize() for word in part.split("-"))
            for part in city.strip().split()
        )
        if formatted_city not in seen:
            unique_cities.append(formatted_city)
            seen.add(formatted_city)

    return "н.п. " + ", н.п. ".join(unique_cities)


def split_by_n(str_in: str) -> str:
    str_arr = str_in.split("\n")
    massive = []
    for one_str in str_arr:
        massive.append(convert_np(one_str))
    return "\n".join(massive)


#np_in = input("Введіть строку з населеними пунктами,\nякщо пусто то буде зчитаний файл \"city_list.txt\":")

#if np_in == "":
with open("city_list.txt", "r", encoding="utf-8") as file:
    np_in = file.read()

result = split_by_n(np_in)

# Записуємо результат назад у файл з заміною вмісту
with open("city_list.txt", "w", encoding="utf-8") as file:
    file.write(result)
