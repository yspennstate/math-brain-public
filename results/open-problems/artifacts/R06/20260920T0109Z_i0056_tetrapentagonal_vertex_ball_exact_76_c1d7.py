from collections import deque, Counter, defaultdict
from fractions import Fraction

# Exact arithmetic in Q(sqrt(2),sqrt(5)) using dyadic basis
# (a0 + a2*sqrt(2) + a5*sqrt(5) + a10*sqrt(10))/2^e.
def _norm(c,e):
    c=tuple(int(x) for x in c); e=int(e)
    if c==(0,0,0,0):
        return c,0
    while e>0 and all((x & 1)==0 for x in c):
        c=tuple(x//2 for x in c); e-=1
    return c,e

class D:
    __slots__=('c','e')
    def __init__(self,c=(0,0,0,0),e=0):
        self.c,self.e=_norm(c,e)
    def __add__(self,o):
        if not isinstance(o,D): o=D((o,0,0,0))
        if self.e==o.e:
            return D(tuple(a+b for a,b in zip(self.c,o.c)),self.e)
        E=max(self.e,o.e)
        a=1<<(E-self.e); b=1<<(E-o.e)
        return D(tuple(a*x+b*y for x,y in zip(self.c,o.c)),E)
    __radd__=__add__
    def __neg__(self): return D(tuple(-x for x in self.c),self.e)
    def __sub__(self,o): return self+(-o if isinstance(o,D) else -D((o,0,0,0)))
    def __rsub__(self,o): return D((o,0,0,0))-self
    def __mul__(self,o):
        if not isinstance(o,D): o=D((o,0,0,0))
        a0,a2,a5,a10=self.c; b0,b2,b5,b10=o.c
        return D((
            a0*b0+2*a2*b2+5*a5*b5+10*a10*b10,
            a0*b2+a2*b0+5*(a5*b10+a10*b5),
            a0*b5+a5*b0+2*(a2*b10+a10*b2),
            a0*b10+a10*b0+a2*b5+a5*b2,
        ), self.e+o.e)
    __rmul__=__mul__
    def __eq__(self,o):
        if not isinstance(o,D): o=D((o,0,0,0))
        return self.c==o.c and self.e==o.e
    def __hash__(self): return hash((self.c,self.e))
    def __repr__(self): return f"D{self.c}/2^{self.e}"

Z=D(); ONE=D((1,0,0,0)); SQ2=D((0,1,0,0)); SQ5=D((0,0,1,0)); SQ10=D((0,0,0,1))
PHI=D((1,0,1,0),1)

def mm(A,B):
    out=[]
    for i in range(3):
        row=[]
        for j in range(3):
            s=Z
            for k in range(3): s=s+A[i][k]*B[k][j]
            row.append(s)
        out.append(tuple(row))
    return tuple(out)

def mv(A,v):
    out=[]
    for i in range(3):
        s=Z
        for k in range(3): s=s+A[i][k]*v[k]
        out.append(s)
    return tuple(out)

def mpow(A,n):
    x=ID
    for _ in range(n): x=mm(A,x)
    return x

ID=tuple(tuple(ONE if i==j else Z for j in range(3)) for i in range(3))
# Coxeter [4,5] simple reflections in simple-root coordinates.
S1=((-ONE,SQ2,Z),(Z,ONE,Z),(Z,Z,ONE))
S2=((ONE,Z,Z),(SQ2,-ONE,PHI),(Z,Z,ONE))
S3=((ONE,Z,Z),(Z,ONE,Z),(Z,PHI,-ONE))
assert mm(S1,S1)==ID and mm(S2,S2)==ID and mm(S3,S3)==ID
assert mpow(mm(S1,S2),4)==ID
assert mpow(mm(S2,S3),5)==ID
assert mpow(mm(S1,S3),2)==ID
# No smaller positive powers for the noncommuting dihedral products.
assert all(mpow(mm(S1,S2),j)!=ID for j in range(1,4))
assert all(mpow(mm(S2,S3),j)!=ID for j in range(1,5))

# Coxeter Gram form: angles pi/4, pi/5, pi/2.  Its leading
# principal minors are 1 and 1/2, while det=(1-sqrt(5))/8<0,
# so it has signature (2,1), i.e. this is the hyperbolic [4,5] model.
C4=D((0,1,0,0),1)              # sqrt(2)/2
C5=D((1,0,1,0),2)              # (1+sqrt(5))/4 = cos(pi/5)
GRAM=((ONE,-C4,Z),(-C4,ONE,-C5),(Z,-C5,ONE))
def mt(A): return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))
for S in (S1,S2,S3):
    assert mm(mt(S),mm(GRAM,S))==GRAM
