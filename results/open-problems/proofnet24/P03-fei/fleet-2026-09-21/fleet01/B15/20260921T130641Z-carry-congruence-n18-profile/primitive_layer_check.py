#!/usr/bin/env python3
"""Primitive valuation-layer check for the n=18 FEI magnitude packets."""
from collections import defaultdict
from fractions import Fraction
import numpy as np
import n18_packet_carry_profile as base

def main():
    table,_=base.reconstruct()
    n=18; N=1<<n
    W=base.fwht(table)
    groups=defaultdict(list)
    for s,w in enumerate(W):
        if w:
            groups[abs(int(w))].append((s,1 if w>0 else -1))
    rows=[]
    for mag,entries in sorted(groups.items()):
        spec=np.zeros(N,dtype=np.int64)
        for s,c in entries:
            spec[s]=c
        V=base.fwht(spec)
        nz=V[V!=0]
        r=min(base.v2(z) for z in nz)
        primitive=sum(1 for z in nz if base.v2(z)==r)
        lower=1<<(n-r)
        assert primitive>=lower
        rows.append((mag,len(entries),r,primitive,lower,Fraction(primitive,N)))
    print("magnitude multiplicity r primitive lower_bound primitive_fraction")
    for row in rows:
        print(*row)
    print("PASS packets=",len(rows))

if __name__=="__main__":
    main()
