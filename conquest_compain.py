def ConquestCampaign(N, M, L, battalion):
    q = 1
    h = True
    a = [[0]*M for i in range(N)]
    for j in range(0, (L*2), 2):
        a[battalion[j]-1][battalion[j+1]-1] = 1
       
    while h:
        for i in range(N):
            for j in range(M):
                if a[i][j] != 0:
                    a[i][j] += 1      
        for k in range(N):
            for l in range(M):
                if a[k][l] == 0:
                    if k>0 and k < N-1 and l>0 and l < M-1:
                        if a[k-1][l]>=2 or a[k+1][l]>=2 or a[k][l+1]>=2 or a[k][l-1]>=2:
                            a[k][l] += 1
                    elif k == 0 and l == 0:
                        if a[k+1][l]>=2 or a[k][l+1]>=2:
                            a[k][l] += 1
                    elif k == N-1 and l == M-1:
                        if a[k-1][l]>=2 or a[k][l-1]>=2:
                            a[k][l] += 1
                    elif k == 0 and l == M-1:
                        if a[k+1][l]>=2  or a[k][l-1]>=2:
                            a[k][l] += 1
                    elif k == N-1 and l == 0:
                        if a[k-1][l]>=2 or a[k][l+1]>=2:
                            a[k][l] += 1
                    elif k == 0:
                        if  a[k+1][l]>=2 or a[k][l+1]>=2 or a[k][l-1]>=2:
                            a[k][l] += 1
                    elif k == N-1:
                        if a[k-1][l]>=2 or a[k][l+1]>=2 or a[k][l-1]>=2:
                            a[k][l] += 1
                    elif l == 0:
                        if a[k-1][l]>=2 or a[k+1][l]>=2 or a[k][l+1]>=2:
                            a[k][l] += 1
                    else:
                        if a[k-1][l]>=2 or a[k+1][l]>=2 or a[k][l-1]>=2:
                            a[k][l] += 1        
                
        for v in range(N):
            for g in range(M):
                if a[v][g] == 0:
                    h = True
                    break
                else:
                    h = False
        q += 1      
                     
    return(q)

print(ConquestCampaign(3, 4, 2, [2,2, 3,4]))