DET_GRAM=(ONE-SQ5)*D((1,0,0,0),3)
# Direct 3x3 determinant check for this tridiagonal Gram matrix.
assert ONE-C4*C4-C5*C5==DET_GRAM
assert (ONE-C4*C4)==D((1,0,0,0),1)

# Vertex p of {4,5} fixed by S2,S3. Scaling is irrelevant.
P=(D((0,5,0,-1),3), ONE, D((1,0,1,0),2))
assert mv(S2,P)==P and mv(S3,P)==P
R=mm(S2,S3)
assert mpow(R,5)==ID

# Five neighbors of a {4,5} vertex: R^k S1 p, k=0,...,4.
STEPS=[]
rk=ID
for _ in range(5):
    STEPS.append(mm(rk,S1)); rk=mm(R,rk)
assert len(set(mv(g,P) for g in STEPS))==5

MAX_R=10
rep={P:ID}; dist={P:0}; order={}
q=deque([P])
while q:
    v=q.popleft(); d=dist[v]; G=rep[v]
    inc=[]
    for g in STEPS:
        H=mm(G,g); w=mv(H,P); inc.append(w)
        if w not in dist and d<MAX_R:
            dist[w]=d+1; rep[w]=H; q.append(w)
    order[v]=tuple(inc)

r_shell=Counter(dist.values())
expected_r=[1,5,15,40,105,275,720,1885,4935,12920,33825]
assert [r_shell[i] for i in range(MAX_R+1)]==expected_r

# Medial graph T=M({4,5}). Its vertices are undirected R-edges; around
# each primal degree-5 vertex, consecutive incident edges are adjacent in T.
def edgekey(u,v): return frozenset((u,v))
Tadj=defaultdict(set)
for v,inc in order.items():
    es=[edgekey(v,w) for w in inc]
    for i in range(5):
        a,b=es[i],es[(i+1)%5]
        Tadj[a].add(b); Tadj[b].add(a)

base=edgekey(P,order[P][0])
MAX_T=10
tdist={base:0}; q=deque([base])
while q:
    e=q.popleft(); d=tdist[e]
    if d>=MAX_T: continue
    for f in Tadj[e]:
        if f not in tdist:
            tdist[f]=d+1; q.append(f)

t_shell=Counter(tdist.values())
expected_t=[1,4,10,20,38,70,130,240,446,824,1528]
assert [t_shell[i] for i in range(MAX_T+1)]==expected_t
# Every vertex needed to determine the radius-9 ball and its entire outer
# boundary has its full degree 4 visible in this exact development.
assert all(len(Tadj[e])==4 for e,d in tdist.items() if d<=9)

B9={e for e,d in tdist.items() if d<=9}
outer={f for e in B9 for f in Tadj[e] if f not in B9}
S10={e for e,d in tdist.items() if d==10}
assert outer==S10
assert len(B9)==1783 and len(outer)==1528
ratio=Fraction(len(outer),len(B9))
assert ratio==Fraction(1528,1783)
# Strict improvement over the previous upper bound 2/sqrt(5), checked
# without floating point by squaring positive quantities.
assert 5*1528*1528 < 4*1783*1783

print("EXACT_COXETER_RELATIONS_PASS")
print("R_SHELLS_0_TO_10", expected_r)
print("T_SHELLS_0_TO_10", expected_t)
print("T_RADIUS9_BALL", len(B9))
print("T_RADIUS9_OUTER_VERTEX_BOUNDARY", len(outer))
print("T_RADIUS9_RATIO", f"{ratio.numerator}/{ratio.denominator}")
print("STRICTLY_BELOW_2_OVER_SQRT5_INTEGER_MARGIN", 4*1783*1783-5*1528*1528)
print("ALL_EXACT_CHECKS_PASS")
