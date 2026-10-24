from itertools import product, combinations
from collections import deque, Counter
from fractions import Fraction
from math import isqrt

# Exact GF(16) model for G_2(4), following the already-certified I0123 reconstruction.
POLY=0b10011
def mul(a,b):
    z=0
    while b:
        if b&1: z ^= a
        b >>= 1
        a <<= 1
        if a&16: a ^= POLY
    return z&15
def pw(a,e):
    z=1
    while e:
        if e&1: z=mul(z,a)
        a=mul(a,a); e>>=1
    return z
def inv_table():
    out=[0]*16
    for a in range(1,16): out[a]=pw(a,14)
    return out
INV=inv_table()
def norm(v):
    for a in v:
        if a:
            ia=INV[a]
            return tuple(mul(ia,x) for x in v)
    raise ValueError
def add(u,v): return tuple(a^b for a,b in zip(u,v))
def scale(a,u): return tuple(mul(a,x) for x in u)
def h(u,v):
    return mul(u[0],pw(v[0],4)) ^ mul(u[1],pw(v[1],4)) ^ mul(u[2],pw(v[2],4))
def line(u,v):
    return {norm(add(scale(a,u),scale(b,v))) for a,b in product(range(16),repeat=2) if a or b}

pts=sorted({norm(v) for v in product(range(16),repeat=3) if v!=(0,0,0)})
iso=[p for p in pts if h(p,p)==0]
non=[p for p in pts if h(p,p)!=0]
assert (len(pts),len(iso),len(non))==(273,65,208)
orth=[[False]*208 for _ in range(208)]
for i in range(208):
    for j in range(i+1,208):
        if h(non[i],non[j])==0: orth[i][j]=orth[j][i]=True
verts=[t for t in combinations(range(208),3) if orth[t[0]][t[1]] and orth[t[0]][t[2]] and orth[t[1]][t[2]]]
assert len(verts)==416
ix={p:i for i,p in enumerate(iso)}
tm=[]
for t in verts:
    s=set()
    for i,j in combinations(t,2): s.update(p for p in line(non[i],non[j]) if p in ix)
    tm.append(sum(1<<ix[p] for p in s))
adj=[0]*416
for i in range(416):
    for j in range(i+1,416):
        if (tm[i]&tm[j]).bit_count()==3:
            adj[i]|=1<<j; adj[j]|=1<<i
assert set(x.bit_count() for x in adj)=={100}

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
    comps=sorted(comps,key=lambda c:min(c))
    return frozenset(B),comps

B0,C0=split(iso[0])
assert len(B0)==96 and [len(c) for c in C0]==[32,32,32]
POS3=[0,35,80,82,86,97,122,127,131,135,149,154,157,167,178,196,197,204,214,223,235,250,270,276,291,297,305,308,309,311,316,321,324,326,339,342,343,349,357,364,365,371,389,392,407,409,410,415]
NEG3=[11,17,70,72,74,79,88,91,102,106,108,120,121,125,145,146,164,169,175,180,190,194,198,205,209,211,224,227,229,242,245,258,265,269,274,301,307,313,328,331,358,363,366,367,382,385,386,394]
supp3=set(POS3)|set(NEG3); Z=set(B0)|supp3; S=sorted(set(range(416))-Z)
assert (len(Z),len(S))==(128,288)

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

# Exact rational intervals for the two phantom scales.
D=10**10
def sqrt_iv(n):
    a=isqrt(n*D*D)
    return (Fraction(a,D),Fraction(a+1,D))
def add_iv(x,y): return (x[0]+y[0],x[1]+y[1])
def mul_iv(x,y):
    vals=[x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1]]
    return (min(vals),max(vals))
def scale_iv(c,x): return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def sub_const(x,c): return (x[0]-c,x[1]-c)
s854=sqrt_iv(854); s222=sqrt_iv(222)
muA=((s854[0]-2)/25,(s854[1]-2)/25)
muB=((s222[0]-1)/13,(s222[1]-1)/13)
assert muA[0]>0 and muB[0]>0
def mu_iv(q):
    if q==Fraction(25,192): return muA
    assert q==Fraction(13,96); return muB
