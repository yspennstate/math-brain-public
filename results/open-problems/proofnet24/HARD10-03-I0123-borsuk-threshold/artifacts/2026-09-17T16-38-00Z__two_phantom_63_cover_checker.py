from itertools import product, combinations
from collections import deque, Counter
POLY=0b10011

def mul(a,b):
    z=0
    while b:
        if b&1: z ^= a
        b >>= 1; a <<= 1
        if a&16: a ^= POLY
    return z&15

def pw(a,e):
    z=1
    while e:
        if e&1: z=mul(z,a)
        a=mul(a,a); e>>=1
    return z
INV=[0]*16
for a in range(1,16): INV[a]=pw(a,14)
def norm(v):
    for a in v:
        if a:
            ia=INV[a]; return tuple(mul(ia,x) for x in v)
    raise ValueError
def add(u,v): return tuple(a^b for a,b in zip(u,v))
def scale(a,u): return tuple(mul(a,x) for x in u)
def h(u,v): return mul(u[0],pw(v[0],4)) ^ mul(u[1],pw(v[1],4)) ^ mul(u[2],pw(v[2],4))
def line(u,v): return {norm(add(scale(a,u),scale(b,v))) for a,b in product(range(16),repeat=2) if a or b}
pts=sorted({norm(v) for v in product(range(16),repeat=3) if v!=(0,0,0)})
iso=[p for p in pts if h(p,p)==0]; non=[p for p in pts if h(p,p)!=0]
orth=[[False]*208 for _ in range(208)]
for i in range(208):
    for j in range(i+1,208):
        if h(non[i],non[j])==0: orth[i][j]=orth[j][i]=True
verts=[t for t in combinations(range(208),3) if orth[t[0]][t[1]] and orth[t[0]][t[2]] and orth[t[1]][t[2]]]
ix={p:i for i,p in enumerate(iso)}; tm=[]
for t in verts:
    s=set()
    for i,j in combinations(t,2): s.update(p for p in line(non[i],non[j]) if p in ix)
    tm.append(sum(1<<ix[p] for p in s))
adj=[0]*416
for i in range(416):
    for j in range(i+1,416):
        if (tm[i]&tm[j]).bit_count()==3:
            adj[i]|=1<<j; adj[j]|=1<<i

def split(q):
    B=[v for v,t in enumerate(verts) if any(h(non[i],q)==0 for i in t)]
    bm=sum(1<<v for v in B); seen=set(); comps=[]
    for r in B:
        if r in seen: continue
        seen.add(r); Q=deque([r]); c=[]
        while Q:
            v=Q.popleft(); c.append(v); y=adj[v]&bm
            while y:
                b=y&-y; w=b.bit_length()-1; y^=b
                if w not in seen: seen.add(w); Q.append(w)
        comps.append(frozenset(c))
    comps=sorted(comps,key=lambda c:min(c)); return frozenset(B),comps
B0,C0=split(iso[0])
POS3=[0,35,80,82,86,97,122,127,131,135,149,154,157,167,178,196,197,204,214,223,235,250,270,276,291,297,305,308,309,311,316,321,324,326,339,342,343,349,357,364,365,371,389,392,407,409,410,415]
NEG3=[11,17,70,72,74,79,88,91,102,106,108,120,121,125,145,146,164,169,175,180,190,194,198,205,209,211,224,227,229,242,245,258,265,269,274,301,307,313,328,331,358,363,366,367,382,385,386,394]
supp3=set(POS3)|set(NEG3); Z=set(B0)|supp3; S=sorted(set(range(416))-Z)
PARTS=[(177,201,231,296,361),(54,128,213,295,303),(45,129,199,277,387),(25,31,236,243,372),(182,191,306,334,405),(8,206,322,377,400),(49,62,100,161,375),(5,113,212,283,286),(153,160,188,332,373),(4,57,90,105,294),(123,139,168,271,397),(3,40,166,218,259),(81,96,155,185,351),(124,288,329,335,378),(58,184,359,370,388),(55,163,300,327,347),(42,48,203,207,369),(16,51,262,315,403),(20,32,156,251,350),(27,33,63,87,323),(1,24,44,238,396),(13,36,181,290,395),(6,19,189,220,393),(67,152,162,266,383),(46,89,147,312,330),(10,12,221,379,391),(64,142,234,319,413),(21,93,115,159,402),(65,94,289,304,376),(14,71,101,252,257),(38,53,76,109,302),(75,85,111,151,233),(69,148,170,193,267),(95,143,248,356,362),(28,41,174,346,408),(18,83,273,337,390),(133,141,210,237,411),(73,78,173,226,336),(2,30,99,287,406),(37,138,254,285,341),(56,279,292,325,368),(61,140,232,255,340),(183,244,278,320,355),(192,200,260,263,298),(104,110,215,261,360),(9,50,132,353,401),(134,202,228,310,354),(107,114,172,246,314),(60,103,165,225,284),(39,137,253,380,412),(26,77,92,208,268),(7,47,52,150,187),(22,59),(136,384),(217,317),(15,68,144),(34,158,338),(43,66,249),(126,186,398),(171,280,414),(264,272,404),(176,216,219,230)]

from fractions import Fraction
from math import isqrt

def eigen20(v):
    for x in range(416):
        y=adj[x]; tot=0
        while y:
            b=y&-y; z=b.bit_length()-1; y^=b; tot += v[z]
        if tot != 20*v[x]: return False
    return True
