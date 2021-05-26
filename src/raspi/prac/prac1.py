x = 2
rnew = x
for i in range(10000):
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1,rnew,r2)
