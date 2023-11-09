def count_letters(text_str):
    new_list = text_str.lower() #тот же текст в нижнем регистре
    correct_list = list()   #лист для заполнения
    for letter in new_list:
        if letter.isalpha():
            correct_list.append(letter) #добавлям буквы в список для заполнения

    needed_dictionary = {} #словарь для заполнения
    for letter in correct_list: #рассматриваем все буквы из нового списка
        if letter not in needed_dictionary: #добавляем пары, если их ещё нет
            needed_dictionary[letter] = correct_list.count(letter)

    return needed_dictionary

def calculate_frequency(needed_dictionary):
    total = sum(needed_dictionary.values()) #суммируем все буквы
    new_dictionary = {}
    for letter in needed_dictionary:
        new_dictionary[letter] = f"{(needed_dictionary[letter]/total):.2f}" #жаль, что не воспользоваться round(,2) - ответ-то всё равно правильный...
    return new_dictionary


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
for letter, value_ in calculate_frequency(count_letters(main_str)).items():
    print(f"{letter}: {value_}")
