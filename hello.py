import pandas as pd

df = pd.DataFrame([[1, 0], [0, 1]])
sum1 = df[df.columns[0]].sum()
print(sum1)
