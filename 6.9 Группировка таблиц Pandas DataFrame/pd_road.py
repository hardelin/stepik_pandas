#Для этого задания используется случайно генерируемая выборка из 100 записей об использовании велодорожек Монреаля по датам. В выгрузке присутствуют данные только о 7 дорожках (в остальных пустые значения).
#
#Посчитайте среднюю посещаемость каждой велодорожки отдельно по дням недели.
#
#Какой день недели (в среднем) наиболее посещаем?

import pandas as pd

csv = pd.read_csv('dataset_345422_14.txt', ',', parse_dates=['Date'])
csv['Weekday'] = csv['Date'].dt.day_name()
print(csv.groupby('Weekday').mean().mean(axis=1).idxmax())
