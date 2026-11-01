"""Rigorous rational enclosures of logarithms, entropy and cancellation.

Only integers and fractions determine signs/endpoints. ln uses the atanh
series with an explicit geometric remainder after dyadic range reduction.
Decimal output is outward rounded solely for readability.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
import numpy as np
from cancellation_composition import fwht
from reconstruct_external_seed import core_and_hosts, make_table, EXPECTED_SHA

TERMS = 80


def log_unit_interval(x: F, terms: int = TERMS) -> tuple[F,F]:
    """ln x for 1 <= x <= 2, using exact nonnegative rational terms."""
    if not (1 <= x <= 2): raise ValueError('Range reduction failure')
    if x == 1: return F(0),F(0)
    z=(x-1)/(x+1)
    z2=z*z
    power=z
    s=F(0)
    for k in range(terms):
        s += power/(2*k+1)
        power *= z2
    lower=2*s
    # The omitted series starts at z^(2*terms+1)/(2*terms+1).
    rem=2*power/((2*terms+1)*(1-z2))
    return lower,lower+rem


@lru_cache(maxsize=None)
def log2_interval(x: F, terms: int = TERMS) -> tuple[F,F]:
    if x <= 0: raise ValueError('Log input must be positive')
    if x < 1:
        lo,hi=log2_interval(1/x,terms)
        return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x < F(2)**e: e-=1
    m=x/(F(2)**e)
    a,b=log_unit_interval(m,terms)
    c,d=log_unit_interval(F(2),terms)
    return F(e)+a/d,F(e)+b/c


def decimal_out(q: F, digits: int = 45, upper: bool = False) -> str:
    scale=10**digits
    a=q.numerator*scale
    b=q.denominator
    v= -((-a)//b) if upper else a//b
    sign='-' if v<0 else ''
    v=abs(v)
    return f'{sign}{v//scale}.{v%scale:0{digits}d}'


def interval_json(lo: F, hi: F) -> dict:
    if lo>hi: raise AssertionError('Reversed interval')
    return {'lower':decimal_out(lo), 'upper':decimal_out(hi,upper=True),
            'width_upper':decimal_out(hi-lo,70,True)}


def entropy_from_squares(sq: np.ndarray, norm: int) -> tuple[F,F]:
    lo=F(0); hi=F(0)
    for s,m in Counter(map(int,sq)).items():
        if s==0: continue
        l,u=log2_interval(F(norm,s))
        w=F(m*s,norm)
        lo+=w*l;hi+=w*u
    return lo,hi


def cancellation_from_squares(sq: np.ndarray, n: int) -> tuple[F,F]:
    ups=sq.copy()
    for j in range(n):
        h=1<<j
        b=ups.reshape(-1,2*h)
        b[:,:h]+=b[:,h:]
    groups=Counter((int(s),int(u)) for s,u in zip(sq,ups) if s)
    lo=F(0);hi=F(0);norm=1<<(2*n)
    for (s,u),m in groups.items():
        l,h=log2_interval(F(u,s))
        w=F(s*m,norm)
        lo+=w*l;hi+=w*h
    return lo,hi


def certify() -> dict:
    base,hosts=core_and_hosts();table=make_table(base,hosts)
    import hashlib
    assert hashlib.sha256(','.join(map(str,table)).encode()).hexdigest()==EXPECTED_SHA
    W=fwht(table); sq=W*W; n=18;norm=1<<(2*n)
    assert W[0]==0 and sum(map(int,sq))==norm
    i=F(sum(k.bit_count()*int(s) for k,s in enumerate(sq)),norm)
    assert i==F(261,128)
    hlo,hhi=entropy_from_squares(sq,norm)
    blo,bhi=cancellation_from_squares(sq,n)
    r=5;factor=(1-i**(-r))/(i-1)
    c=F('2.2273918583')  # safely above (6.4547837166/2 - 1)
    assert blo*factor>c
    assert hlo/(i-1)>F('6.521845710923046575')
    return {
      'source':'Numaro external n18 seed; reproduced, not discovered in this run',
      'truth_table_sha256':EXPECTED_SHA,
      'arithmetic':'integer Walsh plus exact Fraction log-series enclosures',
      'log_series_terms':TERMS,
      'I_exact':str(i),
      'H_seed':interval_json(hlo,hhi),
      'Bcan_seed':interval_json(blo,bhi),
      'amplified_H_limit':interval_json(hlo/(i-1),hhi/(i-1)),
      'amplified_Bcan_limit':interval_json(blo/(i-1),bhi/(i-1)),
      'finite_composition_counterexample':{
          'definition':'F_0 is one input bit; F_(r+1)=g_18(F_r copies on 18 disjoint blocks)',
          'r':r,'number_variables':18**r,'I_exact':str(i**r),
          'Bcan_over_I':interval_json(blo*factor,bhi*factor),
          'H_over_I':interval_json(hlo*factor,hhi*factor),
          'refuted_upper_bound':str(c),
          'strict_margin_lower':decimal_out(blo*factor-c),
          'full_FEI_counterexample':False,
          'meaning':'Refutes a too-strong cancellation-entropy lemma, not existence of a finite universal FEI constant'
      },
      'proposed_full_FEI_route':'A weaker universal Bcan <= c I is still open; c must exceed the certified amplified Bcan lower bound.',
      'novelty_claim':False,
    }


if __name__=='__main__':
    # Analytic anchors whose exact values must be contained.
    for q,known in [(F(1),F(0)),(F(2),F(1)),(F(4),F(2)),(F(1,8),F(-3))]:
        a,b=log2_interval(q); assert a<=known<=b
    report=certify()
    (Path(__file__).resolve().parent/'cancellation_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
