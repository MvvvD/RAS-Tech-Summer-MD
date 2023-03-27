import pandas as pd
n = 20
m = 50
df = pd.read_csv('zadanie-rekrutacyjne.csv')
list1 = df.loc[:].values.tolist()


w_h_ratio = [x[0]/x[1] for x in list1]

weighted_list = list(zip(w_h_ratio, list(list1)))

weighted_list = sorted(weighted_list, key=lambda x:x[0], reverse=True)
print(weighted_list)
h = 0
for n in range(20):
    duck = weighted_list[n][1]
    height = duck[0]
    width = duck [1]
    if m>=width:
        h+=height
        m-=width

print(h)


