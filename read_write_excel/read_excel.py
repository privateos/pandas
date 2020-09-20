import pandas as pd
import numpy as np
import os
old_file_name = 'D:/shan/repo/pandas/read_write_excel/example.xlsx'
new_file_name = 'D:/shan/repo/pandas/read_write_excel/example_new.xlsx'
df = pd.read_excel(old_file_name, sheet_name='Sheet1')
df['平均成绩'] = (df['语文'] + df['数学'])/2
df.to_excel(new_file_name, index=False)