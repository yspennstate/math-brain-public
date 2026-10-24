#!/usr/bin/env python3
# Exact self-checks for HARD10-01 new-method run.
from itertools import combinations

# Tiny polynomial helper in variables D,C,De,Ce represented by monomial exponents.
def add(P,Q):
    R=P.copy()
    for k,v in Q.items(): R[k]=R.get(k,0)+v
    return {k:v for k,v in R.items() if v}
def mul(P,Q):
    R={}
    for a,x in P.items():
        for b,y in Q.items():
            k=tuple(a[i]+b[i] for i in range(4)); R[k]=R.get(k,0)+x*y
    return {k:v for k,v in R.items() if v}
def scale(P,c): return {k:c*v for k,v in P.items() if c*v}
def var(i):
    e=[0]*4;e[i]=1;return {tuple(e):1}
D,C,De,Ce=[var(i) for i in range(4)]

def lin(*terms):
    R={}
    for c,P in terms:R=add(R,scale(P,c))
    return R

def sub(P,Q): return add(P,scale(Q,-1))

# Pure subdivision x-z-y.
Z=lin((4,D),(3,C)); Za=lin((2,D),(1,C)); Ze=lin((4,De),(3,Ce)); Zea=lin((2,De),(1,Ce))
Delta=sub(mul(Ze,Za),mul(Z,Zea))
target=scale(sub(mul(D,Ce),mul(C,De)),2)
assert Delta==target
Zab=D
Delta_ab=sub(mul(Za,Za),mul(Z,Zab))
target_ab=mul(C,add(C,D))
assert Delta_ab==target_ab

# Triangle extension: keep g=xy and add x-z-y.
Zt=lin((7,D),(3,C)); Zta=lin((3,D),(1,C)); Zte=lin((7,De),(3,Ce)); Ztea=lin((3,De),(1,Ce))
Delta_t=sub(mul(Zte,Zta),mul(Zt,Ztea))
assert Delta_t==target
Delta_tab=sub(mul(Zta,Zta),mul(Zt,D))
target_tab=mul(add(D,C),add(scale(D,2),C))
assert Delta_tab==target_tab
# pair (path edge, direct edge g): 2 D^2
Zg=scale(D,3); Zag=D
assert sub(mul(Zta,Zg),mul(Zt,Zag))==scale(mul(D,D),2)

# Exact forest routines for the archived B15 near-miss.
class DSU:
    def __init__(self,n): self.p=list(range(n)); self.r=[0]*n
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]];x=self.p[x]
        return x
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b:return False
        if self.r[a]<self.r[b]:a,b=b,a
        self.p[b]=a
        if self.r[a]==self.r[b]:self.r[a]+=1
        return True
    def copy(self):
        q=DSU(len(self.p));q.p=self.p[:];q.r=self.r[:];return q

def five_counts(H,e,f,n=10):
    c=[0,0,0,0,0] # n0,ne,nf,B,R
    Rm=[]
    for mask in range(1<<len(H)):
        d=DSU(n);ok=True
        for i,(u,v) in enumerate(H):
            if mask>>i&1 and not d.union(u,v):ok=False;break
        if not ok:continue
        ae=d.find(e[0])!=d.find(e[1]); af=d.find(f[0])!=d.find(f[1])
        if not ae and not af:c[0]+=1
        elif ae and not af:c[1]+=1
        elif not ae and af:c[2]+=1
        else:
            d2=d.copy();d2.union(*e)
            if d2.find(f[0])!=d2.find(f[1]):c[3]+=1
            else:c[4]+=1;Rm.append(mask)
    return tuple(c),Rm

def terminal_counts(edges,term,marked,n=10):
    D=C=De=Ce=0; mi=edges.index(marked)
    for mask in range(1<<len(edges)):
        d=DSU(n);ok=True
        for i,(u,v) in enumerate(edges):
            if mask>>i&1 and not d.union(u,v):ok=False;break
        if not ok:continue
        conn=d.find(term[0])==d.find(term[1]); has=bool(mask>>mi&1)
        if conn:C+=1
        else:D+=1
        if has:
            if conn:Ce+=1
            else:De+=1
    return D,C,De,Ce

H=[(0,5),(0,8),(1,5),(1,8),(2,5),(2,6),(2,7),(3,6),(4,5),(4,7),(4,9),(5,6),(5,7),(5,8),(5,9),(6,7),(8,9)]
e=(0,1);f=(2,3)
fc,Rm=five_counts(H,e,f)
assert fc==(4552,6266,9816,13538,4)
n0,ne,nf,B,R=fc
Delta5=ne*nf + R*(ne+nf+B+R)-B*n0
assert Delta5==576
# With actual separator h=2-6 removed, A and B share terminals {2,6}.
A=[x for x in H+[e,f] if 3 not in x and x!=(2,6)]
Bs=[f,(3,6)]
DA,CA,DAe,CAe=terminal_counts(A,(2,6),e)
DB,CB,DBf,CBf=terminal_counts(Bs,(2,6),f)
facA=DA*CAe-CA*DAe; facB=DB*CBf-CB*DBf
assert (DA,CA,DAe,CAe)==(9904,7184,3634,2636)
assert (DB,CB,DBf,CBf)==(3,1,1,1)
assert (facA,facB,facA*facB)==(288,2,576)

print('SYMBOLIC_INTEGER_IDENTITY_CHECKS PASS')
print('degree2 pure: Delta(e,a)=2(D Ce-C De); Delta(a,b)=C(C+D); old-pair field lambda=1/3, scale=9')
print('degree2 triangle: Delta(e,a)=2(D Ce-C De); Delta(a,b)=(D+C)(2D+C); Delta(a,g)=2D^2; A-old-pair field lambda=4/3, scale=9')
print('B15 five classes n0,ne,nf,B,R=',fc)
print('B15 five-class terms: B*n0=',B*n0,' ne*nf=',ne*nf,' R_rescue=',R*(ne+nf+B+R),' Delta=',Delta5)
print('B15 R_masks=',','.join(map(str,Rm)))
print('B15 2cut A counts D,C,De,Ce=',(DA,CA,DAe,CAe),'factor=',facA)
print('B15 2cut B counts D,C,Df,Cf=',(DB,CB,DBf,CBf),'factor=',facB)
print('B15 Delta=factorA*factorB=',facA*facB)
print('ALL EXACT SELF-CHECKS PASS')
