from fractions import Fraction
import sys
sys.setrecursionlimit(10000)
import sympy as sp
from collections import defaultdict

# exact K=Q(zeta_84) representation scaled by 7; vector is coefficients degree<24
x=sp.symbols('x')
phi=sp.Poly(sp.cyclotomic_poly(84,x),x,domain=sp.QQ)
D=24

def red_poly(expr):
    return sp.Poly(expr,x,domain=sp.QQ).rem(phi)

def coeffs7(poly):
    p=poly.rem(phi)
    arr=[Fraction(0) for _ in range(D)]
    for (e,),c in p.terms():
        arr[e]=Fraction(int(c.p), int(c.q))
    out=[]
    for c in arr:
        v=c*7
        if v.denominator!=1:
            raise ValueError(('non-int*1/7',c))
        out.append(v.numerator)
    return tuple(out)

def zpow(k):
    k%=84
    return red_poly(x**k)

def inv_expr(expr):
    p=red_poly(expr)
    return sp.invert(p,phi)

i=zpow(21)
half_alpha=(i*inv_expr(x**12-x**(84-12))).rem(phi)
half_beta =(i*inv_expr(x**24-x**(84-24))).rem(phi)
half_gamma=(i*inv_expr(x**48-x**(84-48))).rem(phi)

P=[];Q=[];R=[]
for j in range(7):
    P.append(coeffs7((-half_gamma*zpow(12*j+21)).rem(phi)))
    Q.append(coeffs7(( half_alpha*zpow(12*j+7)).rem(phi)))
    R.append(coeffs7(( half_beta *zpow(12*j+35)).rem(phi)))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
ZERO=(0,)*D
u=[None]*84
for j in range(7):
    jj=lambda a:(a+j)%7
    pairs=[(P[jj(3)],P[jj(4)]),(R[j],Q[j]),(R[jj(1)],R[jj(4)]),(R[jj(6)],P[jj(6)]),(Q[jj(4)],Q[jj(6)]),(Q[jj(5)],P[jj(5)]),(P[jj(1)],P[j]),(Q[jj(4)],R[jj(4)]),(R[jj(1)],R[jj(5)]),(P[jj(3)],R[jj(3)]),(Q[jj(3)],Q[jj(1)]),(P[jj(2)],Q[jj(2)])]
    for k,(tail,head) in enumerate(pairs):
        u[12*j+k]=sub(head,tail)
assert len(set(u))==84
assert all(neg(v) in set(u) for v in u)
B=neg(add(u[56],u[70]))

