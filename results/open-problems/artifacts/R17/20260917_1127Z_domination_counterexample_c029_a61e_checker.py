#!/usr/bin/env python3
from functools import lru_cache
from collections import defaultdict

MAX_TOTAL = 13

@lru_cache(maxsize=None)
def lcs(a,b):
    dp=[0]*(len(b)+1)
    for x in a:
        nd=[0]*(len(b)+1)
        for j,y in enumerate(b,1):
            nd[j]=dp[j-1]+1 if x==y else max(dp[j],nd[j-1])
        dp=nd
    return dp[-1]

def minimal_match(a,b):
    if not a or not b or a[-1]!=b[-1]:
        return False
    if lcs(a,b)!=1:
        return False
    # For lcs=1, essential final match iff deleting either final symbol kills all matches.
    return lcs(a[:-1],b)==0 and lcs(a,b[:-1])==0

def string_from_mask(mask,n):
    # Last bit fixed to 0 by binary-complement symmetry.
    return ''.join(str((mask>>i)&1) for i in range(n-1))+'0'

def decompositions(X,Y):
    n,m=len(X),len(Y)
    good={}
    for i in range(n):
        for j in range(m):
            nxt=[]
            for ii in range(i+1,n+1):
                for jj in range(j+1,m+1):
                    if minimal_match(X[i:ii],Y[j:jj]):
                        nxt.append((ii,jj))
            good[(i,j)]=nxt
    out=[]
    def dfs(i,j,cuts):
        if i==n and j==m:
            out.append(tuple(cuts)); return
        for q in good.get((i,j),()):
            dfs(q[0],q[1],cuts+(q,))
    dfs(0,0,tuple())
    return out

def key(path):
    return tuple(reversed([i+j for i,j in path]))

pairs_checked=0
first_total=None
witnesses=[]
for total in range(2,MAX_TOTAL+1):
    local=[]
    for n in range(1,total):
        m=total-n
        if n>m: continue  # top/bottom swap symmetry
        for xm in range(1<<(n-1)):
            X=string_from_mask(xm,n)
            for ym in range(1<<(m-1)):
                Y=string_from_mask(ym,m)
                pairs_checked+=1
                ds=decompositions(X,Y)
                by_order=defaultdict(list)
                for p in ds:
                    by_order[len(p)].append(p)
                for r,ps in by_order.items():
                    mk=min(map(key,ps))
                    mins=[p for p in ps if key(p)==mk]
                    if len(mins)>=2:
                        local.append((X,Y,r,mk,mins,ps))
    print(f'total={total} counterexamples={len(local)}')
    if local:
        first_total=total
        witnesses=local
        break

assert first_total==13
X,Y,r,mk,mins,ps=witnesses[0]
assert (X,Y)==('110110','0010110')
assert r==4
assert mk==(13,10,7,4)
assert len(ps)==2 and len(mins)==2
assert lcs(X,Y)==5
assert lcs(X[:-1],Y)==4
assert lcs(X,Y[:-1])==4

print('FIRST_COUNTEREXAMPLE_TOTAL=13')
print('X='+X)
print('Y='+Y)
print('full_lcs='+str(lcs(X,Y)))
print('delete_top_last_lcs='+str(lcs(X[:-1],Y)))
print('delete_bottom_last_lcs='+str(lcs(X,Y[:-1])))
print('order='+str(r))
print('reverse_key='+','.join(map(str,mk)))
for idx,p in enumerate(mins,1):
    prev=(0,0); segs=[]
    for ii,jj in p:
        segs.append((X[prev[0]:ii],Y[prev[1]:jj]))
        prev=(ii,jj)
    print(f'list{idx}_cuts='+repr(p))
    print(f'list{idx}_segments='+repr(segs))
    assert all(minimal_match(a,b) for a,b in segs)
print('order4_total_lists=2')
print('order4_undominated_lists=2')
print('SMALLEST_TOTAL_SIZE_CERTIFIED=13')
print('EXACT_GENERIC_DEFINITION_CHECK_PASS')
