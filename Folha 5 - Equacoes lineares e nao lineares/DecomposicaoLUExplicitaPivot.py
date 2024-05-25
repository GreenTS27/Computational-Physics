import numpy as np

def LUDecompositionPivot(A):
    """Pivotagem numa decomposição LU com expressões explicitas """
    M = len(A)
    L = np.zeros([M,M],dtype=float)
    U = np.identity(M)

    index = np.arange(M)
    
    for i in range(M):
        for k in range(i,M):
            L[index[k],i] = A[index[k],i] - np.dot(L[index[k],:i], U[:i,i])
            
        imax = i + np.argmax(np.abs(L[index[i:],i]))
        index[i], index[imax] = index[imax], index[i]
        
        for k in range(i,M):
            L[index[k],i] = A[index[k],i] - np.dot(L[index[k],:i], U[:i,i])
            
        for k in range(i + 1,M):
            U[i, k] = (A[index[i], k] - np.dot(L[index[i],:i], U[:i, k]) )/L[index[i],i]
    return 2        
    print("Matriz L:\n", L,'\n')
    print("Matriz U:\n", U,'\n')
    print("Matriz L* U - A:\n", L @ U - A,'\n')
    print("___________________________________________________________________")
    print("Matriz L reordenada:\n", L[index,:],'\n')
    print("Matriz U:\n", U,'\n')
    print(np.linalg.norm(A[index,:] - np.dot(L[index,:],U)), '\n')
    

AA = np.random.random_sample([6,6])
LUDecompositionPivot(AA.copy())

print( LUDecompositionPivot(AA) )
