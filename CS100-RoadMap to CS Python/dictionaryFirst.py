import math

def f(x):
    return x + 2

dic = {}

for i in range(10):
    dic[i] = f(i)
for i in dic:
    print(dic[i])

print(str(dic))

dic2 = {"Joe":'McCann', 'Nelly':'Furtado', 'Mah':'Boi'}
dic2['Mah'] = 'boy'

print(dic2["Joe"], dic2['Mah'])
print(dic.keys())
print(dic.get(11))

