#!/usr/bin/env python3
import re, sys
from pathlib import Path

LOW_EXCLUSIVE = 2333
HIGH_INCLUSIVE = 2729
TRANSCRIPT = Path(sys.argv[1])

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

pat = re.compile(
    r'^p=(\d+) omega=(\d+) Hn=(\d+) witness=([^ ]+) '
    r'exclude=(\d+) targetH=(\d+) max_nodes=(\d+) no_nodes=(\d+) '
    r'prunes=(\d+) leaves=(\d+) proof64=([0-9a-f]+)$'
)
rows=[]
for line in TRANSCRIPT.read_text().splitlines():
    m=pat.match(line)
    if not m: continue
    p,om,hn=map(int,m.group(1,2,3))
    W=[int(x) for x in m.group(4).split(',')]
    ex,tgt,mn,nn,pr,lf=map(int,m.group(5,6,7,8,9,10))
    h=m.group(11)
    rows.append((p,om,hn,W,ex,tgt,mn,nn,pr,lf,h))

expected=[p for p in range(LOW_EXCLUSIVE+1,HIGH_INCLUSIVE+1) if p%4==1 and isprime(p)]
seen=[r[0] for r in rows]
assert seen == expected, (seen, expected)
for p,om,hn,W,ex,tgt,mn,nn,pr,lf,h in rows:
    assert hn == (p-5)//4
    assert len(W) == om
    assert W[:2] == [0,1]
    assert len(set(W)) == om
    qr={x*x%p for x in range(1,p)}
    for i in range(om):
        for j in range(i):
            assert (W[i]-W[j])%p in qr, (p,W[i],W[j])
    assert ex == om+1
    assert tgt == om-1
    assert mn > 0 and nn > 0 and pr > 0
    assert lf >= 0
    assert 1 <= len(h) <= 16
    int(h,16)
mx=max(r[1] for r in rows); mxps=[r[0] for r in rows if r[1]==mx]
print(f'ROWS={len(rows)} FIRST={seen[0]} LAST={seen[-1]}')
print('COVERAGE_ALL_ADMISSIBLE_PRIMES_2334_2729=PASS')
print('ALL_HN_FORMULAS=PASS')
print('ALL_WITNESSES_PAIRWISE_QR=PASS')
print('ALL_EXCLUDE_TARGET_FIELDS=PASS')
print('ALL_SEARCH_ACCOUNTING_FIELDS_WELL_FORMED=PASS')
print(f'MAX_OMEGA_EXTENSION={mx} MAX_PRIMES={mxps}')
print('NOTE=This audit verifies coverage and witnesses; nonexistence is certified by the executed deterministic exact decision solver, not by this transcript parser alone.')
print('EXTENSION_AUDIT_PASS')
