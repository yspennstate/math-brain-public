import itertools
import numpy as np

BITS=[np.array([(s>>i)&1 for i in range(3)]) for s in range(8)]
BASIS=[]
for i in range(3):
    E=np.zeros((3,3),complex); E[i,i]=1; BASIS.append(E)
for i,j in [(0,1),(0,2),(1,2)]:
    E=np.zeros((3,3),complex); E[i,j]=E[j,i]=1; BASIS.append(E)
for i,j in [(0,1),(0,2),(1,2)]:
    E=np.zeros((3,3),complex); E[i,j]=1j; E[j,i]=-1j; BASIS.append(E)

def adj(B):
    return B@B-np.trace(B)*B+((np.trace(B)**2-np.trace(B@B))/2)*np.eye(3)

ADJ=np.empty((9,9,3,3),complex)
for i in range(9):
    for j in range(9):
        ADJ[i,j]=adj(BASIS[i]+BASIS[j])-adj(BASIS[i])-adj(BASIS[j])

def frozen(N):
    return np.einsum('ab,ijba->ij',N,ADJ).real

def data(R):
    ws=[]; vs=[]
    for s in range(8):
        ids=np.flatnonzero(BITS[s]); V=np.zeros((3,3),complex)
        if s:
            T=R[np.ix_(ids,ids)]; w=np.linalg.det(T).real
            V[np.ix_(ids,ids)]=np.linalg.inv(T)
        else: w=1.
        ws.append(w); vs.append(np.einsum('ab,jba->j',V,np.array(BASIS)).real)
    return np.array(ws),np.array(vs)

def coefficients(R):
    ws,vs=data(R)
    co={e:np.zeros((9,9)) for e in itertools.product(range(3),repeat=3)}
    for s in range(8):
        for t in range(s+1,8):
            e=tuple(BITS[s]+BITS[t]); d=vs[s]-vs[t]
            co[e]+=ws[s]*ws[t]*np.outer(d,d)
    c=np.array([-np.log(ws[6]),-np.log(ws[5]),-np.log(ws[3])]); tau=np.log(ws[3]*ws[5]*ws[6]/ws[7])
    E=np.diag(c)
    for i in range(3):
        e=[1,1,1]; e[i]=0; N=np.zeros((3,3)); N[i,i]=c[i]
        co[tuple(e)]-=frozen(N)
        e[i]=2; u=R[:,i]; N=(c[i]+tau)*np.outer(u,np.conj(u))
        co[tuple(e)]-=frozen(N)
    co[(1,1,1)]-=frozen(R@E+E@R+tau*R)
    return co,c,tau

def check(R):
    co,c,tau=coefficients(R)
    vals={e:np.linalg.eigvalsh(m)[0] for e,m in co.items()}
    return vals,c,tau

if __name__=='__main__':
    for vals in [(0.2,0.3,0.1,0.2),(0.5,0.6,0.1,0.4),(0.7,0.6,0.2,0.2),(0.9,0.8,0.65,0.15),(0.1,0.104,0,0.106)]:
        a,b,u,v=vals; R=np.array([[1,a,u-1j*v],[a,1,b],[u+1j*v,b,1]])
        if np.linalg.eigvalsh(R)[0]<=0: continue
        ev,c,tau=check(R)
        print(vals,'Rmin',np.linalg.eigvalsh(R)[0],'c',c,'tau',tau,'111',ev[(1,1,1)],'min',min(ev.values()))
    rng=np.random.default_rng(813)
    worst=(1e99,None)
    good=bad=0
    for _ in range(1000):
        Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); R=Z@Z.conj().T
        d=np.sqrt(np.diag(R).real); R=R/np.outer(d,d)
        ev,c,tau=check(R); m=ev[(1,1,1)]
        if m<worst[0]: worst=(m,R)
        if m>=-1e-9: good+=1
        else: bad+=1
    print('random good bad',good,bad,'worst',worst)
