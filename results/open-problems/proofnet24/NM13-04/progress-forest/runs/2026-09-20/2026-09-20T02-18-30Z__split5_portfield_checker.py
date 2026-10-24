#!/usr/bin/env python3
"""Exact certificate for NM13-04 T07 split-5 one-port-field theorem.

Graph H_n = K_5 join independent set on n vertices, n>=1.
Distinguished clique edge g={0,1} has weight s>=0; every other real edge has weight 1.
The script proves, by exact integer/rational arithmetic, that every Rayleigh difference
is positive for all n>=1 and s>=0 (with orbit types requiring two independent vertices
present only for n>=2).

Proof structure certified here:
  * 52 terminal partitions (Bell number B_5), transfer M=6I+N, N^5=0;
  * exact classification of edge pairs into 25 orbits under the stabilizer of g;
  * each normalized Rayleigh gap is A(n)+B(n)s+C(n)s^2 with deg <= 8;
  * 22 orbits are coefficientwise nonnegative in n in A,B,C, with A>0;
  * the only 3 non-coefficientwise orbits have A,C>0 and 4AC-B^2
    coefficientwise positive, so their quadratic has negative discriminant;
  * independent brute-force enumeration for n=2 agrees with every transfer count.

Standard library only.
"""
from itertools import combinations, permutations
from fractions import Fraction
from functools import lru_cache
from math import gcd

R=5
T=tuple(range(R))
BASE=R+1
PORT=(0,1)

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks if b),
                        key=lambda b:(b[0],len(b),b)))

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
assert S==52

def bi(p,x):
    for i,b in enumerate(p):
        if x in b:
            return i
    raise AssertionError

def trans(p,A):
    A=set(A)
    ids=[bi(p,x) for x in A]
    if len(set(ids))!=len(ids):
        return None
    if len(A)<=1:
        return p
    ids=set(ids)
    merged=set(); out=[]
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
    for k in range(R+1):
        for A in combinations(T,k):
            q=trans(p,A)
            if q is None:
                continue
            b=IDX[q]
            M[a][b]+=1
            for i in A:
                E[i][a][b]+=1
            for i,j in combinations(A,2):
                EP[(i,j)][a][b]+=1

def mmul(A,B):
    C=zmat()
    for i in range(S):
        for k,a in enumerate(A[i]):
            if not a: continue
            for j,b in enumerate(B[k]):
                if b: C[i][j]+=a*b
    return C

def msub_scalar_I(A,c):
    B=[row[:] for row in A]
    for i in range(S): B[i][i]-=c
    return B

def nonzero(A):
    return any(any(row) for row in A)

N=msub_scalar_I(M,BASE)
Np=N
for power in range(1,6):
    if power==4:
        assert nonzero(Np)
    if power==5:
        assert not nonzero(Np)
    Np=mmul(Np,N)

def rowmul(v,A):
    out=[0]*S
    for i,x in enumerate(v):
        if not x: continue
        for j,a in enumerate(A[i]):
            if a: out[j]+=x*a
    return out

K5E=list(combinations(T,2))

def clique_partition(es):
    par=list(range(R))
    def root(x):
        while par[x]!=x:
            par[x]=par[par[x]]
            x=par[x]
        return x
    for a,b in es:
        a=root(a); b=root(b)
        if a==b: return None
        par[b]=a
    blocks={}
    for x in range(R):
        blocks.setdefault(root(x),set()).add(x)
    return canon(blocks.values())

@lru_cache(None)
def init_poly(marked_clique_tuple):
    marked=set(marked_clique_tuple)
    a=[0]*S; b=[0]*S
    for mask in range(1<<len(K5E)):
        es=[K5E[k] for k in range(len(K5E)) if (mask>>k)&1]
        p=clique_partition(es)
        if p is None: continue
        ess=set(es)
        if not marked.issubset(ess): continue
        q=IDX[p]
        if PORT in marked:
            a[q]+=1
        elif PORT in ess:
            b[q]+=1
        else:
            a[q]+=1
    return tuple(a),tuple(b)

def count_poly(marked_clique=(), marked_spokes=(), n=1):
    mc=tuple(sorted(tuple(sorted(e)) for e in marked_clique))
    a,b=init_poly(mc)
    a=list(a); b=list(b)
    byv={}
    for v,t in marked_spokes:
        byv.setdefault(v,[]).append(t)
    for v in range(n):
        ts=sorted(byv.get(v,[]))
        if not ts:
            op=M
        elif len(ts)==1:
            op=E[ts[0]]
        elif len(ts)==2:
            op=EP[tuple(ts)]
        else:
            raise AssertionError("at most two marked edges")
        a=rowmul(a,op); b=rowmul(b,op)
    return sum(a),sum(b)

