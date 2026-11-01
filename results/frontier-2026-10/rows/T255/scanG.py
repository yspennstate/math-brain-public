# generic generator by finite differences; min over random V of drift(log F)/|W|^2 (attention only) for correctors of tr W
import numpy as np
from gen import bdrift, noise_basis
rng=np.random.default_rng(9)
def gen(F,V,g2,eps=1e-4):
    s=np.sqrt(np.sum(V*V)); e=eps*s; f=F(V); b=bdrift(V,g2)
    dfb=(F(V+e*b/np.sqrt(np.sum(b*b)))-F(V-e*b/np.sqrt(np.sum(b*b))))/(2*e)*np.sqrt(np.sum(b*b))
    ito=0; qv=0
    for E in noise_basis(V,g2):
        n=np.sqrt(np.sum(E*E))
        if n==0: continue
        fp=F(V+e*E/n); fm=F(V-e*E/n)
        g=(fp-fm)/(2*e)*n; hh=(fp-2*f+fm)/e**2*n*n
        qv+=g*g; ito+=hh
    return (dfb+0.5*ito)/f-0.5*qv/f**2
m=3; P=np.eye(m)-1.0/m; one=np.ones(m)
def parts(V):
    W=P@V@P; trW=np.trace(W); D=np.diag(W)-trW/m; r=P@V@one; S=one@V@one
    return W,trW,D,r,S
Vs=[]
for _ in range(500):
    A=rng.standard_normal((m,m))@np.diag(np.exp(rng.uniform(-2,1,m))); V=A@A.T
    Vs.append(V+np.exp(rng.uniform(-1,5))*np.outer(one,one)/m+1e-4*np.eye(m))
for g2 in (0.3,):
    for th in (0.0,0.5,1.0,2.0,-1.0):
        def F(V,th=th):
            W,trW,D,r,S=parts(V); return trW+th*(r@D)/trW
        vals=[]
        for V in Vs:
            if F(V)<=0: continue
            W=P@V@P; vals.append(gen(F,V,g2)/np.sum(W*W))
        print("g2",g2,"F=trW+%g r.D/trW"%th,"min %.3f  p1 %.3f  frac<0 %.3f"%(min(vals),np.percentile(vals,1),np.mean(np.array(vals)<0)),flush=True)
