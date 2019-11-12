prim = [2]
for n in range(3, 10000):
    if len([m for m in prim if n%m==0])==0:
        prim.append(n)

count = 10000
while 1:
    if len([m for m in prim if count%m==0])==0:
        prim.append(n)
        print(count)

    count += 1
