#!/usr/bin/env python3
"""Independent R19 exact audit of R20/I0100 p=241 finite certificate.

Re-derives the localized Paley nonedge differences from F_241, reconstructs
the active primal/dual LP certificate over Q(2cos(2pi/120)) by modular
embeddings + CRT/rational reconstruction, and verifies exact primal
feasibility, dual feasibility, and objective equality.

This audits only the finite p=241 certificate, not Conjecture 26
asymptotically.
"""
from fractions import Fraction
from math import isqrt,gcd
import sympy as sp
import numpy as np

P=241; N=120; DEG=16
SUPPORT=[0,1,2,4,5,6,10,11,12,13,14,15,16,19,24,28,29,31,33,34,35,38,39,41,45,47,49,50,54,58,60]
EMB=[1,7,11,13,17,19,23,29,31,37,41,43,47,49,53,59]
REPORTED_NEDGES=[5,6,11,12,13,14,16,19,23,27,28,30,32,33,34,36,37,39,40,41,42,43,45,47,48,49,52,53,55,57]
REL={14:16,12:-105,10:364,8:-714,6:784,4:-440,2:96,0:-1}

def legendre(a,p):
    a%=p
    if a==0:return 0
    z=pow(a,(p-1)//2,p)
    return 1 if z==1 else -1

g=sp.primitive_root(P)
NEDGES=[]
for d in range(1,N//2+1):
    if legendre(pow(g,2*d,P)-1,P)<0:
        NEDGES.append(d)
assert NEDGES==REPORTED_NEDGES

x=sp.symbols('x')
MINPOLY=sp.Poly(x**16-16*x**14+105*x**12-364*x**10+714*x**8-784*x**6+440*x**4-96*x**2+1,x)
assert sp.minimal_polynomial(2*sp.cos(2*sp.pi/120),x)==MINPOLY.as_expr()

def solve_mod(A,b,q):
    n=len(A)
    M=np.empty((n,n+1),dtype=np.int64)
    M[:,:n]=np.array(A,dtype=np.int64)%q
    M[:,n]=np.array(b,dtype=np.int64)%q
    for c in range(n):
        nz=np.nonzero(M[c:,c])[0]; assert len(nz)
        piv=c+int(nz[0])
        if piv!=c:M[[c,piv]]=M[[piv,c]]
        inv=pow(int(M[c,c]),q-2,q)
        M[c,:]=(M[c,:]*inv)%q
        fac=M[:,c].copy(); fac[c]=0
        M=(M-fac[:,None]*M[c:c+1,:])%q
    return [int(v) for v in M[:,n]]

def inv_mod(A,q):
    n=len(A)
    M=np.concatenate([np.array(A,dtype=np.int64)%q,np.eye(n,dtype=np.int64)],axis=1)
    for c in range(n):
        nz=np.nonzero(M[c:,c])[0]; assert len(nz)
        piv=c+int(nz[0])
        if piv!=c:M[[c,piv]]=M[[piv,c]]
        inv=pow(int(M[c,c]),q-2,q)
        M[c,:]=(M[c,:]*inv)%q
        fac=M[:,c].copy(); fac[c]=0
        M=(M-fac[:,None]*M[c:c+1,:])%q
    return M[:,n:]

def primes24():
    out=[]; q=1_000_000_000+((1-1_000_000_000)%120)
    while len(out)<24:
        if sp.isprime(q):out.append(int(q))
        q+=120
    return out

def root120(q):
    e=(q-1)//120
    for a in range(2,10000):
        z=pow(a,e,q)
        if z!=1 and all(pow(z,120//r,q)!=1 for r in (2,3,5)):
            return z
    raise AssertionError

def crt_pair(a,m,b,q):
    return a+m*(((b-a)%q)*pow(m%q,q-2,q)%q)

def ratrec(a,m):
    a%=m; B=isqrt(m//2)
    r0,r1=m,a; t0,t1=0,1
    while r1>B:
        q=r0//r1
        r0,r1=r1,r0-q*r1
        t0,t1=t1,t0-q*t1
    num,den=r1,t1
    if den<0:num,den=-num,-den
    d=gcd(abs(num),den); num//=d; den//=d
    assert den and abs(num)<=B and den<=B and (num-a*den)%m==0
    return Fraction(num,den)

R=[[0]*DEG for _ in range(2*len(SUPPORT))]
MOD=1; PRIMES=primes24()
for iq,q in enumerate(PRIMES):
    zeta=root120(q); inv2=(q+1)//2
    aval=[]; values=[]
    for r in EMB:
        def cmod(k):
            kk=(r*k)%N
            return (pow(zeta,kk,q)+pow(zeta,(-kk)%N,q))*inv2%q
        A=[[1]*len(SUPPORT)]+[[cmod(m*d) for m in SUPPORT] for d in NEDGES]
        rhs=[1]+[0]*(len(A)-1)
        w=solve_mod(A,rhs,q)
        y=solve_mod([list(col) for col in zip(*A)],rhs,q)
        values.append(w+y)
        aval.append((pow(zeta,r,q)+pow(zeta,(-r)%N,q))%q)
    V=[[pow(aval[i],j,q) for j in range(DEG)] for i in range(DEG)]
    Vinv=inv_mod(V,q)
    vals=np.array(values,dtype=np.int64)%q
    coeff=[[sum(int(Vinv[i,k])*int(vals[k,j]) for k in range(DEG))%q
            for j in range(vals.shape[1])] for i in range(DEG)]
    if iq==0:
        for j in range(2*len(SUPPORT)):
            for k in range(DEG):R[j][k]=coeff[k][j]
        MOD=q
    else:
        old=MOD
        for j in range(2*len(SUPPORT)):
            for k in range(DEG):
                R[j][k]=crt_pair(R[j][k],old,coeff[k][j],q)
        MOD*=q

EXACT=[[ratrec(R[j][k],MOD) for k in range(DEG)] for j in range(2*len(SUPPORT))]
W=EXACT[:len(SUPPORT)]; Y=EXACT[len(SUPPORT):]

def z():return [Fraction(0) for _ in range(DEG)]
def c(q):
    v=z();v[0]=Fraction(q);return v
def add(a,b):return [a[i]+b[i] for i in range(DEG)]
def sub(a,b):return [a[i]-b[i] for i in range(DEG)]
def scale(a,q):q=Fraction(q);return [q*u for u in a]
def mul(a,b):
    t=[Fraction(0) for _ in range(2*DEG-1)]
    for i,u in enumerate(a):
        if u:
            for j,v in enumerate(b):
                if v:t[i+j]+=u*v
    for k in range(2*DEG-2,DEG-1,-1):
        u=t[k]
        if u:
            t[k]=0;s=k-DEG
            for j,r in REL.items():t[j+s]+=u*r
    return t[:DEG]
def zero(a):return all(u==0 for u in a)
def eq(a,b):return all(a[i]==b[i] for i in range(DEG))
A=z();A[1]=1
C=[None]*(N//2+1);C[0]=c(2);C[1]=A
for m in range(1,N//2):C[m+1]=sub(mul(A,C[m]),C[m-1])
def cosf(k):
    k%=N;k=min(k,N-k)
    return scale(C[k],Fraction(1,2))
def isum(vs):
    s=z()
    for v in vs:s=add(s,v)
    return s

ints=MINPOLY.intervals(eps=sp.Rational(1,10**70))
I=max((iv for iv,mult in ints),key=lambda q:q[0])
def imul(U,V):
    a,b=U;c0,d=V;w=[a*c0,a*d,b*c0,b*d];return min(w),max(w)
def sgn(v):
    if zero(v):return 0
    out=(sp.Rational(0),sp.Rational(0))
    for q in reversed(v):
        out=imul(out,I)
        r=sp.Rational(q.numerator,q.denominator)
        out=(out[0]+r,out[1]+r)
    if out[0]>0:return 1
    if out[1]<0:return -1
    raise AssertionError('sign unresolved')

assert eq(isum(W),c(1))
assert all(sgn(w)>0 for w in W)
for d in NEDGES:
    t=z()
    for m,w in zip(SUPPORT,W):t=add(t,mul(w,cosf(m*d)))
    assert zero(t)

a=Y[0]; lam=Y[1:]; slacks=[]
for m in range(N):
    t=a
    for d,l in zip(NEDGES,lam):t=add(t,mul(l,cosf(m*d)))
    if m==0:t=sub(t,c(1))
    assert sgn(t)>=0
    slacks.append(t)
assert eq(a,W[0])
assert all(zero(slacks[m]) for m in SUPPORT)

theta=scale(W[0],N)
theta_expr=sum(sp.Rational(q.numerator,q.denominator)*x**i for i,q in enumerate(theta))
alpha=2*sp.cos(sp.pi/60)
print('R19 independent audit: R20/I0100 p=241')
print('primitive_root =',g)
print('nonedge_reps =',NEDGES)
print('field_degree =',DEG)
print('CRT_digits =',len(str(MOD)))
print('positive_primal_weights =',sum(sgn(w)>0 for w in W))
print('dual_zero_slacks =',sum(zero(v) for v in slacks))
print('dual_positive_slacks =',sum(sgn(v)>0 for v in slacks))
print('theta_40d =',sp.N(theta_expr.subs(x,alpha),40))
print('ratio_40d =',sp.N(theta_expr.subs(x,alpha)/sp.sqrt(sp.Rational(P,2)),40))
print('PASS_EXACT_FINITE_CASE')
