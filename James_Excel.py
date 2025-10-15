import pandas as pd

df = pd.read_excel('Financial_Sample.xlsx')   

sums = df.select_dtypes(include='number').sum()

sums['Name'] = 'Total'

df_with_total = pd.concat([df, pd.DataFrame([sums])], ignore_index=True)
print(df_with_total)

df_with_total.to_excel('output.xlsx', index=False)

