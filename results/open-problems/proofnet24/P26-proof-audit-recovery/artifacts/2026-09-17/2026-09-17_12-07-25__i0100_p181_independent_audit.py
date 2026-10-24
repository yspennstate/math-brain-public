#!/usr/bin/env python3
import sympy as sp

P=181
SUP=[0,1,6,7,8,9,10,12,13,17,19,20,21,23,24,28,31,34,36,37,41,43,44,45]
EXPECTED_N=[3,4,5,6,7,11,18,19,21,24,25,28,30,31,33,34,36,38,39,40,41,43,45]

def prime_factors(n):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0: n//=d
        d+=1
    if n>1: out.append(n)
    return out

def primitive_root(p):
    fac=prime_factors(p-1)
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in fac): return g
    raise AssertionError

def graph_data(p):
    assert sp.isprime(p) and p%4==1
    n=(p-1)//2
    g=primitive_root(p)
    alpha=pow(g,2,p)
    verts=[pow(alpha,j,p) for j in range(n)]
    Q={x*x%p for x in range(1,p)}
    S={d for d in range(1,n) if (verts[d]-1)%p in Q}
    assert len(S)==(p-5)//4
    assert S=={n-d for d in S}
    N=[d for d in range(1,n//2+1) if d not in S]
    return n,S,N

def qrat(q): return sp.Rational(int(q.numerator),int(q.denominator))

def field_table(n):
    K=sp.QQ.algebraic_field(2*sp.cos(2*sp.pi/n))
    a=K.unit
    C=[K.zero]*(n//2+1); C[0]=2*K.one; C[1]=a
    for m in range(1,n//2): C[m+1]=a*C[m]-C[m-1]
    def cosk(m):
        m%=n; m=min(m,n-m)
        return C[m]/2
    x=sp.Symbol('x')
    mp=sp.Poly.from_list([qrat(c) for c in K.mod.to_list()],x)
    roots=mp.intervals(eps=sp.Rational(1,10**50))
    assert len(roots)==mp.degree() and all(mult==1 for _,mult in roots)
    I=max((iv for iv,_ in roots), key=lambda z:z[0])
    # verify chosen root is the numerical 2cos(2pi/n), not merely some positive conjugate
    target=sp.N(2*sp.cos(2*sp.pi/n),60)
    lo,hi=map(lambda r: sp.N(r,60),I)
    assert lo < target < hi
    return K,cosk,mp,I

def solve_square(A,b,K):
    M=[row[:] + [b[i]] for i,row in enumerate(A)]
    n=len(M)
    for c in range(n):
        r=next(r for r in range(c,n) if M[r][c]!=K.zero)
        M[c],M[r]=M[r],M[c]
        piv=M[c][c]
        M[c]=[z/piv for z in M[c]]
        for r in range(n):
            if r==c: continue
            f=M[r][c]
            if f!=K.zero:
                M[r]=[M[r][j]-f*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def imul(I,J):
    a,b=I;c,d=J; vals=[a*c,a*d,b*c,b*d]; return min(vals),max(vals)

def ieval(coeffs,I):
    out=(sp.Rational(0),sp.Rational(0))
    for c in coeffs:
        lo,hi=imul(out,I); r=qrat(c); out=(lo+r,hi+r)
    return out

def sgn(e,K,I):
    if e==K.zero: return 0
    lo,hi=ieval(e.to_list(),I)
    if lo>0:return 1
    if hi<0:return -1
    raise AssertionError(('unresolved sign',lo,hi))

n,S,N=graph_data(P)
assert n==90 and N==EXPECTED_N and len(SUP)==len(N)+1
K,cosk,mp,I=field_table(n)
# primal for clique-bounding theta(complement H): sum w=1, inverse Fourier zero on nonedges
A=[[K.one for _ in SUP]]+[[cosk(m*d) for m in SUP] for d in N]
w=solve_square(A,[K.one]+[K.zero]*len(N),K)
assert sum(w,K.zero)==K.one
assert all(sgn(x,K,I)>0 for x in w)
for d in N: assert sum((x*cosk(m*d) for x,m in zip(w,SUP)),K.zero)==K.zero
# dual, pinned to equality on the primal support
D=[[K.one]+[cosk(m*d) for d in N] for m in SUP]
y=solve_square(D,[K.one if m==0 else K.zero for m in SUP],K)
a=y[0]; lam=y[1:]
sl=[]
for m in range(n):
    z=a+sum((c*cosk(m*d) for c,d in zip(lam,N)),K.zero)-(K.one if m==0 else K.zero)
    assert sgn(z,K,I)>=0
    sl.append(z)
w0=w[SUP.index(0)]
assert a==w0
assert all(sl[m]==K.zero for m in SUP)
theta=n*w0
print('P26-I0100-P181-INDEPENDENT-EXACT-AUDIT: PASS')
print('p=',P,'n=',n,'degree=',len(S),'nonedge_reps=',len(N),'field_degree=',mp.degree())
print('nonedge_reps_list=',N)
print('support=',SUP)
print('minpoly=',mp.as_expr())
print('positive_primal_weights=',len(w))
print('dual_zero_slacks=',sum(z==K.zero for z in sl),'of',n)
print('objectives_equal_exact=',a==w0)
print('theta_40d=',sp.N(K.to_sympy(theta),40))
print('sqrt_p_over_2_40d=',sp.N(sp.sqrt(sp.Rational(P,2)),40))
print('ratio_40d=',sp.N(K.to_sympy(theta)/sp.sqrt(sp.Rational(P,2)),40))
