#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt, gcd
import sympy as sp
import numpy as np

P=241
N=120
NEDGES=[5,6,11,12,13,14,16,19,23,27,28,30,32,33,34,36,37,39,40,41,42,43,45,47,48,49,52,53,55,57]
SUPPORT=[0,1,2,4,5,6,10,11,12,13,14,15,16,19,24,28,29,31,33,34,35,38,39,41,45,47,49,50,54,58,60]
EMB=[1,7,11,13,17,19,23,29,31,37,41,43,47,49,53,59]
DEG=16
REL={14:16,12:-105,10:364,8:-714,6:784,4:-440,2:96,0:-1}

# Symmetry-reduced source-normalized theta LP.
# Primal: max N*w_0, sum w=1, cosine moments vanish on localized nonedges, w>=0.
# Dual: min N*a, a + sum_d lambda_d cos(2*pi*m*d/N) >= 1_{m=0}.
# The support was found numerically; everything below reconstructs and verifies the
# matching certificate with exact arithmetic.

def solve_mod(A,B,q):
    n=len(A)
    M=np.array([[(x%q) for x in A[i]]+[(x%q) for x in B[i]] for i in range(n)],dtype=np.int64)
    for c in range(n):
        nz=np.nonzero(M[c:,c])[0]
        if len(nz)==0: raise AssertionError('singular mod prime')
        piv=c+int(nz[0])
        if piv!=c: M[[c,piv]]=M[[piv,c]]
        inv=pow(int(M[c,c]),q-2,q)
        M[c,:]=(M[c,:]*inv)%q
        factors=M[:,c].copy(); factors[c]=0
        # q<1e9+2e4, hence every product fits in signed int64.
        M=(M-factors[:,None]*M[c:c+1,:])%q
    return M[:,n:].tolist()

def matmul(A,B,q):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%q for j in range(len(B[0]))] for i in range(len(A))]

def prime_stream(count=24,start=1_000_000_000):
    out=[]
    q=start+((1-start)%120)
    while len(out)<count:
        if sp.isprime(q): out.append(int(q))
        q+=120
    return out

