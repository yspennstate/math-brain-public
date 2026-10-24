#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import hashlib, json

TERMS=(0,1,2)  # a,b,c
CORE=[(0,1),(0,2)]

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda t:(t[0],len(t),t)))

def base_state(): return canon([{0},{1},{2}])

def bidx(st,v):
    for i,b in enumerate(st):
        if v in b:return i
    raise ValueError

def merge_edge(st,u,v):
    i,j=bidx(st,u),bidx(st,v)
    if i==j:return None
    bs=[set(b) for b in st]
    m=bs[i]|bs[j]
    return canon([bs[k] for k in range(len(bs)) if k not in (i,j)]+[m])

def star(st,S):
    inds=[bidx(st,v) for v in S]
    if len(set(inds))<len(inds):return None
    if len(S)<=1:return st
    bs=[set(b) for b in st]; I=set(inds)
    m=set().union(*(bs[i] for i in I))
    return canon([bs[k] for k in range(len(bs)) if k not in I]+[m])

STATES=[
    ((0,),(1,),(2,)),
    ((0,),(1,2)),
    ((0,1),(2,)),
    ((0,1,2),),
    ((0,2),(1,)),
]
IDX={s:i for i,s in enumerate(STATES)}
ALL_STARS=[tuple(i for i in TERMS if mask>>i&1) for mask in range(8)]

# reconstruct exact unmarked-star transfer
M=[[0]*5 for _ in range(5)]
for i,st in enumerate(STATES):
    for S in ALL_STARS:
        ns=star(st,S)
        if ns is not None:M[i][IDX[ns]]+=1
EXPECTED_M=[[4,1,1,1,1],[0,4,0,2,0],[0,0,4,2,0],[0,0,0,4,0],[0,0,0,2,4]]
assert M==EXPECTED_M
N=[[M[i][j]-(4 if i==j else 0) for j in range(5)] for i in range(5)]

def rowmul(v,A):return [sum(v[i]*A[i][j] for i in range(len(v))) for j in range(len(v))]
assert rowmul(rowmul(rowmul([1,2,3,4,5],N),N),N)==[0]*5

def enum_vec(k,forced_core=(),forced_stars=None):
    forced_core=set(forced_core); forced_stars=forced_stars or {}
    out=[0]*5
    for cmask in range(4):
        chosen={i for i in range(2) if cmask>>i&1}
        if not forced_core<=chosen:continue
        st=base_state(); ok=True
        for ci in sorted(chosen):
            st=merge_edge(st,*CORE[ci])
            if st is None:ok=False;break
        if not ok:continue
        stack=[st]
        for r in range(k):
            nxt=[]; req=set(forced_stars.get(r,()))
            for sst in stack:
                for S in ALL_STARS:
                    if not req<=set(S):continue
                    ns=star(sst,S)
                    if ns is not None:nxt.append(ns)
            stack=nxt
        for sst in stack:out[IDX[sst]]+=1
    return out

def padd(a,b):
    c=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def pscale(a,s):return [x*s for x in a]
def pmul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def binom_poly(j):
    p=[Fraction(1)]
    for t in range(j):p=pmul(p,[Fraction(-t),Fraction(1)])
    d=1
    for t in range(2,j+1):d*=t
    return pscale(p,Fraction(1,d))

def count_poly(v):
    # v M^x 1 / 4^x, exactly, with N^3=0
    p=[Fraction(0)]; cur=v[:]
    for j in range(3):
        p=padd(p,pscale(binom_poly(j),Fraction(sum(cur),4**j)))
        cur=rowmul(cur,N)
    assert cur==[0]*5
    return p

def gap_poly(v0,ve,vf,vef):
    z,e,f,ef=map(count_poly,(v0,ve,vf,vef))
    return padd(pmul(e,f),pscale(pmul(z,ef),-1))

def constraints(edges):
    fc=set(); fs=defaultdict(set)
    for e in edges:
        if e[0]=='c':fc.add(e[1])
        else:fs[e[1]].add(e[2])
    return fc,dict(fs)

