#Переменная df содержит DataFrame.
#
#new_index - индекс для строки, которую надо добавить
#new_data - значения для строки, которую надо добавить
#del_index - индекс строки, которую надо удалить
#Добавьте новую строку (с индексом new_index и значениями new_data) и удалите одну из старых (del_index)
#
#Выведите df на печать.

a = df.drop(del_index)
a.loc[new_index] = new_data
print(a)
