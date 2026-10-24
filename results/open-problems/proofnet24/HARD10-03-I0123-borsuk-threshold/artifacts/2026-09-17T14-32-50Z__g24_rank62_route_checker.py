from itertools import product, combinations
from collections import deque, Counter

# Exact certificate for two first-run I0123 obstructions inside the G_2(4) route:
# (1) all 65 structural split planes are too transverse to give the needed R^62 support window;
# (2) one exact 128-support three-dimensional code subspace leaves a 288-point core
#     that has an explicit partition into 62 cliques, hence is not a Borsuk counterexample in R^62.
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
            ia=INV[a]; return tuple(mul(ia,x) for x in v)
    raise ValueError("zero vector")
def add(u,v): return tuple(a^b for a,b in zip(u,v))
def scale(a,u): return tuple(mul(a,x) for x in u)
def h(u,v): return mul(u[0],pw(v[0],4)) ^ mul(u[1],pw(v[1],4)) ^ mul(u[2],pw(v[2],4))
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
    assert len(s)==15
    tm.append(sum(1<<ix[p] for p in s))
adj=[0]*416
for i in range(416):
    for j in range(i+1,416):
        if (tm[i]&tm[j]).bit_count()==3:
            adj[i]|=1<<j; adj[j]|=1<<i
assert {x.bit_count() for x in adj}=={100}
lam=set(); mu=set()
for i in range(416):
    for j in range(i+1,416):
        c=(adj[i]&adj[j]).bit_count()
        if (adj[i]>>j)&1: lam.add(c)
        else: mu.add(c)
assert lam=={36} and mu=={20}
# The exact SRG relation gives nontrivial eigenvalues 20 and -4.
# Trace(A)=0 then forces multiplicity(20)=65 and multiplicity(-4)=350.

def eigen20(v):
    for x in range(416):
        tot=0; y=adj[x]
        while y:
            b=y&-y; z=b.bit_length()-1; y^=b; tot += v[z]
        if tot != 20*v[x]: return False
    return True

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
    assert sorted(map(len,comps))==[32,32,32]
    words=[]
    for a,b in combinations(range(3),2):
        u=[0]*416
        for x in comps[a]: u[x]=1
        for x in comps[b]: u[x]=-1
        assert eigen20(u)
        words.append(frozenset(comps[a]|comps[b]))
    return frozenset(B),comps,words

splits=[split(q) for q in iso]
plane_inter=Counter(); cross=Counter(); ww=Counter()
for i in range(65):
    Bi,_,Wi=splits[i]
    for j in range(i+1,65):
        Bj,_,Wj=splits[j]
        plane_inter[len(Bi&Bj)] += 1
        for w in Wj: cross[(len(w&Bi),len(w-Bi))] += 1
        for w in Wi: cross[(len(w&Bj),len(w-Bj))] += 1
        for u in Wi:
            for v in Wj: ww[len(u&v)] += 1
assert plane_inter==Counter({21:2080})
assert set(cross)=={(14,50)}
assert set(ww)=={8,12}

# Fixed split plane P from the first isotropic point.
B0,C0,Wwords=splits[0]
u1=[0]*416; u2=[0]*416
for x in C0[0]: u1[x]=1; u2[x]=1
for x in C0[1]: u1[x]=-1
for x in C0[2]: u2[x]=-1
assert eigen20(u1) and eigen20(u2)
assert len(B0)==96

