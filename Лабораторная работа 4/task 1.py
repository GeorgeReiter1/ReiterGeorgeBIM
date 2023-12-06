import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)

    sum_of_mult = 0  # Переменная для суммы произведений
    for value in data:
        # На случай, если в словаре нет нужных ключей
        score = value.get("score", 0)
        weight = value.get("weight", 0)

        product = score * weight
        sum_of_mult += product

    return round(sum_of_mult, 3)


print(task())
