# End-to-end check of the product decomposition on a small instance:
# n = 12, three blocks of size b = 4, each block using the same 4 x 8 generator matrix
# (a fixed full-rank Toeplitz block), N = 2n = 24 generators.  Compare the exact TV of the
# walk on Z_2^12 with the bound  E_counts[ sum_j TV_b(K_j) ]  where TV_b(K) is the exact
# TV of the block walk after K steps and (K_1,K_2,K_3) ~ Multinomial(k; 1/3,1/3,1/3).
# The memo's inequality is TV(X_k) <= that expectation; here we check it holds.
import numpy as np, math
from math import comb
b,L=4,3; n=b*L; Nb=2*b
bits=[1,0,1,1,0,0,1,0,1,1,1]   # 8+4-1 bits
Mb=np.array([[bits[c-r+b-1] for c in range(Nb)] for r in range(b)])
# rank check over F_2
def rank_f2(A):
    A=A.copy()%2; r=0
    for c in range(A.shape[1]):
        p=[i for i in range(r,A.shape[0]) if A[i,c]]
        if not p: continue
        A[[r,p[0]]]=A[[p[0],r]]
        for i in range(A.shape[0]):
            if i!=r and A[i,c]: A[i]^=A[r]
        r+=1
    return r
print("block matrix rank over F_2:",rank_f2(Mb),"of",b)
cols_b=[int(sum(Mb[r,i]<<r for r in range(b))) for i in range(Nb)]
# block walk exact TV curve
def tv_curve(cols,dim,kmax):
    mu=np.zeros(2**dim); mu[0]=1; xs=np.arange(2**dim); out=[0.5*np.abs(mu-2.0**-dim).sum()]
    for k in range(1,kmax+1):
        mu=sum(mu[xs^c] for c in cols)/len(cols)
        out.append(0.5*np.abs(mu-2.0**-dim).sum())
    return np.array(out)
kmax=40
tvb=tv_curve(cols_b,b,kmax)
# full walk: generators = block copies
cols=[c<<(b*j) for j in range(L) for c in cols_b]
tvn=tv_curve(cols,n,kmax)
# bound: E[sum_j TV_b(K_j)] = L * E[TV_b(K)], K ~ Bin(k,1/L)
for k in range(0,kmax+1,4):
    bound=L*sum(comb(k,i)*(1/L)**i*(1-1/L)**(k-i)*tvb[i] for i in range(k+1))
    print(f"k={k:2d} exact TV on Z_2^{n} = {tvn[k]:.5f}   product bound = {min(bound,1):.5f}   ok={tvn[k]<=min(bound,1)+1e-12}")