def pair_F_iv(i,j):
    mi,mj=mu_iv(qs[i]),mu_iv(qs[j]); z=add_iv(mi,mj)
    z=add_iv(z,scale_iv(96*rij(i,j),mul_iv(mi,mj)))
    return sub_const(z,Fraction(1))
def pair_compatible(i,j):
    z=pair_F_iv(i,j)
    assert z[0]>0 or z[1]<0, (i,j,z,qs[i],qs[j],rij(i,j))
    return z[0]>0

# Core near graph: a clique is a strictly-smaller-diameter subset.
pos={v:k for k,v in enumerate(S)}; Smask=sum(1<<v for v in S); core_adj=[0]*len(S)
for a,v in enumerate(S):
    y=adj[v]&Smask; m=0
    while y:
        b=y&-y; w=b.bit_length()-1; y^=b; m |= 1<<pos[w]
    core_adj[a]=m

def has_core_clique(mask,k):
    if k==0: return True
    if mask.bit_count()<k: return False
    while mask:
        if mask.bit_count()<k: return False
        b=mask&-mask; v=b.bit_length()-1; mask^=b
        if has_core_clique(mask & core_adj[v],k-1): return True
    return False
allcore=(1<<len(S))-1
assert has_core_clique(allcore,5)
assert not has_core_clique(allcore,6)

Zs=sorted(Z); p_nmask={}
for i in Zs:
    m=0
    for a,v in enumerate(S):
        if (adj[i]>>v)&1: m |= 1<<a
    p_nmask[i]=m
assert all(not has_core_clique(p_nmask[i],5) for i in Zs)

# H is the necessary coexistence graph for any diameter-preserving batch with alpha<=5.
pindex={v:k for k,v in enumerate(Zs)}; H=[0]*len(Zs)
compatible=0; pair_obstruction=0
for i,j in combinations(Zs,2):
    if not pair_compatible(i,j): continue
    compatible += 1
    if has_core_clique(p_nmask[i]&p_nmask[j],4):
        pair_obstruction += 1
        continue
    a,b=pindex[i],pindex[j]; H[a]|=1<<b; H[b]|=1<<a
assert compatible==6272
assert pair_obstruction==4352
assert sum(x.bit_count() for x in H)//2==1920
assert min(x.bit_count() for x in H)==20 and max(x.bit_count() for x in H)==36

def count_k_cliques(k):
    count=0; witness=None
    def rec(P,depth,chosen):
        nonlocal count,witness
        need=k-depth
        if need==0:
            count += 1
            if witness is None: witness=tuple(chosen)
            return
        while P:
            if P.bit_count()<need: return
            b=P&-P; v=b.bit_length()-1; P^=b
            rec(P & H[v],depth+1,chosen+[v])
    rec((1<<len(H))-1,0,[])
    return count,witness
c3,w3=count_k_cliques(3); c4,w4=count_k_cliques(4); c5,w5=count_k_cliques(5); c6,w6=count_k_cliques(6)
assert (c3,c4,c5,c6)==(8960,14720,4608,0)
assert w5 is not None and w6 is None
w5_sources=tuple(Zs[v] for v in w5)

print('I0123_BATCH_PHANTOM_NO_GO_PASS')
print('core_size=288 phantom_sources=128')
print('diameter_compatible_pairs=6272')
print('compatible_pairs_with_core_K4_obstruction=4352')
print('obstruction_preserving_pair_edges=1920 degree_range=(20,36)')
print('H clique counts: K3=%d K4=%d K5=%d K6=%d' % (c3,c4,c5,c6))
print('example_H_K5_sources=',w5_sources)
print('EXACT_CONCLUSION: every diameter-preserving phantom batch with augmented diameter-graph independence number <=5 has size <=5')
print('THEREFORE: the required |P|>=28 batch for the 316-point counting route does not exist in this fixed 128-phantom family')
