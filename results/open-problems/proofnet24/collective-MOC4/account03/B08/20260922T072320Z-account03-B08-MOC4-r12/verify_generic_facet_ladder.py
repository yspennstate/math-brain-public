from fractions import Fraction as F
from itertools import permutations

class Q:
    __slots__=("r","i")
    def __init__(self,r=0,i=0):
        self.r=r if isinstance(r,F) else F(r)
        self.i=i if isinstance(i,F) else F(i)
    def __add__(self,o):
        o=o if isinstance(o,Q) else Q(o); return Q(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return Q(-self.r,-self.i)
    def __sub__(self,o): return self+(-(o if isinstance(o,Q) else Q(o)))
    def __rsub__(self,o): return Q(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q) else Q(o)
        return Q(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,Q) else Q(o)
        n=o.r*o.r+o.i*o.i
        return self*Q(o.r/n,-o.i/n)
    def __eq__(self,o):
        o=o if isinstance(o,Q) else Q(o)
        return self.r==o.r and self.i==o.i
    def conj(self): return Q(self.r,-self.i)
    def n2(self): return self.r*self.r+self.i*self.i
    def __repr__(self): return f"({self.r})+({self.i})i"

Z=Q(); O=Q(1)
def eye(n): return [[O if i==j else Z for j in range(n)] for i in range(n)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mul(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Z) for j in range(len(B[0]))] for i in range(len(A))]
def adj(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def diag(v): return [[v[i] if i==j else Z for j in range(len(v))] for i in range(len(v))]
def inv(A):
    n=len(A); E=eye(n); M=[A[i][:]+E[i][:] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c]!=Z)
        if p!=c: M[c],M[p]=M[p],M[c]
        q=M[c][c]; M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r==c: continue
            f=M[r][c]
            if f!=Z: M[r]=[M[r][j]-f*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]
def det(A):
    n=len(A); M=[r[:] for r in A]; out=O; s=1
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=Z),None)
        if p is None: return Z
        if p!=c: M[c],M[p]=M[p],M[c]; s=-s
        q=M[c][c]; out=out*q
        for r in range(c+1,n):
            f=M[r][c]/q
            for j in range(c,n): M[r][j]=M[r][j]-f*M[c][j]
    return out*s
def prod(xs):
    z=O
    for x in xs: z=z*x
    return z
def givens(t,r,s):
    t=F(t); c=(1-t*t)/(1+t*t); ss=2*t/(1+t*t)
    G=eye(4); G[r][r]=Q(c); G[s][s]=Q(c); G[r][s]=Q(ss); G[s][r]=Q(-ss)
    return G
def solve3(A,b):
    M=[A[i][:]+[b[i]] for i in range(3)]
    for c in range(3):
        p=next(r for r in range(c,3) if M[r][c])
        M[c],M[p]=M[p],M[c]
        q=M[c][c]; M[c]=[x/q for x in M[c]]
        for r in range(3):
            if r==c: continue
            f=M[r][c]
            M[r]=[M[r][j]-f*M[c][j] for j in range(4)]
    return [M[i][3] for i in range(3)]

# Original exact dense Cayley unitary from account03/B08 r11.
x=[F(483,50),F(-63,25),F(-72,25),F(-163,50),
   F(33,50),F(23,5),F(-139,25),F(9,25),
   F(-187,50),F(6,5),F(147,50),F(3,10),
   F(31,10),F(-14,25),F(1,50),F(-7,2)]
K=[[Z for _ in range(4)] for _ in range(4)]
for i in range(4): K[i][i]=Q(0,x[i])
t=4
for i in range(4):
    for j in range(i+1,4):
        z=Q(x[t],x[t+1]); t+=2
        K[i][j]=z; K[j][i]=-z.conj()
I=eye(4)
U0=mul(inv(add(I,K)),sub(I,K))
assert mul(U0,adj(U0))==I