PATHS='''
2 23 28 69 33
7 19 28 69 38
10 31 68 37 14
33 28 20 66 3
37 28 25 74 3
40 17 53 7 14
42 23 14 65 14
44 7 28 78 25
46 7 14 44 13
47 83 37 14 16
48 28 0 6 28
50 19 17 77 28
50 28 17 77 19
53 32 83 14 22
53 40 7 14 17
54 17 28 80 23
62 83 28 25 23
64 7 33 31 14
66 3 20 33 28
69 19 28 38 7
69 33 28 2 23
69 34 17 7 33
69 38 19 7 28
72 39 14 33 12
77 10 17 39 37
77 28 17 50 19
77 46 28 10 23
78 7 44 28 25
80 28 17 54 23
82 19 58 28 25
82 28 26 54 14
83 23 28 62 25
83 36 48 14 17
0 21 83 33 28 52
2 14 47 30 83 37
2 33 14 12 58 39
2 47 30 37 14 83
3 20 37 33 60 7
3 25 4 28 60 37
3 34 14 31 47 80
3 36 8 69 34 28
3 37 13 69 39 22
3 39 28 66 29 8
4 14 49 28 46 7
4 17 25 28 69 48
4 25 51 14 53 17
4 39 28 32 69 8
6 14 37 68 42 19
6 19 28 7 57 44
6 28 57 44 7 19
7 14 78 50 33 31
7 17 44 5 54 28
7 28 64 8 44 25
7 31 69 3 34 33
7 33 14 78 31 50
8 14 53 25 58 21
8 21 0 58 39 28
8 28 73 39 37 6
8 29 66 28 39 3
10 17 23 77 51 39
10 23 14 51 68 31
10 28 37 68 0 31
10 37 60 7 14 38
12 25 68 19 28 58
13 0 39 37 28 76
13 14 51 30 61 14
14 17 7 54 53 26
14 22 69 42 3 34
14 59 82 28 40 17
14 79 18 37 28 60
16 69 47 14 37 13
17 19 36 53 14 72
18 69 28 33 71 20
19 52 21 14 47 83
20 14 47 19 51 82
20 71 33 28 69 18
21 14 38 51 14 74
22 69 14 13 53 32
23 60 32 33 83 7
24 7 28 52 19 69
25 23 76 48 83 28
25 83 47 19 82 37
26 14 39 72 33 82
28 9 28 66 3 40
28 16 83 0 47 37
28 17 40 7 53 0
28 18 71 69 33 20
28 24 75 14 66 33
28 25 12 77 64 33
28 63 18 16 69 28
28 73 63 12 28 25
30 77 28 17 43 80
31 0 33 28 7 64
31 14 48 24 69 7
32 1 54 83 28 23
32 14 13 69 22 53
33 12 83 32 77 39
33 14 66 38 83 21
33 17 66 18 83 39
33 20 7 67 46 14
33 21 14 31 64 77
33 23 21 77 46 83
33 23 80 17 72 39
33 28 82 11 69 34
33 31 50 14 7 78
33 37 83 68 25 12
34 17 15 51 14 68
34 28 17 80 47 0
34 33 3 6 28 66
36 17 28 0 83 48
37 6 33 68 5 28
37 13 14 60 3 36
37 14 74 3 42 25
37 17 54 9 80 28
37 24 39 80 77 17
37 25 68 15 78 28
37 28 60 4 3 25
37 83 14 30 47 2
38 7 14 60 37 10
38 21 66 14 83 33
39 7 78 6 37 33
39 12 28 54 81 14
39 13 14 51 76 23
39 14 18 74 17 51
39 17 14 18 74 51
39 18 14 8 69 42
39 22 69 13 3 37
39 37 14 6 62 13
40 3 53 14 31 7
40 7 3 31 53 14
40 28 3 82 45 14
42 3 34 14 69 22
42 19 82 14 58 25
42 23 25 14 62 83
42 25 3 14 74 37
42 77 46 23 10 14
44 13 21 14 77 46
44 14 21 77 13 46
44 25 83 7 48 17
44 28 5 54 7 17
44 57 7 28 19 6
46 13 77 21 14 44
46 28 7 44 0 13
46 77 14 10 23 42
46 83 77 21 33 23
47 0 80 28 34 17
47 14 21 45 78 14
47 34 3 31 80 14
47 37 14 13 69 16
47 80 31 3 14 34
48 17 69 13 14 36
48 83 28 76 25 23
50 14 31 13 14 62
50 17 14 48 83 22
50 31 78 7 33 14
51 0 17 28 39 4
51 14 39 12 77 24
51 17 0 39 4 28
51 20 0 33 82 28
51 39 77 23 10 17
51 82 19 47 14 20
52 33 28 83 0 21
53 0 32 83 28 22
53 7 26 14 17 54
53 14 72 36 17 19
53 17 14 51 25 4
53 17 19 25 58 7
53 22 69 32 13 14
53 26 25 28 77 3
54 14 17 26 53 7
54 14 81 12 39 28
54 23 28 83 1 32
54 28 1 32 83 23
58 7 25 78 28 30
58 14 25 53 8 21
58 14 41 28 83 16
58 21 25 53 14 8
58 25 42 14 82 19
58 28 39 5 3 22
58 39 12 14 2 33
60 7 44 13 32 14
60 28 23 32 10 77
62 13 6 39 37 14
62 13 39 37 6 14
62 14 83 20 41 28
64 77 31 14 21 33
66 14 49 28 7 24
66 28 29 17 68 19
66 33 83 18 39 17
68 14 51 23 10 31
68 15 78 28 37 25
68 19 17 37 83 36
68 31 0 37 10 28
69 7 24 52 28 19
69 8 34 3 36 28
69 23 16 28 72 33
69 28 48 22 3 20
69 42 8 14 39 18
69 48 31 24 7 14
72 19 44 17 39 7
72 28 33 16 69 23
72 39 19 76 28 23
74 14 21 54 37 17
74 37 14 25 42 3
74 51 18 17 39 14
76 23 39 19 72 28
76 37 28 0 39 13
77 3 42 39 14 26
77 17 80 39 37 24
77 19 64 28 36 17
77 24 51 14 39 12
77 28 24 69 37 16
77 32 42 14 83 30
77 39 12 40 3 28
78 25 28 37 15 68
80 14 31 3 34 47
80 17 39 63 28 18
80 23 46 13 47 14
80 43 17 28 77 30
82 14 19 47 51 20
82 28 25 44 72 19
82 33 72 14 39 26
82 37 19 47 83 25
83 7 33 32 23 60
83 16 28 44 77 32
83 21 14 47 52 19
83 22 48 14 50 17
83 28 22 41 64 14
83 30 14 32 77 42
83 33 14 66 38 21
83 39 18 66 33 17
'''
paths=[tuple(map(int,line.split())) for line in PATHS.strip().splitlines()]
print('paths',len(paths),'len5',sum(len(p)==5 for p in paths),'len6',sum(len(p)==6 for p in paths))
V={ZERO}
for p in paths:
    v=ZERO
    for a in p:
        v=add(v,u[a]); V.add(v)
    if v!=B:
        print('bad endpoint',p); raise SystemExit
