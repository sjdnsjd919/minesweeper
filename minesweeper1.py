import random

dim1, dim2 = (10, 10)
map = [[random.choices([0,1], weights=[.7937,.2063], k=1) for i in range(dim1)] for j in range(dim2)]
map[0][0]=[1]
for i in range(dim1):
    print("% s" % str(map[i]))
def val(x,y):
    return [i for i in range(8) if check(x,y,i)]
def check(x,y,i):
    return 1 if i == 0 and map[x-1][y-1] == 1 else None
print(check(1,1,0))
