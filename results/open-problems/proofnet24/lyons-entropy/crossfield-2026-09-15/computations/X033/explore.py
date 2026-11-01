import numpy as np
from itertools import product

rng=np.random.default_rng(33033)
bits=np.array(list(product((0,1),repeat=3)))
def atoms(K):
    return np.array([((-1)**int(3-x.sum())*np.linalg.det(K-np.diag(1-x))).real for x in bits])
def stats(K):
    p=atoms(K); f=-np.log(p)
    c=np.array([f[3]-f[1]-f[2]+f[0],f[5]-f[1]-f[4]+f[0],f[6]-f[2]-f[4]+f[0]])
    tau=f[7]-f[6]-f[5]-f[3]+f[4]+f[2]+f[1]-f[0]
    M=np.diag(c)+tau*K
    As=[]
    for i,j in ((0,1),(0,2),(1,2)):
        for v in (1,1j):
            A=np.zeros((3,3),complex);A[i,j]=v;A[j,i]=np.conj(v);As.append(A)
    def Q(A):
        adj=A@A-np.trace(A)*A+(np.trace(A)**2-np.trace(A@A))/2*np.eye(3)
        return (2*np.trace(M@adj)).real
    F=np.array([[(Q(A+B)-Q(A)-Q(B))/2 for B in As] for A in As])
    d=np.diag(K).real; cov=np.diag(d)-abs(K)**2
    kapp=[]
    for e in (0,7):
        b=p[e]*(bits[e]-d)
        var=p[e]*(1-p[e])-b@np.linalg.solve(cov,b)
        kapp.append(var/p[e])
    return p,tau,M,np.linalg.eigvalsh(F),kapp

maxfr=(-1e99,None); bad=None; extreme=(-1,None)
for rep in range(1000):
    Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); U=np.linalg.qr(Z)[0]
    eig=1/(1+np.exp(-rng.uniform(-7,7,3)))
    K=(U*eig)@U.conj().T
    p,tau,M,ev,kappa=stats(K)
    if ev[-1]>maxfr[0]: maxfr=(ev[-1],(K,tau,ev,kappa))
    if abs(tau)*kappa[1 if tau>=0 else 0]>extreme[0]: extreme=(abs(tau)*kappa[1 if tau>=0 else 0],(K,tau,kappa))
    As=[]
    for i,j in ((0,1),(0,2),(1,2)):
        for v in (1,1j):
            A=np.zeros((3,3),complex);A[i,j]=v;A[j,i]=np.conj(v);As.append(A)
    T=K if tau>0 else np.eye(3)-K
    def qf(A): return (np.trace(T@(A@A-np.trace(A@A)/2*np.eye(3)))).real
    F=np.array([[(qf(A+B)-qf(A)-qf(B))/2 for B in As] for A in As])
    ew,ev=np.linalg.eigh(F)
    if ew[-1]>1e-7 and abs(tau)<2:
        A=sum(v*B for v,B in zip(ev[:,-1],As))
        adj=A@A-np.trace(A@A)/2*np.eye(3); q=-np.trace(K@adj).real
        bad=(K,A,tau,q,kappa);break
print('max frozen eigenvalue',maxfr)
print('max |tau|kappa',extreme)
print('outside acceleration cone with adverse sign',bad)
