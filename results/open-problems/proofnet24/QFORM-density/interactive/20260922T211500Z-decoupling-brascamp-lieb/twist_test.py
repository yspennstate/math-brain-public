try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np
rng=np.random.default_rng(5)
def draw(law,S,n,starts=None,w=None):
    if law=='unif': return rng.uniform(-.5,.5,(S,n))
    idx=rng.integers(0,starts.shape[1],(S,n)); U=rng.uniform(0,w,(S,n))
    return starts[np.arange(n),idx]+U
n=60; S=400000
v=np.ones(n)/np.sqrt(n)
G=rng.standard_normal((n,n)); E=(G+G.T)/np.sqrt(2*n)
P=np.eye(n)-np.outer(v,v); E=P@E@P; E/=np.linalg.norm(E,2)          # dense, ||E||=1, E v = 0
us=np.linspace(-40,40,801); du=us[1]-us[0]
for law in ['unif','spread']:
    starts=w=None
    if law=='spread':
        Nint=6; w=1.0/Nint; starts=np.sort(rng.uniform(0,8,(n,Nint)),axis=1)
    X=draw(law,S,n,starts,w); X=X-X.mean(0)
    L=X@v; R=np.einsum('ij,jk,ik->i',X,E,X)
    for t in [0.0,0.5,2.0,8.0,32.0,128.0]:
        tw=np.exp(1j*t*R)
        vals=np.array([abs(np.mean(np.exp(1j*u*L)*tw)) for u in us])
        I=vals.sum()*du; floor=(1/np.sqrt(S))*(us[-1]-us[0])
        print(f"{law:6s} t={t:6.1f}  int|Psi(u,t)|du = {I:7.3f}  (MC floor ~{floor:.2f})  |E e^(itR)|={abs(tw.mean()):.3f}")
