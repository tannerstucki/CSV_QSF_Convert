import pandas as pd
new_temp = open('temp.txt', 'w') # writing data to a new file changing the first delimiter only
with open('Word_to_CSV_Tester_v4.txt') as f:
    for line in f:
        line = line.replace('*', '|', 1) # only replace first instance of : to use this as delimiter for pandas
        new_temp.write(line)
new_temp.close()

df = pd.read_csv('temp.txt', delimiter='|', header=None)
df = df.set_index([0]).T
df.to_csv('./new_transposed_df.csv', index=False)