print('V',len(V))
print('B in V',B in V)

# Numeric embedding is used only to choose a stable display/index order; no distance claim relies on it.
import cmath, math
zeta=cmath.exp(2j*math.pi/84)
pows=[zeta**k for k in range(D)]
def ceval(v): return sum(c*pows[k] for k,c in enumerate(v))/7.0
vs=sorted(V,key=lambda v:(round(ceval(v).real,12),round(ceval(v).imag,12),v))
idx={v:i for i,v in enumerate(vs)}
edges=set()
for i,v in enumerate(vs):
    for w in u:
        t=add(v,w)
        j=idx.get(t)
        if j is not None and i<j: edges.add((i,j))
print('shift edges',len(edges))

def fracv(v): return tuple(Fraction(x,7) for x in v)
def fadd(a,b): return tuple(x+y for x,y in zip(a,b))
def fsub(a,b): return tuple(x-y for x,y in zip(a,b))
def fscale(a,c): return tuple(c*x for x in a)
MAXE=140
zrep=[]
for e in range(MAXE+1):
    coeff=[0]*(max(25,e+1)); coeff[e]=1
    for deg in range(len(coeff)-1,23,-1):
        c=coeff[deg]
        if c:
            sh=deg-24
            coeff[sh+22] -= c; coeff[sh+18] += c; coeff[sh+16] += c
            coeff[sh+12] -= c; coeff[sh+8] += c; coeff[sh+6] += c
            coeff[sh+2] -= c; coeff[sh] -= c; coeff[deg]=0
    zrep.append(tuple(coeff[:24]))

def mul_zpow(a,k):
    k%=84
    out=[Fraction(0) for _ in range(24)]
    for i,ai in enumerate(a):
        if ai:
            rr=zrep[i+k]
            for j,c in enumerate(rr): out[j]+=ai*c
    return tuple(out)

VK=[fracv(v) for v in vs]
UK=[fracv(w) for w in u]
BK=fracv(B)
ONE=(Fraction(1),)+tuple(Fraction(0) for _ in range(23))
ZERO_K=tuple(Fraction(0) for _ in range(24))
assert set(mul_zpow(w,14) for w in UK)==set(UK)
assert set(mul_zpow(w,-14) for w in UK)==set(UK)
c1=fscale(fadd(fscale(ONE,Fraction(-1)),BK),Fraction(1,2))
c2=fscale(fadd(ONE,BK),Fraction(1,2))
def rot_about(w,c,k): return fadd(c,mul_zpow(fsub(w,c),k))
V1={rot_about(w,c1,-14) for w in VK}
V2={rot_about(w,c2,14) for w in VK}
VG2=sorted(V1|V2)
idx2={v:i for i,v in enumerate(VG2)}
edges2=set()
for i,v in enumerate(VG2):
    for w in UK:
        j=idx2.get(fadd(v,w))
        if j is not None and i<j: edges2.add((i,j))