def root120(q):
    expo=(q-1)//120
    for aa in range(2,10000):
        z=pow(aa,expo,q)
        if z!=1 and all(pow(z,120//r,q)!=1 for r in (2,3,5)):
            return z
    raise AssertionError('no order-120 root found')

def crt_pair(a,m,b,q):
    return a+m*(((b-a)%q)*pow(m%q,q-2,q)%q)

def rat_reconstruct(a,m):
    a%=m; B=isqrt(m//2)
    r0,r1=m,a; t0,t1=0,1
    while r1>B:
        qq=r0//r1
        r0,r1=r1,r0-qq*r1
        t0,t1=t1,t0-qq*t1
    num,den=r1,t1
    if den<0:num,den=-num,-den
    g=gcd(abs(num),den); num//=g; den//=g
    if den==0 or abs(num)>B or den>B or (num-a*den)%m:
        raise ValueError('rational reconstruction failed')
    return Fraction(num,den)

# Exact arithmetic in Q(alpha), alpha=2*cos(2*pi/120), degree 16.
def fzero(): return [Fraction(0) for _ in range(DEG)]
def fconst(c):
    v=fzero(); v[0]=Fraction(c); return v
def fadd(a,b): return [a[i]+b[i] for i in range(DEG)]
def fsub(a,b): return [a[i]-b[i] for i in range(DEG)]
def fscale(a,c): return [x*Fraction(c) for x in a]
def fmul(a,b):
    tmp=[Fraction(0) for _ in range(2*DEG-1)]
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: tmp[i+j]+=x*y
    for k in range(2*DEG-2,DEG-1,-1):
        c=tmp[k]
        if c:
            tmp[k]=0; sh=k-DEG
            for j,r in REL.items(): tmp[j+sh]+=c*r
    return tmp[:DEG]
def feq(a,b): return all(a[i]==b[i] for i in range(DEG))
def fiszero(a): return all(x==0 for x in a)
ALPHA=fzero(); ALPHA[1]=Fraction(1)

def build_cos_table():
    C=[None]*(N//2+1); C[0]=fconst(2); C[1]=ALPHA
    for m in range(1,N//2): C[m+1]=fsub(fmul(ALPHA,C[m]),C[m-1])
    return C
CT=build_cos_table()
def cosF(k):
    k%=N; k=min(k,N-k)
    return fscale(CT[k],Fraction(1,2))

def isolating_interval():
    x=sp.Symbol('x')
    poly=sp.Poly(x**16-16*x**14+105*x**12-364*x**10+714*x**8-784*x**6+440*x**4-96*x**2+1,x)
    ints=poly.intervals(eps=sp.Rational(1,10**75))
    assert len(ints)==16 and all(mult==1 for _,mult in ints)
    return max((iv for iv,_ in ints),key=lambda t:t[0])
ROOTI=isolating_interval()
def imul(I,J):
    a,b=I;c,d=J; vals=[a*c,a*d,b*c,b*d]; return min(vals),max(vals)
def signF(v):
    if fiszero(v): return 0
    I=(sp.Rational(ROOTI[0]),sp.Rational(ROOTI[1])); out=(sp.Rational(0),sp.Rational(0))
    for c in reversed(v):
        out=imul(out,I); q=sp.Rational(c.numerator,c.denominator); out=(out[0]+q,out[1]+q)
    if out[0]>0:return 1
    if out[1]<0:return -1
    raise AssertionError('exact sign interval contains zero')

def sum_field(vals):
    s=fzero()
    for v in vals:s=fadd(s,v)
    return s

def reconstruct():
    R=[[0]*DEG for _ in range(2*len(SUPPORT))]; M=1
    primes=prime_stream()
    for qi,q in enumerate(primes):
        zeta=root120(q); inv2=(q+1)//2; aval=[]; values=[]
        for r in EMB:
            def cmod(k):
                kk=(r*k)%N
                return (pow(zeta,kk,q)+pow(zeta,(-kk)%N,q))*inv2%q
            A=[[1]*len(SUPPORT)]+[[cmod(m*d) for m in SUPPORT] for d in NEDGES]
            rhs=[[1] if i==0 else [0] for i in range(len(A))]
            w=[row[0] for row in solve_mod(A,rhs,q)]
            AT=[list(col) for col in zip(*A)]
            y=[row[0] for row in solve_mod(AT,rhs,q)]
            values.append(w+y)
            aval.append((pow(zeta,r,q)+pow(zeta,(-r)%N,q))%q)
        V=[[pow(aval[i],j,q) for j in range(DEG)] for i in range(DEG)]
        Vinv=solve_mod(V,[[1 if i==j else 0 for j in range(DEG)] for i in range(DEG)],q)
        coeff=matmul(Vinv,values,q)
        if qi==0:
            for j in range(2*len(SUPPORT)):
                for k in range(DEG): R[j][k]=coeff[k][j]
            M=q
        else:
            oldM=M
            for j in range(2*len(SUPPORT)):
                for k in range(DEG): R[j][k]=crt_pair(R[j][k],oldM,coeff[k][j],q)
            M*=q
    exact=[[rat_reconstruct(R[j][k],M) for k in range(DEG)] for j in range(2*len(SUPPORT))]
    return exact[:len(SUPPORT)],exact[len(SUPPORT):],M,primes

def main():
    assert sp.isprime(P) and P%4==1 and len(NEDGES)+1==len(SUPPORT)
    W,Y,M,primes=reconstruct()
    assert feq(sum_field(W),fconst(1))
    assert all(signF(v)>0 for v in W)
    for d in NEDGES:
        acc=fzero()
        for m,w in zip(SUPPORT,W): acc=fadd(acc,fmul(w,cosF(m*d)))
        assert fiszero(acc)
    a=Y[0]; lam=Y[1:]; slacks=[]
    for m in range(N):
        lhs=a
        for d,l in zip(NEDGES,lam): lhs=fadd(lhs,fmul(l,cosF(m*d)))
        if m==0: lhs=fsub(lhs,fconst(1))
        assert signF(lhs)>=0; slacks.append(lhs)
    assert feq(a,W[0])
    assert all(fiszero(slacks[m]) for m in SUPPORT)
    theta=fscale(W[0],N)
    x=sp.Symbol('x'); alpha_expr=2*sp.cos(sp.pi/60)
    theta_expr=sum(sp.Rational(c.numerator,c.denominator)*x**i for i,c in enumerate(theta))
    print('I0100 / Randomstrasse Conjecture 26 exact p=241 certificate')
    print('p =',P,'n =',N,'field_degree =',DEG)
    print('nonedge_difference_reps =',NEDGES)
    print('primal_support =',SUPPORT)
    print('reconstruction_primes =',primes)
    print('CRT_modulus_decimal_digits =',len(str(M)))
    print('field_minpoly = x^16 - 16*x^14 + 105*x^12 - 364*x^10 + 714*x^8 - 784*x^6 + 440*x^4 - 96*x^2 + 1')
    print('strict_positive_primal_weights =',len(W))
    print('dual_zero_slacks =',sum(fiszero(s) for s in slacks),'of',N)
    print('dual_positive_slacks =',sum(signF(s)>0 for s in slacks),'of',N)
    print('dual_a_equals_w0 =',feq(a,W[0]))
    print('theta_numeric_40d =',sp.N(theta_expr.subs(x,alpha_expr),40))
    print('sqrt(p/2)_numeric_40d =',sp.N(sp.sqrt(sp.Rational(P,2)),40))
    print('ratio_numeric_40d =',sp.N(theta_expr.subs(x,alpha_expr)/sp.sqrt(sp.Rational(P,2)),40))
    print('covered_primes_before = [5, 13, 17, 29, 41, 181]')
    print('covered_primes_after = [5, 13, 17, 29, 41, 181, 241]')
    print('largest_exact_prime = 241')
    print('PASS: exact primal feasibility, exact dual feasibility, exact objective equality')
if __name__=='__main__': main()
