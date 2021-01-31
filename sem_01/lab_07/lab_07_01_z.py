B = [[1,1,1,0,0,1,1,1],
     [1,0,1,0,1,1,0,1],
     [1,0,1,1,1,0,0,1],
     [1,0,0,0,0,0,1,1],
     [1,0,0,0,0,0,1,0],
     [1,0,1,1,1,0,1,1],
     [1,0,1,0,1,0,0,1],
     [1,1,1,0,1,1,1,1]]

srvse = [0]*8 
stvse = [0]*8
sr = [0]*8
st = [0]*8
kol0 = 0
for i in range(8):
    for j in range(8):
        if B[i][j] == 1:
            if j - 1 == -1:
                srvse[i] += 1
            elif i - 1 == -1:
                stvse[j] += 1
            else:
                if B[i][j-1] == 0:
                    srvse[i] += 1
                if B[i-1][j] == 0:
                    stvse[j] += 1
for i in range(8):
    for j in range(8):
        if B[i][j] == 1:
            if j - 1 == -1:
                sr[i] += 1
            elif i - 1 == -1:
                st[j] += 1
            else:
                if B[i][j-1] == 0:
                    sr[i] += 1
                if B[i-1][j] == 0:
                    st[j] += 1
        if (B[i][j] == 0 and sr[i] < srvse[i] and
            st[j]<stvse[j] and sr[i] != 0 and st[j] != 0):
            kol0 += 1
print('Количество нулей в области:', kol0)