def marks(edge):
    if edge[0]=='c':
        return [tuple(sorted(edge[1:]))],[]
    return [],[(edge[1],edge[2])]

def count_edge(edge,n):
    c,s=marks(edge)
    return count_poly(c,s,n)

def count_pair(e,f,n):
    c1,s1=marks(e); c2,s2=marks(f)
    return count_poly(c1+c2,s1+s2,n)

def gap_coeffs(e,f,n):
    z=count_poly((),(),n)
    ze=count_edge(e,n); zf=count_edge(f,n); zef=count_pair(e,f,n)
    a,b=ze; c,d=zf; p,q=z; r,t=zef
    return (a*c-p*r,
            a*d+b*c-p*t-q*r,
            b*d-q*t)

REPS={
 'cc_gA':(('c',0,1),('c',0,2)),
 'cc_gB':(('c',0,1),('c',2,3)),
 'cc_AA_sameP':(('c',0,2),('c',0,3)),
 'cc_AA_sameQ':(('c',0,2),('c',1,2)),
 'cc_AA_dis':(('c',0,2),('c',1,3)),
 'cc_AB_inc':(('c',0,2),('c',2,3)),
 'cc_AB_non':(('c',0,2),('c',3,4)),
 'cc_BB':(('c',2,3),('c',2,4)),
 'cs_gP':(('c',0,1),('s',0,0)),
 'cs_gQ':(('c',0,1),('s',0,2)),
 'cs_A_Pinc':(('c',0,2),('s',0,0)),
 'cs_A_Pother':(('c',0,2),('s',0,1)),
 'cs_A_Qinc':(('c',0,2),('s',0,2)),
 'cs_A_Qother':(('c',0,2),('s',0,3)),
 'cs_B_P':(('c',2,3),('s',0,0)),
 'cs_B_Qinc':(('c',2,3),('s',0,2)),
 'cs_B_Qother':(('c',2,3),('s',0,4)),
 'ssR_PP':(('s',0,0),('s',0,1)),
 'ssR_PQ':(('s',0,0),('s',0,2)),
 'ssR_QQ':(('s',0,2),('s',0,3)),
 'ssD_PP_same':(('s',0,0),('s',1,0)),
 'ssD_PP_diff':(('s',0,0),('s',1,1)),
 'ssD_PQ':(('s',0,0),('s',1,2)),
 'ssD_QQ_same':(('s',0,2),('s',1,2)),
 'ssD_QQ_diff':(('s',0,2),('s',1,3)),
}
assert len(REPS)==25

def ptrim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def padd(a,b):
    c=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return ptrim(c)

def pscale(a,c): return ptrim([x*c for x in a])

def pmul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return ptrim(c)

def peval(p,x):
    z=Fraction(0)
    for c in reversed(p): z=z*x+c
    return z

def interp(points):
    out=[Fraction(0)]
    for i,(xi,yi) in enumerate(points):
        num=[Fraction(1)]; den=Fraction(1)
        for j,(xj,_) in enumerate(points):
            if i==j: continue
            num=pmul(num,[Fraction(-xj),Fraction(1)])
            den*=xi-xj
        out=padd(out,pscale(num,yi/den))
    return ptrim(out)

def lcm(a,b): return abs(a*b)//gcd(a,b) if a and b else 0

def scaled(p):
    den=1
    for x in p: den=lcm(den,x.denominator)
    ints=[int(x*den) for x in p]
    g=den
    for x in ints: g=gcd(g,abs(x))
    if g>1:
        den//=g; ints=[x//g for x in ints]
    return den,ints

def coeff_nonnegative(p): return all(c>=0 for c in p)
def coeff_positive(p): return all(c>0 for c in p)

POLYS={}
for name,(e,f) in REPS.items():
    start=2 if name.startswith('ssD_') else 1
    pts=[[],[],[]]
    for n in range(start,start+10):
        abc=gap_coeffs(e,f,n)
        for j,v in enumerate(abc):
            pts[j].append((n,Fraction(v,36**n)))
    qs=[]
    for j in range(3):
        q=interp(pts[j][:9])
        assert len(q)-1<=8
        assert peval(q,pts[j][9][0])==pts[j][9][1]
        qs.append(q)
    POLYS[name]=qs

EXCEPTIONS=[]
for name,(A,B,C) in POLYS.items():
    if not (coeff_nonnegative(A) and coeff_nonnegative(B) and coeff_nonnegative(C)):
        EXCEPTIONS.append(name)
assert EXCEPTIONS==['cc_AA_dis','cs_A_Pother','ssD_PP_diff']

