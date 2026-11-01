#!/usr/bin/env python3
import re, sys
from pathlib import Path

TRANSCRIPT = Path(sys.argv[1] if len(sys.argv) > 1 else 'i0099_exact_through_1801.out')
text = TRANSCRIPT.read_text(encoding='utf-8')
rows = []
pat = re.compile(r'^p=(\d+) omega=(\d+) Hn=(\d+) witness=([^ ]+) exclude=(\d+) targetH=(\d+) max_nodes=(\d+) no_nodes=(\d+) prunes=(\d+) leaves=(\d+) proof64=([0-9a-f]+)$')
for line in text.splitlines():
    m = pat.match(line)
    if not m:
        continue
    p,omega,hn = map(int,m.group(1,2,3))
    witness = [int(x) for x in m.group(4).split(',')]
    exclude,targetH,max_nodes,no_nodes,prunes,leaves = map(int,m.group(5,6,7,8,9,10))
    proof64=m.group(11)
    rows.append((p,omega,hn,witness,exclude,targetH,max_nodes,no_nodes,prunes,leaves,proof64))

def isprime(n):
    if n < 2: return False
    d=2
    while d*d <= n:
        if n%d==0: return False
        d += 1 if d==2 else 2
    return True

expected=[p for p in range(5,1802) if p%4==1 and isprime(p)]
seen=[r[0] for r in rows]
assert seen == expected, (len(seen), len(expected), set(expected)-set(seen), set(seen)-set(expected))
assert len(rows)==136
for p,omega,hn,W,exclude,targetH,max_nodes,no_nodes,prunes,leaves,proof64 in rows:
    assert hn == (p-5)//4
    assert len(W)==omega and W[:2]==[0,1] and len(set(W))==omega
    qr={x*x%p for x in range(1,p)}
    for i in range(omega):
        for j in range(i):
            assert (W[i]-W[j])%p in qr
    assert exclude == omega+1
    assert targetH == omega-1
    assert max_nodes >= 1 and no_nodes >= 1 and prunes >= 1
    assert 1 <= len(proof64) <= 16 and int(proof64,16)>=0
mx=max(r[1] for r in rows)
mxps=[r[0] for r in rows if r[1]==mx]
assert mx==17 and mxps==[1741]
print(f'ROWS={len(rows)} FIRST={seen[0]} LAST={seen[-1]}')
print('COVERAGE_ALL_ADMISSIBLE_PRIMES_THROUGH_1801=PASS')
print('ALL_HN_FORMULAS=PASS')
print('ALL_WITNESSES_PAIRWISE_QR=PASS')
print('ALL_EXCLUDE_TARGET_FIELDS=PASS')
print(f'MAX_OMEGA={mx} MAX_PRIMES={mxps}')
print('TRANSCRIPT_AUDIT_PASS')
