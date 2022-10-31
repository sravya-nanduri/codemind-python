n=int(input())
i=1
while True:
    k=str(n-i)
    g=str(n+i)
    if k==k[::-1] and g==g[::-1]:
        print(k,g)
        break
    elif k==k[::-1]:
        print(k)
        break
    elif g==g[::-1]:
        print(g)
        break
    else:
        i+=1
        continue
        