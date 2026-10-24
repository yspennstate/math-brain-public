"""Reconstruct Numaro's published n=18 seed from ten 512-bit slices.

Data source: https://numaro.tech/assets/research/fei/check_c71_n18.py
Fetched 2026-09-21. Slice y=0 and y=2**j, lines 1073-1074 and
1073-2**(j+1) through 1074-2**(j+1), zero-based web line numbering.
The auxiliary-host representation is accepted ONLY if the whole regenerated
262144-value truth-table SHA256 matches the published digest.
This is recovery of EXTERNAL work, not an original lower-bound claim.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import numpy as np
from cancellation_composition import walsh_state, fwht

EXPECTED_SHA = 'f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839'
TOP = 'fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00'
BOT = 'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
# Factual truth-table slices, not imported execution code.
SLICES = [
 (TOP, BOT),
 (TOP, 'fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000'),
 (TOP, 'fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000'),
 ('fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00', 'fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP, 'fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000'),
 (TOP, 'fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000'),
 ('fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00', BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00', BOT),
 ('fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00', BOT),
 ('fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00', BOT),
]


def core_and_hosts():
    if any(len(x) != 64 for t in SLICES for x in t):
        raise ValueError('Each slice half must contain exactly 64 hex digits')
    base = int(''.join(SLICES[0]),16)
    masks = [int(''.join(row),16) ^ base for row in SLICES[1:]]
    if any(m & base for m in masks) or any(m.bit_count()!=2 for m in masks):
        raise AssertionError('The recovered slices do not have disjoint two-cell hosts')
    seen=base
    hosts=[]
    for m in masks:
        if seen & m: raise AssertionError('Overlapping auxiliary host supports')
        seen |= m
        hosts.append([x for x in range(512) if m>>x&1])
    return base, hosts


def make_table(base: int, hosts: list[list[int]]) -> np.ndarray:
    naux=len(hosts)
    core=np.array([-1 if base>>x&1 else 1 for x in range(512)],dtype=np.int64)
    result=np.tile(core, (1<<naux,1))
    for j, cells in enumerate(hosts):
        mask=(np.arange(1<<naux) & (1<<j)) != 0
        result[np.ix_(mask, np.array(cells,dtype=int))]=-1
    return result.ravel()


def check() -> tuple[dict,np.ndarray]:
    base,hosts=core_and_hosts()
    table=make_table(base,hosts)
    digest=hashlib.sha256(','.join(map(str,table)).encode()).hexdigest()
    if digest != EXPECTED_SHA:
        raise AssertionError(('Recovered truth table does not match external source',digest))
    n=18; bad=0; changes=0
    for j in range(n):
        s=table.reshape(-1,2,1<<j)
        lo,hi=s[:,0,:],s[:,1,:]
        bad += int(np.count_nonzero((lo==-1)&(hi==1)))
        changes += int(np.count_nonzero(lo!=hi))
    W=fwht(table)
    exact_influence_numerator=sum(int(x*x)*s.bit_count() for s,x in enumerate(W))
    from fractions import Fraction
    I=Fraction(exact_influence_numerator,len(table)**2)
    assert I==Fraction(261,128)
    assert Fraction(changes,1<<17)==I
    assert bad==0 and int(table.sum())==0
    metrics=walsh_state(table).as_dict()
    return {'external_source': 'Numaro NUMARO-2026-016 (2026-07-22)',
            'source_url':'https://numaro.tech/assets/research/fei/check_c71_n18.py',
            'source_table_sha256':EXPECTED_SHA,'reconstructed_sha256':digest,
            'core_true_hex':format(base,'0128x'),'auxiliary_hosts':hosts,
            'balance_sum':int(table.sum()), 'monotonicity_violations':bad,
            'coordinate_edges_checked':n*(1<<(n-1)),
            'I_exact':str(I),'influence_edge_and_fourier_agree':True,
            'nonzero_fourier_coefficients':int(np.count_nonzero(W)),
            'metrics_exploratory_float':metrics,
            'amplified_ratio_float':metrics['H']/(float(I)-1),
            'note':'Independent recovery of published work, not new FEI progress; entropy floats are not the rigorous final endpoints.'},table


if __name__=='__main__':
    report,table=check()
    root=Path(__file__).resolve().parent
    (root/'external_seed_recovery.json').write_text(json.dumps(report,indent=2)+'\n')
    np.save(root/'external_n18_table.npy',table.astype(np.int8))
    print(json.dumps(report,indent=2))
