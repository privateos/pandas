import pandas as pd
import numpy as np
import os
old_file_name = 'D:/shan/repo/pandas/read_write_excel/example_multisheets.xlsx'
new_file_name = 'D:/shan/repo/pandas/read_write_excel/example_multisheets_new.xlsx'
writer = pd.ExcelWriter(new_file_name)


df1 = pd.read_excel(old_file_name, sheet_name='一班')
df1['平均成绩'] = (df1['语文'] + df1['数学'])/2
df1.to_excel(writer, sheet_name='一班', index=False)

df2 = pd.read_excel(old_file_name, sheet_name='二班')
df2['平均成绩'] = (df2['语文'] + df2['数学'])/2
df2.to_excel(writer, sheet_name='二班', index=False)

writer.save()
writer.close()
pd.ExcelFile()