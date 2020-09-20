import pandas as pd
import numpy as np
import os
old_file_name = 'D:/shan/repo/pandas/read_write_excel/example_multisheets.xlsx'
new_file_name = 'D:/shan/repo/pandas/read_write_excel/example_multisheets_new_concat_in_row.xlsx'
writer = pd.ExcelWriter(new_file_name)
reader = pd.ExcelFile(old_file_name)

dfs = []
for sheet in reader.sheet_names:
    df = reader.parse(sheet_name=sheet)
    df['平均成绩'] = (df['语文'] + df['数学'])/2
    dfs.append(df)
concated_dfs = pd.concat(dfs, axis=0)
concated_dfs.to_excel(writer, sheet_name='一班和二班', index=False)

writer.save()
writer.close()