# Independent check of the numbers in "On a contractivity question of Neri and Pinto", from the paper's statements only.
import numpy as np
def Rd(d):
    R = np.zeros((d, d)); R[0,0]=5; R[0,1]=1; R[1,0]=5; R[1,2]=1
    R[d-1,d-1]=5; R[d-1,d-2]=1; R[d-2,d-1]=5; R[d-2,d-3]=1
    for i in range(2, d-2): R[i,i-1]=3; R[i,i+1]=3
    return R
def basisH(d):  # orthonormal basis of the sum-zero hyperplane
    M = np.eye(d) - 1.0/d; u, s, vt = np.linalg.svd(M); return u[:, :d-1]
for d in [8, 9, 10, 20, 40, 60]:
    ev = np.linalg.eigvals(Rd(d)); lst = list(ev); lst.pop(int(np.argmin(abs(ev - 6)))); g = max(x.real for x in lst)
    print("d=%d gamma=%.5f gamma/lambda=%.5f" % (d, g, g/6))
