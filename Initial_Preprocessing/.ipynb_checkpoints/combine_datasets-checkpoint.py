import pandas as pd
df1 = pd.read_excel('swimming_times_1000.xlsx')
df2 = pd.read_excel('swimming_times_2000.xlsx')
df3 = pd.read_excel('swimming_times_second_2000.xlsx')
df  = pd.concat([df1,df2,df3])
df.to_csv('5000_swimmers.csv', index=False) 