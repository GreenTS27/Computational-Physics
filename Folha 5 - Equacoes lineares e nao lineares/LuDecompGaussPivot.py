import numpy as np

def LUDecompositionGaussPivot(A):
    """
    Escrever explicitamente as expressões
    """
    M = len(A)
    L = np.zeros([M,M],dtype=float)
    U = np.copy(A)
    index = np.arange(M)
    
    for i in range(M):
        imax = i + np.argmax(np.abs(U[index[i:], i]))
        index[i], index[imax] = index[imax], index[i]
        
        L[index[i:],i] = U[index[i:], i]

        U[index[i],:] /= U[index[i],i]
        for k in range(i + 1, M):
            U[index[k],i:] -= U[index[k],i] * U[index[i],i:]

    print("Matriz L:\n", L,'\n')
    print("Matriz L reordenada:\n", L[index,:],'\n')
    print("Matriz U:\n", U[index,:],'\n')
    print(np.linalg.norm(A[index,:] - np.dot(L[index,:],U[index,:])), '\n')
    


AA = np.random.random_sample([6,6])
LUDecompositionGaussSeidelPivot(AA.copy())
