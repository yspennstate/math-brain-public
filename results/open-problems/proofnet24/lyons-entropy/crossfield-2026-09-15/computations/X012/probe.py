import numpy as np,itertools
from math import log
rng=np.random.default_rng(1212)
sets=list(itertools.combinations(range(4),2)); signs=[1,-1,1,1,-1,1]
eps=np.array(list(itertools.product([-1,1],repeat=4)))
W=np.array([np.prod(eps[:,S],axis=1) for S in sets]).T

def entropy(v):
    v=np.asarray(v);return -np.dot(v[v>1e-14],np.log(v[v>1e-14]))
def gain(a,b):
    d={S:np.linalg.det(a[list(S)]) for S in sets};e={S:np.linalg.det(b[list(S)]) for S in sets}
    c=np.array([sg*d[S]*e[tuple(i for i in range(4) if i not in S)] for sg,S in zip(signs,sets)])
    p=abs(c)**2;q=abs(W@c)**2/16
    return entropy(q)-entropy(p),p.sum(),c
for field in ['real','complex']:
    best=(1,None)
    for i in range(2000):
        U=rng.normal(size=(4,2));V=rng.normal(size=(4,2))
        if field=='complex':U=U+1j*rng.normal(size=(4,2));V=V+1j*rng.normal(size=(4,2))
        U=np.linalg.qr(U)[0];V=np.linalg.qr(V)[0]
        g,m,c=gain(U,V)
        if g/m<best[0]:best=(g/m,(g,m,c))
    print(field,best)
