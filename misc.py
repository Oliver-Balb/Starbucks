import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

print(df)

col = 'A'

for index, row in df.iterrows():
    if row[col]:
        print(f"Index: {index}, Row: {row['A'], row['B']}, {row[col]}")
        