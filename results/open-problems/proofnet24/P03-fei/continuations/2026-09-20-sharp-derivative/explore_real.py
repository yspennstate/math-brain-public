import numpy as np,json
from scipy.optimize import minimize
from explore_derivative import fwht,entropy
rng=np.random.default_rng(20260921)
def calc(a):
    a=a/np.linalg.norm(a); N=len(a); n=N.bit_length()-1
    p=a*a; H=entropy(p); I=np.dot(p,[x.bit_count() for x in range(N)])
    g=fwht(a); labels=np.arange(N)
    der=g[None,:]*g[np.bitwise_xor(labels[:,None],labels[None,:])]
    b=fwht(der)/N
    joint=b*b/N; z=joint.sum(axis=1)
    hc=entropy(joint.ravel())-entropy(z)
    return (2*H-hc)/I if I>1e-14 else 0,2*H-hc,I,a,z
best=(0,None)
for n in range(1,6):
    N=1<<n
    for k in range(80):
        a=rng.normal(size=N)
        if k%2:a[0]*=20
        sol=minimize(lambda a:-calc(a)[0],a,method='BFGS',options={'maxiter':100,'gtol':1e-7})
        r,D,I,b,z=calc(sol.x)
        if r>best[0]:best=(r,{'n':n,'a':b.tolist(),'D':D,'I':I,'z':z.tolist()})
    print('real',n,best[0],flush=True)
    if best[0]>4.000001:break
print(json.dumps({'best':best},indent=2))
