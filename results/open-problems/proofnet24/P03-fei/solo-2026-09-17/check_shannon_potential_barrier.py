#!/usr/bin/env python3
"""Exact checks for SHANNON_POTENTIAL_BARRIER_2026-09-18.md."""
from fractions import Fraction as F
from pathlib import Path
import json

from certify_nand80 import IV, h, LN2_LO, LN2_HI, rational_interval
from check_logarithmic_structures import indicator_metrics, kedge, log2, overlap
from check_unequal_nand_potential import potential


def bent_values(m):
    return [1 if sum(((x >> (2*j)) & 1)*((x >> (2*j+1)) & 1)
                         for j in range(m//2)) % 2 == 0 else -1
            for x in range(1 << m)]


def cterm(q):
    return IV(2*q/LN2_HI, 2*q/LN2_LO)


def formulas(m):
    N = 1 << m
    rootN = 1 << (m//2)
    e = F(1, rootN)
    q = e*e/4
    xp = e*e*(1-2*e)**2/4
    xm = e*e*(1+2*e)**2/4
    zp = e*e*(1-e)**2/4
    zm = e*e*(1+e)**2/4
    y = e**4/4
    nplus = (N+rootN)//2
    nminus = (N-rootN)//2
    V0 = m*h(q)+cterm(m*q)
    V1 = F(m*N,4)*kedge(xp,xm)+m*h(xp)+cterm(m*xp)
    kdata = F(m*N,4)*kedge(zp,zm)
    kselector = y*((nplus-1)*log2(zp/y)+nminus*log2(zm/y))
    VA = kdata+kselector+m*h(zp)+h(y)+cterm(m*zp+y)
    return V0,V1,VA


def main():
    rows=[]
    for m in range(2,13,2):
        N=1<<m
        g=bent_values(m)
        gp=g[:]; gp[0]*=-1
        a0=[(1-v)//2 for v in g]
        a1=[(1-v)//2 for v in gp]
        a=a0+a1
        p0=potential(indicator_metrics(a0))[-1]
        p1=potential(indicator_metrics(a1))[-1]
        pa=potential(indicator_metrics(a))[-1]
        f0,f1,fa=formulas(m)
        overlap(p0,f0);overlap(p1,f1);overlap(pa,fa)
        defect=pa-(p0+p1)*F(1,2)
        assert defect.lo>0
        rows.append({'m':m,'N':N,'selector_influence_exact':str(F(1,N)),
                     'V_A_interval':rational_interval(pa),
                     'restriction_defect_interval':rational_interval(defect),
                     'defect_over_selector_influence_interval':
                        rational_interval(defect*N)})
    result={'status':'PASS',
            'arithmetic':'exact rational arithmetic and 160-bit outward rational logarithm intervals',
            'dimensions_checked':[r['m'] for r in rows],
            'rows':rows,
            'scope':'Full Walsh checks are finite self-checks. The asymptotic all-m obstruction is proved algebraically in the note; no independent audit.'}
    Path('shannon_potential_barrier_certificate.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','dimensions_checked':result['dimensions_checked'],
                      'last_row':rows[-1]},indent=2))


if __name__=='__main__':
    main()
