for i in range(0,9):
    for j in range(0,9):
        map[i][j]=random.choices([0,1]], weights=[0.85,0.15], k=1)
print(map)
