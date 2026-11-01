# Independent exact audit for R20/I0100 p=181 certificate.
# Reconstructs localized Paley nonedges and exact primal/dual LP certificate
# from the support reported in R20, without importing R20's checker.
import sympy as sp

p=181
n=(p-1)//2
support=[0,1,6,7,8,9,10,12,13,17,19,20,21,23,24,28,31,34,36,37,41,43,44,45]
N_expected=[3,4,5,6,7,11,18,19,21,24,25,28,30,31,33,34,36,38,39,40,41,43,45]

def prime_factors(n):
    fs=[]; d=2
    while d*d<=n:
        if n%d==0:
            fs.append(d)
            while n%d==0: n//=d
        d+=1
    if n>1: fs.append(n)
    return fs

g=None
for cand in range(2,p):
    if all(pow(cand,(p-1)//q,p)!=1 for q in prime_factors(p-1)):
        g=cand; break
assert g is not None
alpha=pow(g,2,p)
Q={x*x%p for x in range(1,p)}
verts=[pow(alpha,j,p) for j in range(n)]
S={d for d in range(1,n) if (verts[d]-1)%p in Q}
N=[d for d in range(1,n//2+1) if d not in S]
assert N==N_expected
assert len(S)==44

x=sp.symbols('x')
theta=2*sp.cos(2*sp.pi/n)
mp=sp.Poly(sp.minimal_polynomial(theta,x),x)
expected=sp.Poly(x**12 - 12*x**10 + x**9 + 54*x**8 - 9*x**7 - 112*x**6 + 27*x**5 + 105*x**4 -31*x**3 -36*x**2 +12*x +1,x)
assert mp == expected

K=sp.QQ.algebraic_field(theta)
aK=K.unit
C=[K.zero]*(n//2+1); C[0]=2*K.one; C[1]=aK
for m in range(1,n//2): C[m+1]=aK*C[m]-C[m-1]
def cosK(m):
    m%=n; m=min(m,n-m); return C[m]/2

def solve(A,b):
    A=[list(row)+[b[i]] for i,row in enumerate(A)]; M=len(A)
    for j in range(M):
        pivot=next(i for i in range(j,M) if A[i][j]!=K.zero)
        A[j],A[pivot]=A[pivot],A[j]
        piv=A[j][j]; A[j]=[v/piv for v in A[j]]
        for i in range(M):
            if i==j: continue
            c=A[i][j]
            if c!=K.zero: A[i]=[A[i][k]-c*A[j][k] for k in range(M+1)]
    return [A[i][-1] for i in range(M)]

P=[[K.one]*len(support)] + [[cosK(m*d) for m in support] for d in N]
w=solve(P,[K.one]+[K.zero]*len(N))
D=[[K.one]+[cosK(m*d) for d in N] for m in support]
dual=solve(D,[K.one if m==0 else K.zero for m in support])
aa=dual[0]; lam=dual[1:]
assert sum(w,K.zero)==K.one
for d in N: assert sum((wi*cosK(m*d) for wi,m in zip(w,support)),K.zero)==K.zero
w0=w[0]; assert aa==w0

intervals=mp.intervals(eps=sp.Rational(1,10**50))
I=max((iv for iv,mult in intervals), key=lambda ab: ab[0])
def rat(q): return sp.Rational(int(q.numerator),int(q.denominator))
def mul_int(A,B):
    vals=[A[0]*B[0],A[0]*B[1],A[1]*B[0],A[1]*B[1]]
    return min(vals),max(vals)
def eval_interval(e):
    acc=(sp.Rational(0),sp.Rational(0))
    for coeff in e.to_list():
        acc=mul_int(acc,I); q=rat(coeff); acc=(acc[0]+q,acc[1]+q)
    return acc
def sgn(e):
    if e==K.zero: return 0
    J=eval_interval(e)
    if J[0]>0:return 1
    if J[1]<0:return -1
    raise AssertionError(('unresolved sign',J))

assert all(sgn(wi)>0 for wi in w)
slacks=[]
for m in range(n):
    lhs=aa+sum((ld*cosK(m*d) for ld,d in zip(lam,N)),K.zero)
    sl=lhs-(K.one if m==0 else K.zero)
    assert sgn(sl)>=0; slacks.append(sl)
assert all(slacks[m]==K.zero for m in support)
Theta=n*w0
print('R19 independent exact audit R20-I0100 p=181')
print('primitive_root',g,'residue_generator',alpha)
print('nonedge_reps',N)
print('minpoly',mp.as_expr())
print('positive_primal_weights',len(w))
print('dual_zero_slacks',sum(sl==K.zero for sl in slacks),'of',n)
print('theta',sp.N(K.to_sympy(Theta),40))
print('PASS_EXACT_P181')