for name,(A,B,C) in POLYS.items():
    start=2 if name.startswith('ssD_') else 1
    assert peval(A,start)>0
    if name not in EXCEPTIONS:
        assert coeff_nonnegative(A) and coeff_nonnegative(B) and coeff_nonnegative(C)
    else:
        assert coeff_nonnegative(A) and coeff_nonnegative(C)
        D=padd(pscale(pmul(A,C),Fraction(4)), pscale(pmul(B,B),Fraction(-1)))
        assert coeff_positive(D)
        assert peval(D,start)>0

def actual_edge(e):
    if e[0]=='c': return tuple(sorted((e[1],e[2])))
    return tuple(sorted((5+e[1],e[2])))

def graph_edges(n):
    return sorted(list(combinations(range(5),2)) +
                  [tuple(sorted((5+v,t))) for v in range(n) for t in range(5)])

def maps_n3():
    maps=[]
    for swap in (False,True):
        for p3 in permutations((2,3,4)):
            for pr in permutations((5,6,7)):
                mp={0:(1 if swap else 0),1:(0 if swap else 1)}
                mp.update({2+i:p3[i] for i in range(3)})
                mp.update({5+i:pr[i] for i in range(3)})
                maps.append(mp)
    return maps
AUT=maps_n3()
assert len(AUT)==72
E3=graph_edges(3)

def image_edge(e,mp): return tuple(sorted((mp[e[0]],mp[e[1]])))
def canon_pair(pair):
    ims=[]
    for mp in AUT:
        a=image_edge(pair[0],mp); b=image_edge(pair[1],mp)
        ims.append(tuple(sorted((a,b))))
    return min(ims)
ALL_ORBITS={canon_pair(p) for p in combinations(E3,2)}
REP_ORBITS={canon_pair(tuple(map(actual_edge,rep))) for rep in REPS.values()}
assert len(ALL_ORBITS)==25
assert REP_ORBITS==ALL_ORBITS

def brute_n2():
    n=2
    verts=5+n
    edges=graph_edges(n)
    m=len(edges)
    gidx=edges.index(PORT)
    Z=[0,0]
    Ze=[[0,0] for _ in range(m)]
    Zef={}
    for mask in range(1<<m):
        if mask.bit_count()>verts-1: continue
        par=list(range(verts))
        def root(x):
            while par[x]!=x:
                par[x]=par[par[x]]; x=par[x]
            return x
        inds=[]; ok=True
        for i,(a,b) in enumerate(edges):
            if not ((mask>>i)&1): continue
            ra=root(a); rb=root(b)
            if ra==rb:
                ok=False; break
            par[rb]=ra; inds.append(i)
        if not ok: continue
        hg=1 if gidx in inds else 0
        Z[hg]+=1
        for i in inds:
            exp=hg-(1 if i==gidx else 0)
            Ze[i][exp]+=1
        for i,j in combinations(inds,2):
            exp=hg-(1 if (i==gidx or j==gidx) else 0)
            Zef.setdefault((i,j),[0,0])[exp]+=1
    assert tuple(Z)==count_poly((),(),n)
    def sym(e):
        a,b=e
        if a<5 and b<5: return ('c',a,b)
        if a>=5: a,b=b,a
        return ('s',b-5,a)
    for i,e in enumerate(edges):
        assert tuple(Ze[i])==count_edge(sym(e),n)
    for i,j in combinations(range(m),2):
        got=tuple(Zef.get((i,j),[0,0]))
        want=count_pair(sym(edges[i]),sym(edges[j]),n)
        assert got==want,(edges[i],edges[j],got,want)
    return len(edges),sum(Z),Z

m2,z2,z2poly=brute_n2()

print('T07-SPLIT5-PORTFIELD exact checker')
print('states =',S)
print('transfer: M=6I+N, N^4 != 0, N^5 = 0')
print('pair_orbits_under_port_stabilizer =',len(ALL_ORBITS))
print('exceptional_quadratic_orbits =',','.join(EXCEPTIONS))
print('brute_n2_edges =',m2,'forests_at_s=1 =',z2,'Z(s)=',z2poly)
print('POLYNOMIAL_CERTIFICATES normalized by 36^n; coefficient lists are high-degree-first integers over denominator')
for name in sorted(POLYS):
    A,B,C=POLYS[name]
    fields=[]
    for tag,p in [('A',A),('B',B),('C',C)]:
        den,ints=scaled(p)
        fields.append(f"{tag}=({list(reversed(ints))})/{den}")
    print(name,'; '.join(fields))
    if name in EXCEPTIONS:
        D=padd(pscale(pmul(A,C),Fraction(4)), pscale(pmul(B,B),Fraction(-1)))
        den,ints=scaled(D)
        print(name+'_DISC_MARGIN',f"4AC-B^2=({list(reversed(ints))})/{den}")
print('ALL_EXACT_CHECKS_PASS')
