#!/usr/bin/env python3
"""Independent S_6 pair-compressed family enumerator for PROB20-21.

This does NOT evaluate mutual information. It independently reconstructs the
Courtade--Kumar source family S_6 as order ideals of the singleton and pair
lex-compression implications, checks every section directly, and emits a
frozen sorted-mask SHA-256.
"""
from hashlib import sha256

NV=6
N=1<<NV
FULL=(1<<N)-1

succ=[0]*N
for i in range(NV):
    for base in range(N):
        if ((base>>i)&1)==0:
            u=base; v=base|(1<<i)
            succ[u] |= 1<<v
for i in range(NV):
    for j in range(i+1,NV):
        for base in range(N):
            if ((base>>i)&1)==0 and ((base>>j)&1)==0:
                # section order 00 < 01 < 10 < 11; membership is initial segment.
                u=base|(1<<j)
                v=base|(1<<i)
                succ[u] |= 1<<v

for k in range(N):
    bk=1<<k
    for i in range(N):
        if succ[i]&bk:
            succ[i] |= succ[k]

pred=[0]*N
for u in range(N):
    z=succ[u]
    while z:
        l=z & -z
        v=l.bit_length()-1
        pred[v] |= 1<<u
        z-=l
pm=[pred[v]|(1<<v) for v in range(N)]
sm=[succ[v]|(1<<v) for v in range(N)]

out=[]
def rec(inc,exc):
    undec=FULL & ~(inc|exc)
    if not undec:
        out.append(inc); return
    best=None; score=-1
    z=undec
    while z:
        l=z & -z; v=l.bit_length()-1; z-=l
        sc=(pm[v]&undec).bit_count()+(sm[v]&undec).bit_count()
        if sc>score: score=sc; best=v
    if pm[best]&exc == 0:
        rec(inc|pm[best],exc)
    if sm[best]&inc == 0:
        rec(inc,exc|sm[best])

rec(0,0)
out=sorted(set(out))

def direct(m):
    for i in range(NV):
        for base in range(N):
            if (base>>i)&1: continue
            a=(m>>base)&1
            b=(m>>(base|(1<<i)))&1
            if a<b: return False
    for i in range(NV):
        for j in range(i+1,NV):
            for base in range(N):
                if (base>>i)&1 or (base>>j)&1: continue
                q=[base,base|(1<<j),base|(1<<i),base|(1<<i)|(1<<j)]
                vals=[(m>>x)&1 for x in q]
                if any(vals[k]<vals[k+1] for k in range(3)):
                    return False
    return True

assert len(out)==1173
assert all(direct(m) for m in out)
payload=''.join(f'{m:016x}\n' for m in out).encode()
print('S6_INDEPENDENT_ENUMERATION=PASS')
print('candidate_count=',len(out))
print('sorted_mask_sha256=',sha256(payload).hexdigest(),sep='')
print('first_mask=',f'{out[0]:016x}',sep='')
print('last_mask=',f'{out[-1]:016x}',sep='')
print('balanced_count=',sum(m.bit_count()==32 for m in out),sep='')
