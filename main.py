import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('day73(Data Visualisation with Matplotlib)\QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
print(df.head())
print(df.tail())



# test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old'],
#                         'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu'],
#                         'Power': [100, 80, 25, 50, 99, 75, 5]})
# print(test_df)

# pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
# print(pivoted_df)

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df)

plt.plot(reshaped_df.index, reshaped_df["python"])