import json

import pandas as pd

a = [["1","2"],["s"],["指纹"]]
x = json.dumps(a)
x2 = json.loads(x)
aa = [x for x in a]
bb = a.copy()
a.append("x")
a[1].append(("as"))
print(a)
print(bb)
print(aa)
print(x2)
exit()


df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
ser1 = pd.Series(['e', 'f', 'g'], index=[1, 2, 3])
# print(ser1.index)
# ser1.
# ser2 = pd.Series(ser1, index=[0,1,2])
# print(ser2)
# exit()
# a = ser1.reindex()
# ser1.reset_index(inplace=True)
# print(a)
print(ser1)
print(123)
exit()

print(123)
print(df)
ser2 = ser1.copy()
df2 = ser2.to_frame()
df2.columns = ["x"]
df2.reset_index(inplace=True)
print(df2)
print()
df["c"] = df2["x"]
print(df)