def solveGaussJordanPivotagemTotal(A, b):
    M = len(b)
    linhas = np.arange(M)
    colunas = np.arange(M + 1)
    AA = np.zeros([M, M+1])
    AA[:M,:M] = A
    AA[:,M] = b
    aa = np.zeros(M * M)

    for p in range(M):
        m = M - p
        for i in range(m):
            aa[i * m:(i + 1) * m] = AA[linhas[p + i], colunas[p:-1]]
        print(aa[:m * m])
        index = np.argmax(np.abs(aa[:m * m]))

        l1 = p + index // m
        c1 = p + index % m
        linhas[p], linhas[l1] = linhas[l1], linhas[p] 
        colunas[p], colunas[c1] = colunas[c1], colunas[p]        
        AA[linhas[p], colunas[:] ] /= AA[linhas[p],colunas[p]]
        for i in range(p):
            AA[linhas[i],colunas[p:]] -= AA[linhas[p],colunas[p:]] * AA[linhas[i],colunas[p]]
            
        for i in range(p + 1, M):
            AA[linhas[i],colunas[p:]] -= AA[linhas[p],colunas[p:]] * AA[linhas[i],colunas[p]]

    return AA[colunas[linhas[:]], -1]

AA = np.array([[0.1,1,2, 4.1],[3,4.1,5,2],[6,7,8,5],[0.5,0,3,5]])
BB = np.array([0.1, 0.2, 0.3, 0.4])
sol = solveGaussJordanPivotagemTotal(AA.copy(), BB.copy())
np.dot(AA, sol) - BB