a=[Q(18,-17),Q(-20,2),Q(15,-22),Q(-21,2)]
b=[Q(-19,4),Q(25,-5),Q(18,-1),Q(-18,1)]
assert len({(z.r,z.i) for z in a})==4
assert len({(z.r,z.i) for z in b})==4
assert all(a[i]+b[j]!=Z for i in range(4) for j in range(4))

ps=list(permutations(range(4)))
v=[prod([a[i]+b[p[i]] for i in range(4)]) for p in ps]
assert len({(z.r,z.i) for z in v})==24

# Integrity correction: the r11 support direction has a two-vertex top face.
q0=Q(-5782,-19099)
L0=lambda z:(q0*z).r
H0=[L0(z) for z in v]
M0=max(H0)
top0=[ps[k] for k,h in enumerate(H0) if h==M0]
assert M0==F(-61633500)
assert top0==[(0,1,2,3),(0,2,3,1)]

# Remove that degeneracy with a genuinely different common direction.
q=Q(-6032,-19799)
L=lambda z:(q*z).r   # = -6032 Re(z) + 19799 Im(z)
H=[L(z) for z in v]
assert len(set(H))==24
order=sorted(range(24),key=lambda k:H[k],reverse=True)
M=H[order[0]]; m=min(H); sep=M-H[order[1]]
assert ps[order[0]]==(0,2,3,1)  # one-line 1342
assert M==F(-63921000)
assert m==F(-62046835110)
assert sep==F(4261400)

# Five exact rational genuine-unitary pair moves.
U=U0
moves=[
    ("L",1,2,F(73,5000)),
    ("R",0,2,F(19,1000)),
    ("L",1,2,F(71,5000)),
    ("L",0,1,F(-9,1000)),
    ("R",0,2,F(119,10000)),
]
def determinant_of(U):
    return det(add(diag(a),mul(mul(U,diag(b)),adj(U))))
ladder=[L(determinant_of(U))]
for side,r,s,t in moves:
    G=givens(t,r,s)
    U=mul(G,U) if side=="L" else mul(U,G)
    ladder.append(L(determinant_of(U)))
assert all(ladder[j+1]>ladder[j] for j in range(len(ladder)-1))
assert mul(U,adj(U))==I
assert all(z!=Z for row in U for z in row)
pmin=min(z.n2() for row in U for z in row)
assert pmin>F(1,500)

D=determinant_of(U)
gap=M-L(D); width=M-m
assert gap>0
assert gap<sep
assert gap/width < F(1,25000)  # < 4e-5 of full support width

# Exact target-hull rescue by three spectral permutation vertices.
inds=[0,3,8] # 1234, 1342, 2314
lam=solve3([[v[i].r for i in inds],
            [v[i].i for i in inds],
            [F(1),F(1),F(1)]],
           [D.r,D.i,F(1)])
assert all(z>0 for z in lam)
assert sum(lam)==1
assert sum((v[inds[j]]*lam[j] for j in range(3)),Z)==D

# The candidate is not pair-stationary: another exact true-unitary move raises
# the SAME common support while remaining below the target maximum.
Uplus=mul(givens(F(89,10000),1,2),U)
Dplus=determinant_of(Uplus)
improvement=L(Dplus)-L(D)
gapplus=M-L(Dplus)
assert improvement>0
assert gapplus>0

print("PASS MOC4-GENERIC-FACET-LADDER-v1")
print("old_support_top_face=1234,1342")
print("new_support_all_24_distinct=True")
print("new_support_unique_max=1342")
print("support_max=",M,"support_min=",m,"runner_up_separation=",sep)
print("ladder_strict_common_support_improvement=True")
print("ladder_support_gaps=",[M-x for x in ladder])
print("unitary_exact=True")
print("all_16_entries_nonzero=True")
print("pmin_sq_gt_1_over_500=True")
print("support_gap=",gap)
print("normalized_gap=",gap/width,"~",float(gap/width))
print("support_gap_lt_runner_up_separation=True")
print("caratheodory_vertices=1234,1342,2314")
print("caratheodory_weights=",lam)
print("sixth_pair_move_support_improvement=",improvement)
print("sixth_pair_move_still_below_target_max=True")
