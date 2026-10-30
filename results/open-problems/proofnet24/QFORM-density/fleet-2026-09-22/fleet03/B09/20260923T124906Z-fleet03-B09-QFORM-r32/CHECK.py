import itertools, math
import numpy as np

rng=np.random.default_rng(20260923)
p=1/4
c=p*(1-p)**3

def ortho(m,r):
    q,_=np.linalg.qr(rng.normal(size=(m,r)))
    return q[:,:r]

def gammas2(C,D):
    N=len(C); g=np.zeros(N)
    for k in range(N):
        cols=[j for j in range(N) if j!=k]
        for J in itertools.combinations(cols,3):
            R=np.vstack([C[list(J),:].T,D[k,list(J)]])
            g[k]+=np.linalg.det(R)**2
    return g

def subweights(C,D,S):
    N=len(C); S=set(S); T=[j for j in range(N) if j not in S]
    w=np.zeros(N)
    for k in S:
        for J in itertools.combinations(T,3):
            R=np.vstack([C[list(J),:].T,D[k,list(J)]])
            w[k]+=np.linalg.det(R)**2
    return w

def physical_subvolume(P,C,D,S):
    N=len(C); H=len(P); S=set(S); T=[j for j in range(N) if j not in S]
    z=0.0
    for a,b in itertools.combinations(range(H),2):
        for k in S:
            for J in itertools.combinations(T,3):
                R=np.vstack([P[[a,b],:]@C[list(J),:].T,D[k,list(J)]])
                z+=np.linalg.det(R)**2
    return z

worst_expect=10.0
worst_max=10.0
worst_factor=0.0
for trial in range(25):
    N=6; H=5
    P=ortho(H,2)
    C=rng.normal(size=(N,2))
    X=rng.normal(size=(N,N)); D=(X+X.T)/2
    g=gammas2(C,D); G=g.sum()
    EW=0.0; maxW=-1.0; best=[]
    for mask in range(1<<N):
        S=[i for i in range(N) if (mask>>i)&1]
        W=subweights(C,D,S).sum()
        prob=(p**len(S))*((1-p)**(N-len(S)))
        EW+=prob*W
        if W>maxW:
            maxW=W; best=S
    worst_expect=min(worst_expect,EW/(c*G))
    worst_max=min(worst_max,maxW/(c*G))
    W=subweights(C,D,best).sum()
    Zphys=physical_subvolume(P,C,D,best)
    worst_factor=max(worst_factor,abs(W-Zphys)/(1+abs(W)))

# target-valid regression
P=np.array([[1/math.sqrt(2),0],[1/math.sqrt(2),0],[0,1/math.sqrt(2)],[0,1/math.sqrt(2)]])
C=np.array([[1.,0.],[0.,1.],[0.,0.],[0.,0.]])
D=np.zeros((4,4)); D[2,3]=D[3,2]=1
B=P@C.T
A=np.block([[np.zeros((4,4)),B],[B.T,D]])
evals=np.linalg.eigvalsh(A)
g=gammas2(C,D); G=g.sum()
S=[2]; T=[0,1,3]
M=np.vstack([P@C[T,:].T,D[np.ix_(S,T)]])
K=M[[0,2,4],:]
detK=np.linalg.det(K)
partner=3*abs(detK)**(-1/3)
mainC=3*math.e*(512/27)**(1/6)

print('c =',repr(c))
print('min exact-expectation ratio EW/(c G) =',repr(worst_expect))
print('min max-cut ratio maxW/(c G) =',repr(worst_max))
print('max relative physical-factorization error =',repr(worst_factor))
print('regression eigenvalues =',np.array2string(evals,precision=12))
print('regression Gamma_k^2 =',np.array2string(g,precision=12))
print('regression G =',repr(float(G)))
print('regression physical det K =',repr(float(detK)))
print('fleet04/B09 partner bound =',repr(partner))
print('main theorem constant 3e(512/27)^(1/6) =',repr(mainC))

assert abs(worst_expect-1)<1e-12
assert worst_max>=1-1e-12
assert worst_factor<1e-12
assert np.sum(np.abs(evals)>=1-1e-10)>=6
assert np.allclose(g,[0,0,1,1],atol=1e-12)
assert abs(detK-0.5)<1e-12
print('ALL CHECKS PASSED')
