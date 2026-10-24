import itertools, math
import numpy as np

def walsh_U(m):
    assert m % 4 == 0
    s=np.r_[np.ones(m//2),-np.ones(m//2)]
    return np.column_stack([np.ones(m),s])/math.sqrt(m)

def leaf(m,sigma=1.0):
    U=walsh_U(m)
    K=sigma*U@U.T
    return np.block([[np.zeros((m,m)),K],[K,np.zeros((m,m))]])

def intercut(m):
    k=m//2; q=k//2
    groups=[list(range(0,k)),list(range(k,m)),list(range(m,m+k)),list(range(m+k,2*m))]
    S=[]; T=[]
    for g in groups:
        S += g[:q]; T += g[q:]
    return S,T

def vol3(M):
    nr,nc=M.shape
    Z=0.0
    ar=np.zeros(nr); bc=np.zeros(nc)
    for R in itertools.combinations(range(nr),3):
        for C in itertools.combinations(range(nc),3):
            w=float(np.linalg.det(M[np.ix_(R,C)])**2)
            Z+=w
            for i in R: ar[i]+=w
            for j in C: bc[j]+=w
    return Z,ar/Z,bc/Z

def hub_square(m):
    a=np.ones(m)/math.sqrt(m)
    z=np.ones(m)/math.sqrt(m)
    A=np.zeros((1+2*m,1+2*m))
    A[0,1:1+m]=a
    A[1:1+m,0]=a
    A[1+m:,1+m:]=np.outer(z,z)
    return A

def Wrs(A):
    n=A.shape[0]
    T=list(itertools.combinations(range(n),3))
    W=np.zeros(4)
    for I in T:
        SI=set(I)
        for J in T:
            w=float(np.linalg.det(A[np.ix_(I,J)])**2)
            W[len(SI.intersection(J))]+=w
    return W

m=8
L=leaf(m)
S,T=intercut(m)
M=L[np.ix_(S,T)]
sv=np.linalg.svd(M,compute_uv=False)
Z,alpha,beta=vol3(M)
assert np.allclose(sv[:4],0.5)
assert np.all(sv[4:] < 1e-10)
assert abs(Z-1/16)<1e-12
assert np.allclose(alpha,3/m)
assert np.allclose(beta,3/m)

A=hub_square(m)
ev=np.linalg.eigvalsh(A)
nz=ev[np.abs(ev)>1e-9]
assert np.allclose(nz,[-1,1,1])
W=Wrs(A)
target=np.array([0,(m-1)**2/m**2,2*(m-1)/m**2,1/m**2],float)
assert np.allclose(W,target)
assert abs(W.sum()-1)<1e-12

C_D=6*math.sqrt(math.e)*2**(2/3)
C_H=3*2**(4/3)
print('m',m)
print('interleaved_singular_values',*[f'{x:.12g}' for x in sv[:4]])
print('Z3',f'{Z:.12g}')
print('row_marginal',f'{alpha[0]:.12g}')
print('D_constant_sigma1',f'{C_D:.12f}')
print('hub_square_nonzero_spectrum',*[f'{x:.12g}' for x in nz])
print('W0_W1_W2_W3',*[f'{x:.12g}' for x in W])
print('H_constant',f'{C_H:.12f}')
print('partner_constant',12)
print('STATUS=PASS')
