users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
all_users = len(users)
unique_users = len(set(users))
dicti = {"Общее количество": all_users,
         "Уникальные посещения": unique_users
         }
print(dicti)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
