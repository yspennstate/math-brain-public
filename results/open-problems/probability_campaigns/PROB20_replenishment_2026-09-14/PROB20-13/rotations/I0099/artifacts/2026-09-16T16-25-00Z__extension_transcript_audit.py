#!/usr/bin/env python3
import re, sys
from pathlib import Path

LOW_EXCLUSIVE = 1801
HIGH_INCLUSIVE = 2333
TRANSCRIPT = Path(sys.argv[1])

def isprime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

pat = re.compile(
    r'^p=(\d+) omega=(\d+) Hn=(\d+) witness=([^ ]+) '
    r'exclude=(\d+) targetH=(\d+) max_nodes=(\d+) no_nodes=(\d+) '
    r'prunes=(\d+) leaves=(\d+) proof64=([0-9a-f]+)$'
)

rows = []
for line in TRANSCRIPT.read_text(encoding="utf-8").splitlines():
    m = pat.match(line)
    if not m:
        continue
    p, omega, hn = map(int, m.group(1,2,3))
    W = [int(x) for x in m.group(4).split(",")]
    exclude, targetH, max_nodes, no_nodes, prunes, leaves = map(int, m.group(5,6,7,8,9,10))
    proof64 = m.group(11)
    rows.append((p,omega,hn,W,exclude,targetH,max_nodes,no_nodes,prunes,leaves,proof64))

expected = [p for p in range(LOW_EXCLUSIVE+1, HIGH_INCLUSIVE+1) if p % 4 == 1 and isprime(p)]
seen = [r[0] for r in rows]
assert seen == expected, (seen, expected)

for p,omega,hn,W,exclude,targetH,max_nodes,no_nodes,prunes,leaves,proof64 in rows:
    assert hn == (p-5)//4
    assert len(W) == omega
    assert W[:2] == [0,1]
    assert len(set(W)) == omega
    qr = {x*x % p for x in range(1,p)}
    for i in range(omega):
        for j in range(i):
            assert (W[i]-W[j]) % p in qr
    assert exclude == omega + 1
    assert targetH == omega - 1
    assert max_nodes > 0 and no_nodes > 0 and prunes > 0
    assert leaves == 0
    assert 1 <= len(proof64) <= 16
    int(proof64, 16)

mx = max(r[1] for r in rows)
mxps = [r[0] for r in rows if r[1] == mx]
print(f"ROWS={len(rows)} FIRST={seen[0]} LAST={seen[-1]}")
print("COVERAGE_ALL_ADMISSIBLE_PRIMES_1802_2333=PASS")
print("ALL_HN_FORMULAS=PASS")
print("ALL_WITNESSES_PAIRWISE_QR=PASS")
print("ALL_EXCLUDE_TARGET_FIELDS=PASS")
print("ALL_SEARCH_TRANSCRIPTS_REPORT_ONE_LARGER_EXCLUSION=PASS")
print(f"MAX_OMEGA_EXTENSION={mx} MAX_PRIMES={mxps}")
print("EXTENSION_TRANSCRIPT_AUDIT_PASS")
