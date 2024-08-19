def convert_np(np: str) -> str:
    # Видалити зайві пробіли між словами
    np = np.replace("  ", " ")
    # Розділити рядок на частини
    ns = np.split(",")
    # Очистити кожен елемент від зайвих пробілів, форматувати та привести до потрібного регістру
    n_tuple = set(
        " ".join(
            "-".join(word.capitalize() for word in part.split("-"))
            for part in city.strip().split()
        )
        for city in ns
    )
    # Повернути форматований рядок
    return "н.п. " + ", н.п. ".join(n_tuple)


np_in = input("Введіть строку з населеними пунктами:")
print(convert_np(np_in))
