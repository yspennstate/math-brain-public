# Independent exact check of K7P sections 2 and 3 (my own hitting solves, sympy rationals).
import sympy as sp
def hit(Wm, target):
    n=Wm.shape[0]; deg=[sum(Wm[i,:]) for i in range(n)]
    # E_x T_target ; loops counted once in degree
    idx=[i for i in range(n) if i!=target]
    A=sp.zeros(len(idx)); b=sp.ones(len(idx),1)
    for r,i in enumerate(idx):
        A[r,r]=1
        for c,j in enumerate(idx):
            A[r,c]-=Wm[i,j]/deg[i]
    x=A.LUsolve(b); h=[0]*n
    for r,i in enumerate(idx): h[i]=sp.nsimplify(x[r])
    return h,deg
def Fmat(Wm):
    n=Wm.shape[0]; F=sp.zeros(n)
    for j in range(n):
        h,deg=hit(Wm,j); Wt=sum(deg); Epi=sum(deg[i]*h[i] for i in range(n))/Wt
        for i in range(n): F[i,j]=sp.simplify(h[i]-Epi)
    return F
def quot(Wm, blocks):
    k=len(blocks); Q=sp.zeros(k)
    for a,B in enumerate(blocks):
        for b,C in enumerate(blocks):
            s=sum(Wm[i,j] for i in B for j in C)
            Q[a,b]= s if a!=b else (2*sum(Wm[i,j] for i in B for j in B if i<j)+sum(Wm[i,i] for i in B))
    return Q
def fam(t):
    W=sp.zeros(4); a,b,u,v=0,1,2,3
    W[a,u]=W[u,a]=1; W[b,u]=W[u,b]=1; W[u,v]=W[v,u]=t**2; W[a,a]=t-1; W[b,b]=t-1; W[v,v]=t**6
    return W
for t in [2,3,10]:
    W=fam(t); F=Fmat(W); T=max(F)
    Wt=t**6+2*t**2+2*t+2; N=t**7+t**6+2*t**5+2*t**4+2*t**3+t**2+4*t+2
    Q=quot(W,[[0],[1],[2,3]]); Fh=Fmat(Q)
    aa=Fh[0,0]-F[0,0]
    print('t',t,'T==N/W',sp.simplify(T-sp.Rational(N,Wt))==0,'a_a==formula',sp.simplify(aa-sp.Rational(t**2*(t**4+1)**2,Wt))==0,'a_a/T',float(aa/T),'Fhat max/T',float(max(Fh)/T))
# Section 3 sequential example at t=10
t=10; W6=sp.zeros(6); W6[:4,:4]=fam(t); e=sp.Rational(1,10**6)
for x in (4,5): W6[3,x]=W6[x,3]=e
F=Fmat(W6); T=max(F); ta=max(F[0,:]); tb=max(F[1,:])
Q1=quot(W6,[[0],[1],[2,3],[4],[5]]); F1=Fmat(Q1)
print('seq: t1a+t1b',max(F1[0,:])+max(F1[1,:]),'claimed',sp.Rational(10002120000039,250055500001))
print('seq: ta+tb+T',ta+tb+T,'claimed',sp.Rational(229169325000879,6251387500025))
Q2=quot(W6,[[0],[1],[2,3],[4,5]]); F2=Fmat(Q2)
print('seq final: max Fhat/T',float(max(F2)/T),'Fhat_ab/T',float(F2[0,1]/T))
