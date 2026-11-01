#!/usr/bin/env python3
"""Exact arithmetic check of the documented frontier 2060..2092.

Source convention (Cati-Pasechnik Table 4 v2): for odd n<=2999, an entry
n(m) gives the least exponent m with H(2^m n) recorded known; absent n means
m=2.  The only table entries needed in this interval are 515(3), 523(3);
the intervening odd parts below are absent in the machine-diffed transcription
JD-Jones-ASES/Hadamard-T data/cp-table4-v2.json @
1699c317e6c6515962ba48c4b5e35ab2ea225bab.

A separate exact P15 checker has verified a public H(2060), so 2060 is treated
as a 2026 override.  This is a documented-status computation, not a proof that
no unrecorded H(2092) exists in the world literature.
"""

TABLE = {515: 3, 523: 3}
ABSENT_RELEVANT = {65, 129, 259, 261, 517, 519, 521}
OVERRIDE_KNOWN = {2060}


def oddpart_and_v2(N):
    a = 0
    n = N
    while n % 2 == 0:
        a += 1
        n //= 2
    return n, a

rows=[]
for N in range(2060, 2093, 4):
    n,a = oddpart_and_v2(N)
    assert n % 2 == 1
    if n in TABLE:
        m = TABLE[n]
        source = f"table:{n}({m})"
    else:
        assert n in ABSENT_RELEVANT
        m = 2
        source = f"table-absent:{n}->m=2"
    known_by_table = a >= m
    known = known_by_table or N in OVERRIDE_KNOWN
    rows.append((N,n,a,m,known_by_table,N in OVERRIDE_KNOWN,known,source))

for row in rows:
    N,n,a,m,k0,ov,k,src=row
    print(f"N={N} oddpart={n} v2={a} table_min_m={m} table_known={k0} override2060={ov} documented_known={k} source={src}")

unknown=[N for N,_,_,_,_,_,k,_ in rows if not k]
assert unknown == [2092]
print("documented_unresolved_in_interval=2092")
print("EXACT_FRONTIER_ARITHMETIC_PASS")
print("SCOPE: combines a dated table transcription with an exact H2060 override; not a global nonexistence claim for H2092.")