u1=[0]*416; u2=[0]*416; u3=[0]*416
for x in C0[0]: u1[x]=1; u2[x]=1
for x in C0[1]: u1[x]=-1
for x in C0[2]: u2[x]=-1
for x in POS3: u3[x]=1
for x in NEG3: u3[x]=-1
assert eigen20(u1) and eigen20(u2) and eigen20(u3)
U=[u1,u2,u3]
G=[[sum(U[a][i]*U[b][i] for i in range(416)) for b in range(3)] for a in range(3)]
assert G==[[64,32,48],[32,64,0],[48,0,96]]
Gi=[[Fraction(1,24),Fraction(-1,48),Fraction(-1,48)],
    [Fraction(-1,48),Fraction(5,192),Fraction(1,96)],
    [Fraction(-1,48),Fraction(1,96),Fraction(1,48)]]
for a in range(3):
    for b in range(3):
        assert sum(Fraction(G[a][c])*Gi[c][b] for c in range(3)) == Fraction(int(a==b))

def bil(w,z):
    return sum(Fraction(w[a])*Gi[a][b]*Fraction(z[b]) for a in range(3) for b in range(3))
def Ein(i,j):
    if i==j: return Fraction(5,32)
    return Fraction(1,32) if ((adj[i]>>j)&1) else Fraction(-1,96)
ws={i:tuple(U[a][i] for a in range(3)) for i in Z}
qs={i:Ein(i,i)-bil(ws[i],ws[i]) for i in Z}
assert Counter(qs.values())==Counter({Fraction(25,192):64,Fraction(13,96):64})
def rij(i,j): return Ein(i,j)-bil(ws[i],ws[j])

# Pure-rational interval arithmetic proving the sign of the phantom-pair diameter criterion.
# q=25/192 => mu=(-2+sqrt(854))/25; q=13/96 => mu=(-1+sqrt(222))/13.
D=10**8
def sqrt_iv(n):
    a=isqrt(n*D*D)
    return (Fraction(a,D),Fraction(a+1,D))
def add_iv(x,y): return (x[0]+y[0],x[1]+y[1])
def mul_iv(x,y):
    vals=[x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1]]
    return (min(vals),max(vals))
def scale_iv(c,x):
    return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def sub_const(x,c): return (x[0]-c,x[1]-c)
s854=sqrt_iv(854); s222=sqrt_iv(222)
muA=((s854[0]-2)/25,(s854[1]-2)/25)
muB=((s222[0]-1)/13,(s222[1]-1)/13)
assert muA[0]>0 and muB[0]>0

def mu_iv(q):
    if q==Fraction(25,192): return muA
    assert q==Fraction(13,96); return muB

def pair_F_iv(i,j):
    # D_ij <= 1/3 iff F:=mu_i+mu_j+96*r_ij*mu_i*mu_j-1 >=0.
    mi,mj=mu_iv(qs[i]),mu_iv(qs[j])
    z=add_iv(mi,mj)
    z=add_iv(z,scale_iv(96*rij(i,j),mul_iv(mi,mj)))
    return sub_const(z,Fraction(1))

def pair_compatible(i,j):
    z=pair_F_iv(i,j)
    assert z[0]>0 or z[1]<0, (i,j,z,qs[i],qs[j],rij(i,j))
    return z[0]>0

flat=[v for P in PARTS for v in P]
assert len(PARTS)==62 and len(flat)==288 and len(set(flat))==288 and set(flat)==set(S)
for P in PARTS:
    for a,b in combinations(P,2): assert (adj[a]>>b)&1

def safe_pc(p,v): return bool((adj[p]>>v)&1)
def local_two_cover(P,p,q):
    items=list(P)+[('p',p),('q',q)]
    n=len(items); full=(1<<n)-1
    def safe(a,b):
        at=isinstance(a,tuple); bt=isinstance(b,tuple)
        if at and bt: return True  # invoked only for a diameter-compatible phantom pair
        if at: return safe_pc(a[1],b)
        if bt: return safe_pc(b[1],a)
        return bool((adj[a]>>b)&1)
    def clique(mask):
        I=[i for i in range(n) if (mask>>i)&1]
        return all(safe(items[i],items[j]) for i,j in combinations(I,2))
    if clique(full): return (full,0)
    for m in range(1,full):
        if not (m&1): continue
        if clique(m) and clique(full^m): return (m,full^m)
    return None

pair_type_counts=Counter(); compatible=0; witness_parts=Counter()
for i,j in combinations(sorted(Z),2):
    qa,qb=qs[i],qs[j]
    if qa>qb: qa,qb=qb,qa
    pair_type_counts[(qa,qb,rij(i,j))]+=1
    if not pair_compatible(i,j):
        continue
    compatible += 1
    witness=None
    for pidx,P in enumerate(PARTS):
        splitmask=local_two_cover(P,i,j)
        if splitmask is not None:
            witness=(pidx,splitmask); break
    assert witness is not None, (i,j,qs[i],qs[j],rij(i,j))
    witness_parts[witness[0]] += 1

assert sum(pair_type_counts.values())==8128
assert len(pair_type_counts)==12
assert compatible==6272
assert sum(witness_parts.values())==6272

print('I0123_TWO_PHANTOM_63_COVER_PASS')
print('core: 288 vertices, pinned exact clique partition=62 parts')
print('deleted sources:',len(Z),'projection-norm classes=',dict(Counter(str(q) for q in qs.values())))
print('phantom source pairs:',8128,'diameter-compatible=',compatible,'exact pair types=',len(pair_type_counts))
print('all',compatible,'diameter-compatible two-phantom extensions admit a <=63-clique cover')
print('mechanism: replace one of the pinned 62 core cliques by at most two augmented cliques; other 61 core cliques unchanged')
print('conclusion: no diameter-compatible two-phantom extension of THIS fixed 288-point rank-62 core, using the source projection/rescaling phantom construction, is a Borsuk counterexample in R^62')
