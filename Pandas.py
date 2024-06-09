# -*- coding: UTF-8 -*-
import pathlib
import pandas
from pathlib import Path

work_path = pathlib.Path.cwd()
print(work_path)
data_path = Path(work_path, 'datasets', 'Free_Test_Data_500KB_CSV-1.csv')
data = pandas.read_csv(data_path, nrows=5)

print(data)
# print(data[['AGE', 'NAME']])
# print(data.count())

name_table = data[['NAME']]
print(name_table)
print(name_table.count())

print(data.NAME.count())
print(data.AGE.sum())
print(data.AGE.min())
print(data.AGE.max())
mean_1 = data.AGE.mean()
print(mean_1)

median_1 = data.AGE.median()
print(median_1)





