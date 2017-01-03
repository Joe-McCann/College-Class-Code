import string
x = 'hello'
print(x.lower(), x)
print(x.upper(), x)
print(x.index('l'))
print(x.find('dog'))
print(x.find('hell'))
print(x.replace('he', 'she'))

y = "!?hello//"
print(len(y), y)
print(y.strip("?!/"))
z = "?hello,bye,how are you"
print(z.strip("?,h"))
print(y.strip(",!/o"))
print(z.strip(string.punctuation))

a = "Hello my name is joe"
print(a.split())
phone = '732-609-7755'
print(phone.split('-'))
print(a.split('name'))

line = "evacuate, evacuate, evacuate"
count = 0
for i in line.split():
    if i.strip(string.punctuation) == 'evacuate':
        count += 1
print(count)

