from collections import Counter
az = open ('pbnumbers.txt', 'r')
x = az.read()
k = x.split()
Counter = Counter(k)
print (Counter.most_common(10))



