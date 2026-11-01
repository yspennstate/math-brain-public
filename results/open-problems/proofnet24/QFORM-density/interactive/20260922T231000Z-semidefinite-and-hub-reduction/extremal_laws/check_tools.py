try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, time
from q3tools import Law, density, g_partial
U = lambda c=0.0: Law([c-0.5],[c+0.5])
A = np.eye(3); b = np.zeros(3)
laws = [U(),U(),U()]
t0=time.time()
for s in [0.1,0.25,0.3]:
    print("sphere s=",s," quad",density(A,b,s,laws), " exact", (2*np.pi*np.sqrt(s) if s<=0.25 else 3*np.pi-4*np.pi*np.sqrt(s)), flush=True)
print("time",time.time()-t0,flush=True)
# MC check for a random matrix with linear term and a spread law
rng=np.random.default_rng(0)
A = rng.normal(size=(3,3)); A=(A+A.T)/2
b = rng.normal(size=3)
laws = [Law([-0.5],[0.5]), Law([0.0,2.0],[0.4,2.6]), Law([-1.3],[-0.3])]
def sample(law,m):
    seg = rng.choice(len(law.a), size=m, p=(law.b-law.a)/np.sum(law.b-law.a))
    return law.a[seg] + (law.b[seg]-law.a[seg])*rng.random(m)
N=4_000_000
X = np.column_stack([sample(l,N) for l in laws])
Q = np.einsum('ij,jk,ik->i',X,A,X) + X@b
for s in [np.median(Q), np.quantile(Q,0.3)]:
    for i in range(3):
        print("s=%.4f coord %d quad %.5f"%(s,i,density(A,b,s,laws,i=i)),flush=True)
    for w in [0.02,0.01]:
        print("   MC window",w, np.mean(np.abs(Q-s)<w/2)/w, flush=True)
