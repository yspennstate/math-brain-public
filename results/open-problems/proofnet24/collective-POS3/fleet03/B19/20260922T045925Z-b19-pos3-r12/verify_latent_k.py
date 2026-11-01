#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations
from math import comb

M = 8
# Core labels: e=0,d=1,x=2,y=3,u=4; residual chain is 5,...,4+M.
E0,D,X,Y,U = 0,1,2,3,4

def build(m):
    n=5+m
    edges=[(E0,X),(E0,Y),(D,Y),(D,U),(X,U)]
    if m:
        edges.append((E0,5))
        for r in range(5,5+m-1):
            edges.append((r,r+1))
        edges.append((4+m,U))
    succ=[0]*n
    for a,b in edges:
        succ[a] |= 1<<b
    for k in range(n):
        kb=1<<k
        for i in range(n):
            if succ[i]&kb:
                succ[i] |= succ[k]
    pred=[0]*n
    for i in range(n):
        for j in range(n):
            if (succ[i]>>j)&1:
                pred[j] |= 1<<i
    return n,edges,succ,pred

def extension_count(n,pred):
    @lru_cache(None)
    def dp(rem):
        if rem==0: return 1
        total=0
        m=rem
        while m:
            bit=m&-m
            v=bit.bit_length()-1
            if pred[v]&rem==0:
                total += dp(rem^bit)
            m-=bit
        return total
    return dp((1<<n)-1)

def with_relations(n,succ,pred,rels):
    edges=[]
    for i in range(n):
        for j in range(n):
            if (succ[i]>>j)&1:
                edges.append((i,j))
    edges.extend(rels)
    ns=[0]*n
    for a,b in edges:
        if a==b: return None
        ns[a] |= 1<<b
    for k in range(n):
        kb=1<<k
        for i in range(n):
            if ns[i]&kb:
                ns[i] |= ns[k]
    if any((ns[i]>>i)&1 for i in range(n)):
        return None
    np=[0]*n
    for i in range(n):
        for j in range(n):
            if (ns[i]>>j)&1:
                np[j]|=1<<i
    return ns,np

def count_word(n,succ,pred,word):
    rel=[(word[i],word[i+1]) for i in range(len(word)-1)]
    q=with_relations(n,succ,pred,rel)
    return 0 if q is None else extension_count(n,q[1])

def count_before(n,succ,pred,a,b):
    if (succ[a]>>b)&1: return extension_count(n,pred)
    if (succ[b]>>a)&1: return 0
    q=with_relations(n,succ,pred,[(a,b)])
    return extension_count(n,q[1])

def predset(pred,v):
    return {i for i in range(len(pred)) if (pred[v]>>i)&1}
def succset(succ,v):
    return {i for i in range(len(succ)) if (succ[v]>>i)&1}

def width(n,succ):
    best=0; witness=()
    for r in range(1,n+1):
        ok=None
        for S in combinations(range(n),r):
            if all(not ((succ[a]>>b)&1) and not ((succ[b]>>a)&1)
                   for a,b in combinations(S,2)):
                ok=S; break
        if ok is None: break
        best=r; witness=ok
    return best,witness

def six_words(n,succ,pred):
    pats=[
        (D,Y,X,U), (D,X,Y,U), (D,X,U,Y),
        (X,D,Y,U), (X,D,U,Y), (X,U,D,Y)
    ]
    return tuple(count_word(n,succ,pred,p) for p in pats)

# Exact ideal-state checks against the closed family formulas for m=0,...,8.
for m in range(0,M+1):
    n,edges,succ,pred=build(m)
    ext=extension_count(n,pred)
    p=comb(m+3,3)
    q=comb(m+2,2)
    r=m+1
    expected_words=(p+q,p+q,q+r,p,q,0)
    words=six_words(n,succ,pred)
    assert words==expected_words,(m,words,expected_words)
    expected_E=3*p+4*q+r
    assert ext==expected_E,(m,ext,expected_E)

# Targeted m=8 certificate.
n,edges,succ,pred=build(M)
EE=extension_count(n,pred)
assert EE==684
assert predset(pred,Y)==predset(pred,X)|{D}
assert succset(succ,X)==succset(succ,Y)|{U}
assert predset(pred,X)==predset(pred,D)|{E0}
assert succset(succ,D)==succset(succ,X)|{Y}
assert (succ[D]>>U)&1
ww=six_words(n,succ,pred)
A,C,Xw,Yw,Z,W=ww
assert ww==(210,210,54,165,45,0)
K=A+Z
assert K==255
assert 3*K-EE==81==(M+1)**2
assert 8*K < 3*EE                    # disproves K >= 3E/8
assert 3*K > EE                      # but K > E/3
minor_xy=count_before(n,succ,pred,Y,X)
minor_dx=count_before(n,succ,pred,X,D)
assert minor_xy==A==210
assert minor_dx==210
assert 3*A < EE                      # both corridor endpoints remain unbalanced
wd,wit=width(n,succ)
assert wd==3

balanced=[]
for a,b in combinations(range(n),2):
    if (succ[a]>>b)&1 or (succ[b]>>a)&1:
        continue
    c=count_before(n,succ,pred,a,b)
    q=min(c,EE-c)
    if 3*q>=EE:
        balanced.append((a,b,c,q))
assert balanced
assert (D,6,306,306) in balanced

# Exact formulas and asymptotic identity.
# p=C(m+3,3), q=C(m+2,2), r=m+1:
# E_m=3p+4q+r, K_m=p+2q, so 3K_m-E_m=(m+1)^2.
for m in (0,1,2,8,10,50,100,1000):
    p=comb(m+3,3); q=comb(m+2,2); r=m+1
    Ef=3*p+4*q+r
    Kf=p+2*q
    assert 3*Kf-Ef==(m+1)**2
    assert 3*Kf>Ef

print("family_m",M)
print("extensions",EE)
print("width",wd,"witness",wit)
print("six_words_A_C_X_Y_Z_W",*ww)
print("corridor_minorities",minor_xy,minor_dx)
print("K",K,"K_over_E",f"{K}/{EE}")
print("threeK_minus_E",3*K-EE)
print("refutes_K_ge_3E_over_8",8*K,3*EE)
print("balanced_sample_d_r2",count_before(n,succ,pred,D,6),"/",EE)
print("balanced_pair_count",len(balanced))
print("formula_E","3*C(m+3,3)+4*C(m+2,2)+(m+1)")
print("formula_K","C(m+3,3)+2*C(m+2,2)")
print("formula_3K_minus_E","(m+1)^2")
print("limit_K_over_E","1/3_from_above")
print("POS3_B19_LATENT_K_SHARPNESS_PASS")