print('G2 copy sizes/intersection/union',len(V1),len(V2),len(V1&V2),len(VG2))
print('G2 edges',len(edges2))

def make_adj(n,edges):
    a=[set() for _ in range(n)]
    for x,y in edges: a[x].add(y);a[y].add(x)
    return a
adj2=make_adj(len(VG2),edges2)

def kmul(a,b):
    out=[Fraction(0) for _ in range(24)]
    for i,ai in enumerate(a):
        if not ai: continue
        for j,bj in enumerate(b):
            if not bj: continue
            q=ai*bj; rr=zrep[i+j]
            for t,c in enumerate(rr): out[t]+=q*c
    return tuple(out)

def kconj(a):
    out=[Fraction(0) for _ in range(24)]
    for i,ai in enumerate(a):
        if ai:
            rr=zrep[(84-i)%84]
            for t,c in enumerate(rr): out[t]+=ai*c
    return tuple(out)

for w in UK:
    assert kmul(w,kconj(w)) == ONE
print('UNIT_VECTORS_EXACT',len(UK))
assert len(VK)==740 and len(edges)==3985
print('G1_EXACT_COUNTS',len(VK),len(edges))
assert len(VG2)==1066 and len(edges2)==6264
print('G2_EXACT_COUNTS',len(VG2),len(edges2))

MONE=fscale(ONE,-1)
def Fext(w):
    wp=fadd(w,ONE)
    return (fadd(MONE,fscale(wp,Fraction(7,8))), fscale(mul_zpow(wp,21),Fraction(1,8)))

orig=[(w,ZERO_K) for w in VG2]
trans=[Fext(w) for w in VG2]
VG3=sorted(set(orig)|set(trans)); idx3={v:i for i,v in enumerate(VG3)}
assert len(set(orig)&set(trans))==1
assert len(VG3)==2131
edges3=set()
for a,b in edges2:
    edges3.add(tuple(sorted((idx3[orig[a]],idx3[orig[b]]))))
    edges3.add(tuple(sorted((idx3[trans[a]],idx3[trans[b]]))))

def ext_norm2_diff(p,q):
    A=fsub(p[0],q[0]); Bc=fsub(p[1],q[1])
    base=fadd(kmul(A,kconj(A)),fscale(kmul(Bc,kconj(Bc)),15))
    cross=fadd(kmul(A,kconj(Bc)),kmul(Bc,kconj(A)))
    return base,cross

for w in (BK,ONE):
    p=(w,ZERO_K); q=Fext(w)
    base,cross=ext_norm2_diff(p,q)
    assert base==ONE and cross==ZERO_K
    edges3.add(tuple(sorted((idx3[p],idx3[q]))))
assert Fraction(49,64)+Fraction(15,64)==1
assert len(edges3)==12530
print('G3_EXACT_COUNTS',len(VG3),len(edges3),'BRIDGES',2)

import json,hashlib
witness_path=sys.argv[1] if len(sys.argv)>1 else 'haugland_relation_witnesses.json'
raw=open(witness_path,'rb').read(); data=json.loads(raw)
print('WITNESS_SHA256',hashlib.sha256(raw).hexdigest())
adj1=make_adj(len(vs),edges)
A1=idx[ZERO]; B1=idx[B]
G2m=idx2[fscale(ONE,-1)]; G2p=idx2[ONE]
checks=[('G1_A_B',adj1,A1,B1),('G2_m1_p1',adj2,G2m,G2p)]
for name,adj,u0,v0 in checks:
    rec=data[name]
    assert rec['n']==len(adj); assert rec['m']==sum(map(len,adj))//2
    assert rec['u']==u0 and rec['v']==v0
    for relation in ('eq','neq'):
        rr=rec[relation]; assert rr['sat'] is True
        col=rr['coloring']
        assert len(col)==len(adj) and all(isinstance(c,int) and 0<=c<5 for c in col)
        assert all(col[a]!=col[b] for a in range(len(adj)) for b in adj[a] if a<b)
        if relation=='eq': assert col[u0]==col[v0]
        else: assert col[u0]!=col[v0]
        print('WITNESS_VERIFIED',name,relation,'colors',len(set(col)))
print('ALL_EXACT_HAUGLAND_CHECKS_PASSED')
