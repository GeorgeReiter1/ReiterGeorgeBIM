def find_common_participants(first_group, second_group, divide_with = ","):
    divided_first_group = first_group.replace(divide_with, ',').split(',')
    divided_second_group = second_group.replace(divide_with, ',').split(',')
    common_people = list(set(divided_first_group).intersection(divided_second_group))
    common_people.sort()
    return common_people

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(f"{find_common_participants(participants_first_group, participants_second_group,"|")}")