# Exact third 20-eigenvector, found heuristically then frozen here and checked from scratch.
POS3=[0, 35, 80, 82, 86, 97, 122, 127, 131, 135, 149, 154, 157, 167, 178, 196, 197, 204, 214, 223, 235, 250, 270, 276, 291, 297, 305, 308, 309, 311, 316, 321, 324, 326, 339, 342, 343, 349, 357, 364, 365, 371, 389, 392, 407, 409, 410, 415]
NEG3=[11, 17, 70, 72, 74, 79, 88, 91, 102, 106, 108, 120, 121, 125, 145, 146, 164, 169, 175, 180, 190, 194, 198, 205, 209, 211, 224, 227, 229, 242, 245, 258, 265, 269, 274, 301, 307, 313, 328, 331, 358, 363, 366, 367, 382, 385, 386, 394]
u3=[0]*416
for x in POS3: u3[x]=1
for x in NEG3: u3[x]=-1
assert len(POS3)==48 and len(NEG3)==48 and set(POS3).isdisjoint(NEG3)
assert eigen20(u3)
supp3={i for i,x in enumerate(u3) if x}
assert len(supp3)==96 and len(supp3-B0)==32 and len(supp3&B0)==64
Z=set(B0)|supp3
assert len(Z)==128
S=sorted(set(range(416))-Z)
assert len(S)==288
# u3 is independent of u1,u2 because it is nonzero outside supp(P)=B0.
assert not any(u3[x] for x in S)
assert any(u3[x] for x in supp3-B0)

PARTS=[(177, 201, 231, 296, 361), (54, 128, 213, 295, 303), (45, 129, 199, 277, 387), (25, 31, 236, 243, 372), (182, 191, 306, 334, 405), (8, 206, 322, 377, 400), (49, 62, 100, 161, 375), (5, 113, 212, 283, 286), (153, 160, 188, 332, 373), (4, 57, 90, 105, 294), (123, 139, 168, 271, 397), (3, 40, 166, 218, 259), (81, 96, 155, 185, 351), (124, 288, 329, 335, 378), (58, 184, 359, 370, 388), (55, 163, 300, 327, 347), (42, 48, 203, 207, 369), (16, 51, 262, 315, 403), (20, 32, 156, 251, 350), (27, 33, 63, 87, 323), (1, 24, 44, 238, 396), (13, 36, 181, 290, 395), (6, 19, 189, 220, 393), (67, 152, 162, 266, 383), (46, 89, 147, 312, 330), (10, 12, 221, 379, 391), (64, 142, 234, 319, 413), (21, 93, 115, 159, 402), (65, 94, 289, 304, 376), (14, 71, 101, 252, 257), (38, 53, 76, 109, 302), (75, 85, 111, 151, 233), (69, 148, 170, 193, 267), (95, 143, 248, 356, 362), (28, 41, 174, 346, 408), (18, 83, 273, 337, 390), (133, 141, 210, 237, 411), (73, 78, 173, 226, 336), (2, 30, 99, 287, 406), (37, 138, 254, 285, 341), (56, 279, 292, 325, 368), (61, 140, 232, 255, 340), (183, 244, 278, 320, 355), (192, 200, 260, 263, 298), (104, 110, 215, 261, 360), (9, 50, 132, 353, 401), (134, 202, 228, 310, 354), (107, 114, 172, 246, 314), (60, 103, 165, 225, 284), (39, 137, 253, 380, 412), (26, 77, 92, 208, 268), (7, 47, 52, 150, 187), (22, 59), (136, 384), (217, 317), (15, 68, 144), (34, 158, 338), (43, 66, 249), (126, 186, 398), (171, 280, 414), (264, 272, 404), (176, 216, 219, 230)]
flat=[v for P in PARTS for v in P]
assert len(PARTS)==62 and len(flat)==288 and len(set(flat))==288 and set(flat)==set(S)
assert Counter(map(len,PARTS))==Counter({5:52,3:6,2:3,4:1})
for P in PARTS:
    for a,b in combinations(P,2):
        assert (adj[a]>>b)&1, ("not a clique",P,a,b)

print("I0123_EXACT_CERTIFICATE_PASS")
print("G2(4): vertices=416 degree=100; isotropic split planes=65")
print("split-family: every distinct plane pair intersects in 21 vertices")
print("split-family: every structural 64-word from another split has 14 points inside / 50 outside a fixed 96-support plane")
print("therefore that structural one-step rank-drop route gives support 146, not <=105")
print("frozen 3D code witness: support(Z)=128; surviving two-distance core=288 points in dimension <=62")
print("explicit clique partition: 62 parts with sizes", dict(sorted(Counter(map(len,PARTS)).items())))
print("consequence: this 288-point core is partitionable into 62 smaller-diameter parts; core + any one extra point is partitionable into <=63 parts by making it a singleton")
