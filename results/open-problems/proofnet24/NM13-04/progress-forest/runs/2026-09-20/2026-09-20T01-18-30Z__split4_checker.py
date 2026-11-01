#!/usr/bin/env python3
"""
Exact checker for T07-SPLIT4-SIGN-02:
G_n = K_4 join independent set on n vertices.

Standard library only.  It:
  * builds the 15-state terminal-partition transfer exactly;
  * verifies M = 5 I + N and N^4 = 0;
  * compares transfer counts with the closed formulas for n=1..20;
  * brute-force enumerates every edge subset for n=1,2,3 and checks
    every edge pair plus the orbit formulas exactly.

All arithmetic is integer arithmetic.
"""
from itertools import combinations

T = tuple(range(4))

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks if b),
                        key=lambda b:(b[0], len(b), b)))

def gen_parts(items):
    items=list(items)
    if not items:
        yield ()
        return
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

def bi(p,x):
    for i,b in enumerate(p):
        if x in b:
            return i
    raise AssertionError

def trans(p,A):
    A=set(A)
    ids=[bi(p,x) for x in A]
    if len(set(ids)) != len(ids):
        return None
    if len(A)<=1:
        return p
    ids=set(ids)
    merged=set()
    out=[]
    for i,b in enumerate(p):
        if i in ids:
            merged.update(b)
        else:
            out.append(set(b))
    out.append(merged)
    return canon(out)

def zmat():
    return [[0]*S for _ in range(S)]

M=zmat()
E=[zmat() for _ in T]
EP={(i,j):zmat() for i,j in combinations(T,2)}
for a,p in enumerate(PARTS):
    for r in range(5):
        for A in combinations(T,r):
            q=trans(p,A)
            if q is None:
                continue
            b=IDX[q]
            M[a][b]+=1
            for i in A:
                E[i][a][b]+=1
            for i,j in combinations(A,2):
                EP[(i,j)][a][b]+=1

def eye():
    A=zmat()
    for i in range(S): A[i][i]=1
    return A

def madd(A,B,sa=1,sb=1):
    return [[sa*A[i][j]+sb*B[i][j] for j in range(S)] for i in range(S)]

def mmul(A,B):
    C=zmat()
    for i in range(S):
        for k in range(S):
            if A[i][k]:
                aik=A[i][k]
                for j in range(S):
                    if B[k][j]:
                        C[i][j]+=aik*B[k][j]
    return C

def mpow(A,n):
    R=eye()
    B=A
    while n:
        if n&1: R=mmul(R,B)
        B=mmul(B,B)
        n//=2
    return R

def rowmul(v,A):
    out=[0]*S
    for i,x in enumerate(v):
        if x:
            for j in range(S):
                out[j]+=x*A[i][j]
    return out

def rowsum(v):
    return sum(v)

I=eye()
N=madd(M,I,1,-5)
N2=mmul(N,N); N3=mmul(N2,N); N4=mmul(N3,N)
assert any(any(x for x in row) for row in N3)
assert not any(any(x for x in row) for row in N4)

# Enumerate K4 forests to get initial vectors with marked clique edges.
K4E=list(combinations(T,2))
def part_if_forest(edges, nverts=4):
    par=list(range(nverts))
    def f(x):
        while par[x]!=x:
            par[x]=par[par[x]]
            x=par[x]
        return x
    for a,b in edges:
        a=f(a); b=f(b)
        if a==b: return None
        par[b]=a
    blocks={}
    for x in range(nverts):
        blocks.setdefault(f(x),set()).add(x)
    return canon(blocks.values())

u=[0]*S
wt=[0]*S
wtta=[0]*S
wttd=[0]*S
e01=(0,1); e02=(0,2); e23=(2,3)
for mask in range(1<<len(K4E)):
    es=[K4E[k] for k in range(len(K4E)) if (mask>>k)&1]
    p=part_if_forest(es)
    if p is None: continue
    q=IDX[p]
    u[q]+=1
    if e01 in es: wt[q]+=1
    if e01 in es and e02 in es: wtta[q]+=1
    if e01 in es and e23 in es: wttd[q]+=1

assert sum(u)==38 and sum(wt)==14 and sum(wtta)==4 and sum(wttd)==5

def apply(v,*ops):
    for A in ops:
        v=rowmul(v,A)
    return v

def transfer_counts(n):
    Mn=mpow(M,n)
    out={}
    out["Z"]=rowsum(apply(u,Mn))
    out["Zt"]=rowsum(apply(wt,Mn))
    out["Ztt_adj"]=rowsum(apply(wtta,Mn))
    out["Ztt_dis"]=rowsum(apply(wttd,Mn))
    out["Zs"]=rowsum(apply(u,E[0],mpow(M,n-1)))
    out["Zts_inc"]=rowsum(apply(wt,E[0],mpow(M,n-1)))
    out["Zts_non"]=rowsum(apply(wt,E[2],mpow(M,n-1)))
    out["Zss_sameR"]=rowsum(apply(u,EP[(0,1)],mpow(M,n-1)))
    if n>=2:
        out["Zss_sameL"]=rowsum(apply(u,E[0],E[0],mpow(M,n-2)))
        out["Zss_dis"]=rowsum(apply(u,E[0],E[1],mpow(M,n-2)))
    return out

