import random

dim1, dim2 = (10, 10)
map = [[random.choices([0,1], weights=[.7937,.2063], k=1) for i in range(dim1)] for j in range(dim2)]
for i in range(dim1):
    print("% s" % str(map[i]))
def val(x,y):
    if map[x][y]!=[1]:
        k=0
        for i in range(8):
            if check(x,y,i,1):
                k+=1
        return  k
    else:
        return "$"
def check(x,y,i,k):
    if i == 0 and x!=0 and y!=0 and map[x-1][y-1] == [k]:
        return 1
    if i == 1 and x!=0 and map[x-1][y] == [k]:
        return 1
    if i == 2 and x!=0 and y!=9 and map[x-1][y+1] == [k]:
        return 1
    if i == 3 and y!=9 and map[x][y+1] == [k]:
        return 1
    if i == 4 and x!=9 and y!=9 and map[x+1][y+1] == [k]:
        return 1
    if i == 5 and x!=9 and map[x+1][y] == [k]:
        return 1
    if i == 6 and x!=9 and y!=0 and map[x+1][y-1] == [k]:
        return 1
    if i == 7 and y!=0 and map[x][y-1] == [k]:
        return 1

map2 = [[[val(j,i)] for i in range(dim1)] for j in range(dim2)]
print("\n    0    1    2    3    4    5    6    7    8    9")
for i in range(dim1):
    print("% s" % i + " " +str(map2[i]).replace("'",""))
map3 = [[['-'] for i in range(dim1)] for j in range(dim2)]
k1 = random.randint(0,9)
k2 = random.randint(0,9)
while map2[k1][k2] != [0]:
    k1 = random.randint(0,9)
    k2 = random.randint(0,9)
map3[k1][k2]=['*']
print("\n    0    1    2    3    4    5    6    7    8    9")
for i in range(dim1):
    print("% s" % i + " " +str(map3[i]).replace("'",""))
