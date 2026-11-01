#!/usr/bin/env python3
"""Independent exact check of the Courtade-Kumar S_5 compression family.

No numerical entropy calculations. This verifies that the local two-coordinate
lex-compression constraints generate exactly 119 subsets, matching Table I of
Courtade-Kumar (2013), and records the frozen mask list hash.
"""
from itertools import combinations
import hashlib

n=5
N=1<<n
pred=[0]*N
for i,j in combinations(range(n),2):
    for base in range(N):
        if base & ((1<<i)|(1<<j)):
            continue
        v00=base
        v01=base|(1<<j)
        v10=base|(1<<i)
        v11=base|(1<<i)|(1<<j)
        pred[v01] |= 1<<v00
        pred[v10] |= 1<<v01
        pred[v11] |= 1<<v10
for _ in range(N):
    changed=False
    for v in range(N):
        q=pred[v]
        y=q
        while y:
            bit=y & -y
            b=bit.bit_length()-1
            q |= pred[b]
            y -= bit
        if q != pred[v]:
            pred[v]=q
            changed=True
    if not changed:
        break
succ=[0]*N
for u in range(N):
    y=pred[u]
    while y:
        bit=y&-y
        v=bit.bit_length()-1
        succ[v] |= 1<<u
        y-=bit

def minimal(avail):
    y=avail
    while y:
        bit=y&-y
        v=bit.bit_length()-1
        if pred[v]&avail == 0:
            return v
        y-=bit
    raise RuntimeError

out=[]
def rec(avail,inc):
    if avail==0:
        out.append(inc);return
    m=minimal(avail); bit=1<<m
    rec(avail & ~bit, inc|bit)
    rec(avail & ~bit & ~succ[m], inc)
rec((1<<N)-1,0)
out=sorted(set(out))
assert len(out)==119

def pair_compressed(mask):
    for i,j in combinations(range(n),2):
        for base in range(N):
            if base & ((1<<i)|(1<<j)):
                continue
            vs=[base,base|(1<<j),base|(1<<i),base|(1<<i)|(1<<j)]
            seen_zero=False
            for v in vs:
                inside=(mask>>v)&1
                if not inside:
                    seen_zero=True
                elif seen_zero:
                    return False
    return True
assert all(pair_compressed(m) for m in out)

full=(1<<N)-1
def is_dictator(mask):
    for i in range(n):
        d=sum((1<<x) for x in range(N) if (x>>i)&1)
        if mask==d or mask==(full^d):
            return True
    return False
constants=sum(m in (0,full) for m in out)
dictators=sum(is_dictator(m) for m in out)
nontrivial=119-constants-dictators
balanced_nontrivial=sum(m.bit_count()==16 and m not in (0,full) and not is_dictator(m) for m in out)

text='\n'.join(f'{m:08x}' for m in out)+'\n'
sha=hashlib.sha256(text.encode()).hexdigest()
print('S5_COMPRESSION_INDEPENDENT_CHECK: PASS')
print('count=119')
print(f'constants={constants}')
print(f'dictators={dictators}')
print(f'nontrivial={nontrivial}')
print(f'balanced_nontrivial={balanced_nontrivial}')
print(f'mask_list_sha256={sha}')
print('first_mask='+f'{out[0]:08x}')
print('last_mask='+f'{out[-1]:08x}')