def closed_counts(n):
    p5=5**n
    out={
      "Z":p5*(16*n**3+327*n**2+2182*n+4750)//125,
      "Zt":p5*(8*n**2+107*n+350)//25,
      "Ztt_adj":p5*(3*n+20)//5,
      "Ztt_dis":p5*(4*n+25)//5,
      "Zs":p5*(16*n**3+399*n**2+3166*n+8044)//625,
      "Zts_inc":p5*(8*n**2+121*n+446)//125,
      "Zts_non":p5*(8*n**2+141*n+576)//125,
      "Zss_sameR":p5*(8*n**2+121*n+446)//125,
    }
    if n>=2:
        out["Zss_sameL"]=p5*(16*n**3+471*n**2+4216*n+11806)//3125
        out["Zss_dis"]=p5*(16*n**3+471*n**2+4416*n+13156)//3125
    return out

def closed_gaps(n):
    p=5**(2*n)
    out={
      "tt_adj": p*(16*n**4+411*n**3+3963*n**2+17010*n+27500)//625,
      "tt_dis": 2*p*(2*n**3+73*n**2+675*n+1875)//625,
      "ts_inc": 2*p*(176*n**4+4731*n**3+47450*n**2+210443*n+348450)//15625,
      "ts_non": 2*p*(16*n**4+421*n**3+4375*n**2+21113*n+39700)//15625,
      "ss_sameR": p*(256*n**6+9568*n**5+146713*n**4+1179901*n**3+
                     5246068*n**2+12236558*n+11743436)//390625,
    }
    if n>=2:
        out["ss_sameL"]=6*p*(688*n**4+18771*n**3+190924*n**2+
                             857986*n+1437906)//390625
        out["ss_dis"]=2*p*(464*n**4+12813*n**3+133847*n**2+
                           626108*n+1107468)//390625
    return out

def gaps_from_counts(c):
    Z=c["Z"]; Zt=c["Zt"]; Zs=c["Zs"]
    out={
      "tt_adj":Zt*Zt-Z*c["Ztt_adj"],
      "tt_dis":Zt*Zt-Z*c["Ztt_dis"],
      "ts_inc":Zt*Zs-Z*c["Zts_inc"],
      "ts_non":Zt*Zs-Z*c["Zts_non"],
      "ss_sameR":Zs*Zs-Z*c["Zss_sameR"],
    }
    if "Zss_sameL" in c:
        out["ss_sameL"]=Zs*Zs-Z*c["Zss_sameL"]
        out["ss_dis"]=Zs*Zs-Z*c["Zss_dis"]
    return out

for n in range(1,21):
    a=transfer_counts(n)
    b=closed_counts(n)
    assert a==b, (n,a,b)
    g=gaps_from_counts(a)
    h=closed_gaps(n)
    assert g==h, (n,g,h)
    assert all(x>0 for x in g.values())

# Full brute-force check for n=1,2,3.
def brute(n):
    nv=4+n
    edges=K4E+[(i,4+r) for r in range(n) for i in T]
    m=len(edges)
    Z=0
    Ze=[0]*m
    Zef=[[0]*m for _ in range(m)]
    for mask in range(1<<m):
        par=list(range(nv))
        def f(x):
            while par[x]!=x:
                par[x]=par[par[x]]
                x=par[x]
            return x
        ok=True
        chosen=[]
        for k,(a,b) in enumerate(edges):
            if not ((mask>>k)&1): continue
            ra,rb=f(a),f(b)
            if ra==rb:
                ok=False
                break
            par[rb]=ra
            chosen.append(k)
        if not ok: continue
        Z+=1
        for a in chosen: Ze[a]+=1
        for a,b in combinations(chosen,2):
            Zef[a][b]+=1
            Zef[b][a]+=1
    return edges,Z,Ze,Zef

def orbit(e,f):
    ce=lambda x: x[0]<4 and x[1]<4
    c1,c2=ce(e),ce(f)
    if c1 and c2:
        return "tt_adj" if set(e)&set(f) else "tt_dis"
    if c1 != c2:
        t=e if c1 else f
        s=f if c1 else e
        terminal=s[0] if s[0]<4 else s[1]
        return "ts_inc" if terminal in t else "ts_non"
    term=lambda s: s[0] if s[0]<4 else s[1]
    right=lambda s: s[1] if s[0]<4 else s[0]
    if right(e)==right(f): return "ss_sameR"
    if term(e)==term(f): return "ss_sameL"
    return "ss_dis"

for n in (1,2,3):
    edges,Z,Ze,Zef=brute(n)
    c=closed_counts(n); g=closed_gaps(n)
    assert Z==c["Z"]
    for a,b in combinations(range(len(edges)),2):
        gap=Ze[a]*Ze[b]-Z*Zef[a][b]
        o=orbit(edges[a],edges[b])
        assert gap==g[o], (n,edges[a],edges[b],o,gap,g[o])
        assert gap>0

print("T07-SPLIT4 exact checker")
print("states =", S)
print("nilpotent index: N^3 != 0 and N^4 = 0")
print("K4 initial totals: forests=38 edge-marked=14 adj-pair=4 disjoint-pair=5")
for n in (1,2,3,4,8,20):
    c=closed_counts(n)
    g=closed_gaps(n)
    print("n=%d Z=%d min_gap=%d orbits=%d" % (n,c["Z"],min(g.values()),len(g)))
print("transfer-vs-closed formulas: PASS for n=1..20")
print("full brute-force all edge pairs: PASS for n=1,2,3")
print("ALL_EXACT_CHECKS_PASS")