ORBITS={
'XX':(('c',0),('c',1),0),
'YY':(('s',0,0),('s',1,0),2),
'ZZ_B':(('s',0,1),('s',1,1),2),
'ZZ_C':(('s',0,1),('s',0,2),1),
'ZZ_D':(('s',0,1),('s',1,2),2),
'XY':(('c',0),('s',0,0),1),
'XZ_B':(('c',0),('s',0,1),1),
'XZ_D':(('c',0),('s',0,2),1),
'YZ_C':(('s',0,0),('s',0,1),1),
'YZ_D':(('s',0,0),('s',1,1),2),
}
EXPECTED={
'XX':[Fraction(0),Fraction(3,16),Fraction(1,16)],
'YY':[Fraction(160),Fraction(457,8),Fraction(41,8)],
'ZZ_B':[Fraction(292),Fraction(617,8),Fraction(41,8)],
'ZZ_C':[Fraction(4),Fraction(37,4),Fraction(1097,256),Fraction(87,128),Fraction(9,256)],
'ZZ_D':[Fraction(158),Fraction(289,8),Fraction(17,8)],
'XY':[Fraction(18),Fraction(63,8),Fraction(7,8)],
'XZ_B':[Fraction(28),Fraction(79,8),Fraction(7,8)],
'XZ_D':[Fraction(4),Fraction(9,8),Fraction(1,8)],
'YZ_C':[Fraction(18),Fraction(243,16),Fraction(1241,256),Fraction(87,128),Fraction(9,256)],
'YZ_D':[Fraction(84),Fraction(209,8),Fraction(17,8)],
}
POLYS={}
for name,(e,f,k) in ORBITS.items():
    v0=enum_vec(k)
    fc,fs=constraints((e,));ve=enum_vec(k,fc,fs)
    fc,fs=constraints((f,));vf=enum_vec(k,fc,fs)
    fc,fs=constraints((e,f));vef=enum_vec(k,fc,fs)
    p=gap_poly(v0,ve,vf,vef)
    assert p==EXPECTED[name],(name,p)
    assert all(c>=0 for c in p)
    if name=='XX':assert p[0]==0 and all(c>0 for c in p[1:])
    else:assert all(c>0 for c in p)
    POLYS[name]=(k,p)

# brute-force original all-forests model for n=1,2,3 and every edge pair
def graph_edges(n):
    es=[(0,1),(0,2)]
    for r in range(n):
        v=3+r
        es.extend([(0,v),(1,v),(2,v)])
    return es

def forest_counts(n):
    es=graph_edges(n); V=3+n; m=len(es)
    Z=0; I=[0]*m; II=[[0]*m for _ in range(m)]
    for mask in range(1<<m):
        par=list(range(V))
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]];x=par[x]
            return x
        chosen=[];ok=True
        for i,(u,v) in enumerate(es):
            if mask>>i&1:
                a,b=find(u),find(v)
                if a==b:ok=False;break
                par[a]=b;chosen.append(i)
        if not ok:continue
        Z+=1
        for i in chosen:I[i]+=1
        for aa in range(len(chosen)):
            for bb in range(aa+1,len(chosen)):
                i,j=chosen[aa],chosen[bb];II[i][j]+=1;II[j][i]+=1
    return es,Z,I,II

def etype(e):
    u,v=e
    if v<3:return ('X',v)
    r=v-3
    if u==0:return ('Y',r)
    return ('Z',u,r)

def orbit(e,f):
    a,b=etype(e),etype(f)
    if a[0]>b[0]:a,b=b,a
    if a[0]=='X' and b[0]=='X':return 'XX'
    if a[0]=='Y' and b[0]=='Y':return 'YY'
    if a[0]=='Z' and b[0]=='Z':
        if a[1]==b[1]:return 'ZZ_B'
        if a[2]==b[2]:return 'ZZ_C'
        return 'ZZ_D'
    if a[0]=='X' and b[0]=='Y':return 'XY'
    if a[0]=='X' and b[0]=='Z':return 'XZ_B' if a[1]==b[1] else 'XZ_D'
    if a[0]=='Y' and b[0]=='Z':return 'YZ_C' if a[1]==b[2] else 'YZ_D'
    raise AssertionError((a,b))

def peval(p,x):return sum(c*(x**i) for i,c in enumerate(p))

for n in (1,2,3):
    es,Z,I,II=forest_counts(n)
    for i,j in combinations(range(len(es)),2):
        o=orbit(es[i],es[j]);k,p=POLYS[o]
        assert n>=k
        exact=I[i]*I[j]-Z*II[i][j]
        predicted=(16**(n-k))*peval(p,n-k)
        assert predicted.denominator==1 and exact==predicted.numerator,(n,es[i],es[j],o,exact,predicted)
        assert exact>0
    print('bruteforce_n',n,'Z',Z,'pairs',len(es)*(len(es)-1)//2,'ALL_MATCH_STRICT')

payload={name:{'k':k,'coeffs':[[c.numerator,c.denominator] for c in p]} for name,(k,p) in POLYS.items()}
digest=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('transfer_matrix',M)
for name in sorted(POLYS):
    k,p=POLYS[name]
    print(name,'k',k,'normalized_gap_coeffs_x=n-k',[str(c) for c in p])
print('certificate_sha256',digest)
print('THEOREM: uniform all-forests on K_{1,2,n} is strictly pairwise edge-negatively correlated for every n>=1')
print('PROB10_07_K12N_TRIPARTITE_EXACT_PASS')
