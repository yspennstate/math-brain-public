#!/usr/bin/env python3
"""Exact checker for NM13-08 T07 transparent-internal-substitution / neutralizer run.

Checks:
  * symbolic two-terminal substitution cross-Rayleigh factorization;
  * exact K4-join-independent-n port activity formulas from the 15-state transfer;
  * Q_7 activity = 25/7;
  * transparent theta U_l has activity 1;
  * the explicit PF neutralizer B=(4 U_l) series (4 U_l) has activity 16/9;
  * Q_7 series B has activity exactly 1;
  * exact vertex/edge increment formulas for the resulting wheel-expansion family.

All enumerative arithmetic is integer/Fraction arithmetic. Sympy is used only to
verify a universal polynomial identity by exact symbolic expansion.
"""
from itertools import combinations
from fractions import Fraction
import sympy as sp

# ---------- symbolic substitution identity ----------
DA,CA,DAp,CAp,DB,CB,DBr,CBr = sp.symbols('DA CA DAp CAp DB CB DBr CBr')
IA,IAp = DA+CA, DAp+CAp
Z   = DA*CB + IA*DB
Zp  = DAp*CB + IAp*DB
Zr  = DA*CBr + IA*DBr
Zpr = DAp*CBr + IAp*DBr
cross = sp.expand(Zp*Zr - Z*Zpr)
want  = sp.expand((DA*CAp-CA*DAp)*(DB*CBr-CB*DBr))
assert sp.expand(cross-want) == 0
print('SYMBOLIC_CROSS_FACTOR_PASS')

# ---------- Bell(4)=15 transfer for H_n=K4 join independent_n ----------
T = tuple(range(4))
PORT=(0,1)

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks if b),
                        key=lambda b:(b[0],len(b),b)))

def gen_parts(items):
    items=list(items)
    if not items:
        yield (); return
    x=items[0]
    for p in gen_parts(items[1:]):
        yield canon(((x,),)+p)
        for i in range(len(p)):
            q=[set(b) for b in p]
            q[i].add(x)
            yield canon(q)

PARTS=sorted(set(gen_parts(T)), key=lambda p:(-len(p),p))
IDX={p:i for i,p in enumerate(PARTS)}
S=len(PARTS)
assert S==15

def block_index(p,x):
    for i,b in enumerate(p):
        if x in b: return i
    raise AssertionError

def trans(p,A):
    A=set(A)
    ids=[block_index(p,x) for x in A]
    if len(set(ids))!=len(ids): return None
    if len(A)<=1: return p
    ids=set(ids); merged=set(); out=[]
    for i,b in enumerate(p):
        if i in ids: merged.update(b)
        else: out.append(set(b))
    out.append(merged)
    return canon(out)

def zmat(): return [[0]*S for _ in range(S)]
M=zmat()
for a,p in enumerate(PARTS):
    for r in range(5):
        for A in combinations(T,r):
            q=trans(p,A)
            if q is not None:
                M[a][IDX[q]] += 1

def eye():
    A=zmat()
    for i in range(S): A[i][i]=1
    return A

def mmul(A,B):
    C=zmat()
    for i in range(S):
        for k in range(S):
            if A[i][k]:
                for j in range(S):
                    if B[k][j]: C[i][j]+=A[i][k]*B[k][j]
    return C

def madd(A,B,sa=1,sb=1):
    return [[sa*A[i][j]+sb*B[i][j] for j in range(S)] for i in range(S)]

def mpow(A,n):
    R=eye(); B=A
    while n:
        if n&1: R=mmul(R,B)
        B=mmul(B,B); n//=2
    return R

def rowmul(v,A):
    out=[0]*S
    for i,x in enumerate(v):
        if x:
            for j in range(S): out[j]+=x*A[i][j]
    return out

I=eye(); N=madd(M,I,1,-5)
N2=mmul(N,N); N3=mmul(N2,N); N4=mmul(N3,N)
assert any(any(x for x in row) for row in N3)
assert not any(any(x for x in row) for row in N4)
print('TRANSFER_NILPOTENCE_PASS: states=15, M=5I+N, N^4=0')

K4E=list(combinations(T,2))
def part_if_forest(edges,nv=4):
    par=list(range(nv))
    def f(x):
        while par[x]!=x:
            par[x]=par[par[x]]; x=par[x]
        return x
    for a,b in edges:
        a,b=f(a),f(b)
        if a==b: return None
        par[b]=a
    blocks={}
    for x in range(nv): blocks.setdefault(f(x),set()).add(x)
    return canon(blocks.values())

# initial K4 forest vectors according to absence/presence of port 01
v0=[0]*S; v1=[0]*S
for mask in range(1<<len(K4E)):
    es=[K4E[k] for k in range(len(K4E)) if (mask>>k)&1]
    p=part_if_forest(es)
    if p is None: continue
    (v1 if PORT in es else v0)[IDX[p]] += 1

def rowsum(v): return sum(v)
def z_coeffs(n):
    Mn=mpow(M,n)
    # Z_Hn(s)=z0 + s*z1, where z1=D_Qn and z0=I_Qn=D_Qn+C_Qn.
    z0=rowsum(rowmul(v0,Mn))
    z1=rowsum(rowmul(v1,Mn))
    return z0,z1

def D_formula(n): return Fraction(5)**(n-2)*(8*n*n+107*n+350)
def C_formula(n): return Fraction(5)**(n-3)*(16*n**3+247*n*n+1112*n+1250)

for n in range(1,13):
    z0,z1=z_coeffs(n)
    D=z1; C=z0-z1
    assert Fraction(D,1)==D_formula(n)
    assert Fraction(C,1)==C_formula(n)
print('Qn_ACTIVITY_FORMULAS_PASS')
print('D_n = 5^(n-2) * (8 n^2 + 107 n + 350)')
print('C_n = 5^(n-3) * (16 n^3 + 247 n^2 + 1112 n + 1250)')

n=7
D=D_formula(n); C=C_formula(n)
tQ=C/D
assert tQ==Fraction(25,7)
print(f'Q7: D={D}, C={C}, t={tQ}')

# ---------- exact activity neutralization ----------
def par(a,b): return a+b
def ser(a,b): return a*b/(1+a+b)

for ell in range(2,9):
    r=2**ell-1
    t_path=Fraction(1,r)  # length-ell path: C=1, D=2^ell-1
    tU=r*t_path
    assert tU==1
    tP=4*tU
    tB=ser(tP,tP)
    tT=ser(tQ,tB)
    assert tP==4 and tB==Fraction(16,9) and tT==1
    vU=2+r*(ell-1); eU=r*ell
    vP=2+4*r*(ell-1); eP=4*r*ell
    vB=2*vP-1; eB=2*eP
    vT=11+vB-1; eT=33+eB
    assert vT==13+8*r*(ell-1)
    assert eT==33+8*r*ell
    print(f'ell={ell}: U_t=1, P_t=4, B_t={tB}, T_t={tT}, |V(T)|={vT}, |E(T)|={eT}')

# Concrete first expanded wheel W_4 (5 vertices, 8 edges) by one T_2 replacement.
ell=2; r=2**ell-1
vT=13+8*r*(ell-1); eT=33+8*r*ell
V=5+(vT-2); E=8+(eT-1)
assert (V,E)==(40,88)
print(f'W4_ONE_T2_REPLACEMENT: V={V}, E={E}')
print('ALL_EXACT_CHECKS_PASS')
