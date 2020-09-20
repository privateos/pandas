import pandas as pd
import numpy as np
import os
old_file_name = 'D:/shan/repo/pandas/read_write_excel/example_for_merge_in_colums.xlsx'
new_file_name = 'D:/shan/repo/pandas/read_write_excel/example_merge_in_colums.xlsx'
writer = pd.ExcelWriter(new_file_name)
reader = pd.ExcelFile(old_file_name)

merged_df = None
for sheet in reader.sheet_names:
    df = reader.parse(sheet_name=sheet)
    if merged_df is None:
        merged_df = df
    else:
        merged_df = pd.merge(merged_df, df)

merged_df.to_excel(writer, sheet_name='合并后的sheet', index=False)

writer.save()
writer.close()