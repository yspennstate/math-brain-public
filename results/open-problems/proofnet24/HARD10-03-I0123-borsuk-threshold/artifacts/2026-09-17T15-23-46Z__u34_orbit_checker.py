from itertools import product, combinations, permutations
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
for a in range(1,16):
    INV[a]=pw(a,14)
    assert mul(a,INV[a])==1
def norm(v):
    for a in v:
        if a:
            ia=INV[a]
            return tuple(mul(ia,x) for x in v)
    raise ValueError("zero")
def add(u,v): return tuple(a^b for a,b in zip(u,v))
def scale(a,u): return tuple(mul(a,x) for x in u)
def h(u,v): return mul(u[0],pw(v[0],4)) ^ mul(u[1],pw(v[1],4)) ^ mul(u[2],pw(v[2],4))
def line(u,v):
    return {norm(add(scale(a,u),scale(b,v)))
            for a,b in product(range(16),repeat=2) if a or b}
def mat_vec(cols,v):
    out=[0,0,0]
    for j in range(3):
        for i in range(3):
            out[i] ^= mul(cols[j][i],v[j])
    return tuple(out)

pts=sorted({norm(v) for v in product(range(16),repeat=3) if v!=(0,0,0)})
iso=[p for p in pts if h(p,p)==0]
non=[p for p in pts if h(p,p)!=0]
assert (len(pts),len(iso),len(non))==(273,65,208)

orth=[[False]*208 for _ in range(208)]
for i in range(208):
    for j in range(i+1,208):
        if h(non[i],non[j])==0:
            orth[i][j]=orth[j][i]=True
verts=[t for t in combinations(range(208),3)
       if orth[t[0]][t[1]] and orth[t[0]][t[2]] and orth[t[1]][t[2]]]
assert len(verts)==416

ix={p:i for i,p in enumerate(iso)}
tm=[]
for t in verts:
    s=set()
    for i,j in combinations(t,2):
        s.update(p for p in line(non[i],non[j]) if p in ix)
    assert len(s)==15
    tm.append(sum(1<<ix[p] for p in s))
adj=[0]*416
for i in range(416):
    for j in range(i+1,416):
        if (tm[i]&tm[j]).bit_count()==3:
            adj[i]|=1<<j; adj[j]|=1<<i
assert {x.bit_count() for x in adj}=={100}

def eigen20(v):
    for x in range(416):
        y=adj[x]; tot=0
        while y:
            b=y&-y; z=b.bit_length()-1; y^=b
            tot += v[z]
        if tot != 20*v[x]: return False
    return True

def split(q):
    B=[v for v,t in enumerate(verts) if any(h(non[i],q)==0 for i in t)]
    bm=sum(1<<v for v in B)
    seen=set(); comps=[]
    for r in B:
        if r in seen: continue
        seen.add(r); Q=deque([r]); c=[]
        while Q:
            v=Q.popleft(); c.append(v); y=adj[v]&bm
            while y:
                b=y&-y; w=b.bit_length()-1; y^=b
                if w not in seen:
                    seen.add(w); Q.append(w)
        comps.append(frozenset(c))
    comps=sorted(comps,key=lambda c:min(c))
    assert sorted(map(len,comps))==[32,32,32]
    return frozenset(B),comps

B0,C0=split(iso[0])
u1=[0]*416; u2=[0]*416
for x in C0[0]: u1[x]=1; u2[x]=1
for x in C0[1]: u1[x]=-1
for x in C0[2]: u2[x]=-1
assert eigen20(u1) and eigen20(u2)

POS3=[0,35,80,82,86,97,122,127,131,135,149,154,157,167,178,196,197,204,214,223,235,250,270,276,291,297,305,308,309,311,316,321,324,326,339,342,343,349,357,364,365,371,389,392,407,409,410,415]
NEG3=[11,17,70,72,74,79,88,91,102,106,108,120,121,125,145,146,164,169,175,180,190,194,198,205,209,211,224,227,229,242,245,258,265,269,274,301,307,313,328,331,358,363,366,367,382,385,386,394]
u3=[0]*416
for x in POS3: u3[x]=1
for x in NEG3: u3[x]=-1
assert eigen20(u3)
supp3=frozenset(i for i,x in enumerate(u3) if x)
assert len(supp3)==96
assert len(supp3 & B0)==64
assert len(B0 | supp3)==128

scal_to_one={}
for val in {h(p,p) for p in non}:
    for a in range(1,16):
        if mul(pw(a,5),val)==1:
            scal_to_one[val]=a; break
assert set(scal_to_one)=={1,6,7}
norm1=[a for a in range(1,16) if pw(a,5)==1]
assert len(norm1)==5

# Each graph vertex is an unordered orthogonal projective basis.  Ordering it
# and choosing two relative norm-one phases gives every projective unitary map.
fullM={}
for t in verts:
    base=[]
    for idx in t:
        p=non[idx]
        base.append(scale(scal_to_one[h(p,p)],p))
    for order in permutations(range(3)):
        cols0=[base[k] for k in order]
        for d1 in norm1:
            for d2 in norm1:
                cols=(cols0[0],scale(d1,cols0[1]),scale(d2,cols0[2]))
                for i in range(3):
                    for j in range(3):
                        assert h(cols[i],cols[j])==(1 if i==j else 0)
                fullM[cols]=cols
assert len(fullM)==62400

non_index={p:i for i,p in enumerate(non)}
vert_index={tuple(sorted(t)):i for i,t in enumerate(verts)}
def map_vertex(vi,cols):
    tt=[]
    for ni in verts[vi]:
        q=norm(mat_vec(cols,non[ni]))
        tt.append(non_index[q])
    return vert_index[tuple(sorted(tt))]
def map_set(S,cols):
    return frozenset(map_vertex(v,cols) for v in S)

q0=iso[0]
stab=[cols for cols in fullM.values() if norm(mat_vec(cols,q0))==q0]
assert len(stab)==960

stab_supps={map_set(supp3,M) for M in stab}
stab_deletions={frozenset(B0 | S) for S in stab_supps}
assert len(stab_supps)==60
assert len(stab_deletions)==30
assert {len(Z) for Z in stab_deletions}=={128}

# One coset representative for each of the 65 isotropic images of q0.
reps={}
for M in fullM.values():
    q=norm(mat_vec(M,q0))
    reps.setdefault(q,M)
assert len(reps)==65

orbit=set()
for M in reps.values():
    for S in stab_supps:
        orbit.add(map_set(S,M))
assert len(orbit)==3900
intersection_hist=Counter(len(S & B0) for S in orbit)
assert intersection_hist==Counter({22:2880,20:960,64:60})

near={S for S in orbit if len(S&B0)==64}
assert near==stab_supps
near_deletions={frozenset(B0|S) for S in near}
assert near_deletions==stab_deletions

# The pinned first-run certificate proves a 62-clique partition for one of these
# 128-deletion cores.  Since every other 128-deletion core above is a q0-stabilizer
# image, that partition transports to all 30 cores.
print("I0123_U34_ORBIT_CERTIFICATE_PASS")
print("projective_unitary_automorphisms=62400")
print("q0_stabilizer=960")
print("u3_support_stabilizer_orbit=60")
print("support128_deletion_orbit=30")
print("full_u3_support_orbit=3900")
print("intersection_hist_with_B0=",dict(sorted(intersection_hist.items())))
print("only_intersection64_supports_are_stabilizer_orbit=True")
print("consequence: every support-128 rank-62 core in this orbit is isomorphic to the pinned cover-easy core")
