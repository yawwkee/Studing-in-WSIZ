list = [ ]
for i in range(1000,10000):
    pdc = i // 100
    odc = i % 100
    if i == pdc**2 + odc**2:
        list.append(i)
print(list)
print(len(list))
