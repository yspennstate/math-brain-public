#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
import re, sys
TRANSCRIPT=Path(sys.argv[1])
LO=3389; HI=3541
EXPECTED_OMEGA={3413:15,3433:17,3449:15,3457:17,3461:16,3469:17,3517:17,3529:19,3533:16,3541:15}

def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def qrset(p): return {x*x%p for x in range(1,p)}
text=TRANSCRIPT.read_text()
expected=[p for p in range(LO+1,HI+1) if p%4==1 and isprime(p)]
assert expected==list(EXPECTED_OMEGA), (expected,list(EXPECTED_OMEGA))
prime_blocks=re.split(r'(?=^=== PRIME )',text,flags=re.M)
prime_blocks=[b for b in prime_blocks if b.startswith('=== PRIME ')]
seen=[]
for block in prime_blocks:
    mh=re.match(r'=== PRIME p=(\d+) omega=(\d+) ===',block)
    assert mh
    p,om=map(int,mh.groups()); seen.append(p); assert EXPECTED_OMEGA[p]==om
    qr=qrset(p)
    witness_lines=re.findall(r'^I0099_V4_WITNESS p=(\d+) omega=(\d+) Hn=(\d+) witness=([^ ]+) witness_nodes=(\d+)$',block,re.M)
    assert witness_lines
    witnesses=[]
    for pp,oo,hn,ws,nodes in witness_lines:
        assert int(pp)==p and int(oo)==om and int(hn)==(p-5)//4 and int(nodes)>0
        W=tuple(map(int,ws.split(','))); assert len(W)==om and len(set(W))==om and W[:2]==(0,1)
        for i in range(len(W)):
            for j in range(i): assert (W[i]-W[j])%p in qr
        witnesses.append(W)
    assert all(W==witnesses[0] for W in witnesses)
    W=witnesses[0]
    def chi(z):
        z%=p
        return 0 if z==0 else (1 if z in qr else -1)
    Sv=[sum(chi(x-a) for a in W) for x in range(p)]
    m2=sum(s*s for s in Sv); m4=sum(s**4 for s in Sv)
    assert m2==om*(p-om)
    ratio=Fraction(m4,p*om*om)
    print(f'MOMENT p={p} omega={om} M2={m2} M4={m4} M4_over_p_k2={ratio.numerator}/{ratio.denominator} approx={float(ratio):.12f}')
    cert_headers=re.findall(r'^I0099_V4_CERT p=(\d+) omega=(\d+) Hn=(\d+) s3reps=(\d+)$',block,re.M)
    assert cert_headers
    reps={int(x[3]) for x in cert_headers}; assert len(reps)==1; reps=reps.pop()
    ranges=[]
    for m in re.finditer(r'^=== CHUNK s3=(\d+)\.\.(\d+) exit=(\S+).*?^CERTIFIED_V4_RANGE p=(\d+) omega=(\d+) s3=(\d+)\.\.(\d+) all_no_one_larger=1 obligations=(\d+) total_nodes=(\d+) proof64=([0-9a-f]+) seconds=([0-9.]+)$',block,re.M|re.S):
        a,b,ec,pp,oo,a2,b2,obl,nodes,h,sec=m.groups()
        a,b,a2,b2,pp,oo,obl,nodes=int(a),int(b),int(a2),int(b2),int(pp),int(oo),int(obl),int(nodes)
        assert ec=='0' and pp==p and oo==om and (a,b)==(a2,b2) and obl>0 and nodes>0 and int(h,16)>=0
        ranges.append((a,b))
    ranges.sort(); assert ranges and ranges[0][0]==0 and ranges[-1][1]==reps
    for (a,b),(c,d) in zip(ranges,ranges[1:]): assert b==c
    assert sum(b-a for a,b in ranges)==reps
assert seen==expected
print(f'PRIMES={len(seen)} FIRST={seen[0]} LAST={seen[-1]}')
print('ALL_ADMISSIBLE_PRIMES_IN_INTERVAL_PRESENT=PASS')
print('ALL_CHUNK_EXIT_CODES_ZERO=PASS')
print('ALL_S3_RANGES_EXACT_PARTITION=PASS')
print('ALL_WITNESSES_PAIRWISE_QUADRATIC_RESIDUE=PASS')
print('ALL_ONE_LARGER_EXCLUSIONS_COMPLETED=PASS')
print('I0099_EXTENSION_AUDIT_PASS')
