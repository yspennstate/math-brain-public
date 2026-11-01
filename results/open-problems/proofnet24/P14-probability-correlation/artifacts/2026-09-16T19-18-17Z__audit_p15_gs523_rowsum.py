#!/usr/bin/env python3
# Independent exact P14 audit of P15 §7 multiplier-order row-sum gate.
# Audited peer report:
# proofnet24/P15-hadamard/runs/2026-09-16/2026-09-16_19-23-52__run-report.md
# peer report blob 37945b4cb10910f9eaa31af76376fedbe91c26f7
# The peer report assigns no formal claim ID to this §7 gate; none is invented here.

import hashlib

TARGET=2092
P=523
NONZERO=P-1

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def row_sums(d):
    n=NONZERO//d
    vals=set()
    for j in range(n+1):
        S=n-2*j
        vals.add(1+d*S)
        vals.add(-1+d*S)
    return sorted(vals)

def four_square_hits(absvals):
    vals=[x for x in absvals if x*x<=TARGET]
    pairs={}
    for i,a in enumerate(vals):
        for b in vals[i:]:
            s=a*a+b*b
            if s<=TARGET:
                pairs.setdefault(s,[]).append((a,b))
    hits=set()
    for s,L in pairs.items():
        R=pairs.get(TARGET-s,())
        for a,b in L:
            for c,d in R:
                hits.add(tuple(sorted((a,b,c,d))))
    return sorted(hits)

def main():
    survivors=[]
    payload=[]
    for d in divisors(NONZERO):
        rs=row_sums(d)
        hits=four_square_hits(sorted({abs(r) for r in rs}))
        if hits:
            survivors.append(d)
        payload.append((d,tuple(hits)))
        print(f"d={d} orbit_count={NONZERO//d} row_sum_count={len(rs)} hit_count={len(hits)} hits={hits}")
    assert survivors==[1,2,3,6,9], survivors
    print("surviving_multiplier_orders="+repr(survivors))
    raw=repr(payload).encode()
    print("audit_payload_sha256="+hashlib.sha256(raw).hexdigest())
    print("AUDIT_VERDICT=PASS")
    print("SCOPE=necessary row-sum gate only; not a Hadamard existence/nonexistence certificate")

if __name__=="__main__":
    main()
