"""Exact extension certificate for PROB20-12 quintic orbits.

Run beside 2026-09-15T225648Z__quintic_obstruction_certificate.py.
It reuses that exact state/marginal/cubic table and certifies four further
S6 x S3 orbits of indispensable degree-5 two-monomial fibers.
"""
from pathlib import Path
import runpy, itertools
import numpy as np

base=runpy.run_path(str(Path(__file__).with_name(
    '2026-09-15T225648Z__quintic_obstruction_certificate.py')))
CODES=base['CODES']; D3=base['D3']; GENS=base['GENS']; relkey=base['relkey']
lam=base['lam']

SEEDS=[
 ((13,49,50,63,77),(21,37,51,72,76)),
 ((36,50,65,68,73),(38,48,63,66,76)),
 ((1,9,16,54,69),(5,10,21,33,81)),
 ((30,36,44,56,57),(32,33,45,53,59)),
 ((6,13,43,78,82),(7,9,46,74,81)),
]
EXPECTED=[(1080,2),(2160,2),(2160,1),(216,0),(1080,0)]
ORBS=[]
for (P,N),(want_size,want_cls) in zip(SEEDS,EXPECTED):
    target=sum(CODES[s] for s in P)
    assert target==sum(CODES[s] for s in N)
    # Complete degree-5 fiber enumeration by all 2+3 decompositions.
    fib=set()
    for pair in itertools.combinations_with_replacement(range(90),2):
        rem=target-CODES[pair[0]]-CODES[pair[1]]
        for tri in D3.get(rem,()):
            q=tuple(sorted(pair+tri))
            if sum(CODES[s] for s in q)==target:
                fib.add(q)
    assert fib=={tuple(sorted(P)),tuple(sorted(N))}
    assert set(P).isdisjoint(N)

    seed=relkey(P,N); orb={seed}; stack=[seed]
    while stack:
        p,n=stack.pop()
        for g in GENS:
            k=relkey([g[s] for s in p],[g[s] for s in n])
            if k not in orb:
                orb.add(k); stack.append(k)
    assert len(orb)==want_size

    z=np.zeros(90,dtype=int)
    for s in P: z[s]+=1
    for s in N: z[s]-=1
    cls=int(lam@z)%3
    assert cls==want_cls
    ORBS.append(orb)
    print('seed',seed,'fiber',len(fib),'orbit',len(orb),'class',cls)

for i in range(len(ORBS)):
    for j in range(i):
        assert ORBS[i].isdisjoint(ORBS[j])
assert sum(map(len,ORBS))==6696
print('total_certified_quintics',6696)
print('ALL FIVE QUINTIC ORBITS EXACTLY CERTIFIED')
