import re

# Читання файлу
with open("city_list.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Заміна фраз
phrases_to_replace = [
    "південно-західніше ", "південно-східніше ",
    "північно-східніше ", "північно-західніше ",
    "південно-західна околиця в ", "північно-східна околиця в ",
    "південно-східна околиця в ", "північно-західна околиця в ",
    "східна околиця в ", "західна околиця в ", "південна околиця в ", "північна околиця в ",
    "східніше ", "західніше ", "південніше ", "північніше "
]
for phrase in phrases_to_replace:
    content = content.replace(phrase, "")

# Регулярні вирази
# 1. Заміна "\n{1,}" на "\n"
content = re.sub(r"\n{2,}", "\n", content)

# 2. Видалення останнього абзацу
#content = re.sub(r"\n[^\n]*$", "", content)

# 3. Заміна "\n" на ", "
content = content.replace("\n", ", ")

# Запис результату назад у файл
with open("city_list.txt", "w", encoding="utf-8") as file:
    file.write(content)
