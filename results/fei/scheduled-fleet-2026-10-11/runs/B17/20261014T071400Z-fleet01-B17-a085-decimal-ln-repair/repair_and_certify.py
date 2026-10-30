#!/usr/bin/env python3
"""Adversarial repair of the B17/A084 Decimal logarithm enclosure.

Decimal.ln() is correctly rounded with ROUND_HALF_EVEN regardless of the
context rounding mode.  The original logp therefore did not create directed
bounds.  Here a correctly-rounded guard-precision value is bracketed by its
two adjacent representable values, then rounded outward at certificate
precision.  All other interval operations remain those of the source-pinned
A084 checker.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN, localcontext
from pathlib import Path
import runpy

HERE=Path(__file__).resolve().parent
SOURCE=(HERE.parent/'20261014T064217Z-fleet01-B17-a084-equality-corners'/
        'certify_equality_corners.py')
ns=runpy.run_path(str(SOURCE))

PREC=ns['PREC']
DOWN=ns['DOWN']; UP=ns['UP']
GUARD=Context(prec=PREC+24,rounding=ROUND_HALF_EVEN)

def rigorous_logp(x):
    assert x>0
    with localcontext(GUARD):
        y=x.ln()  # correctly rounded to PREC+24 in ROUND_HALF_EVEN
        lo=y.next_minus()
        hi=y.next_plus()
    with localcontext(DOWN): lo=+lo
    with localcontext(UP): hi=+hi
    return lo,hi

def rigorous_logiv(x):
    return rigorous_logp(x[0])[0],rigorous_logp(x[1])[1]

# Functions produced by runpy retain ns as their global dictionary.
ns['logp']=rigorous_logp
ns['logiv']=rigorous_logiv

def audit_rounding_defect():
    x=D(2)
    with localcontext(DOWN): old_lo=+x.ln()
    with localcontext(UP): old_hi=+x.ln()
    assert old_lo==old_hi  # proves old method did not direct the transcendental
    lo,hi=rigorous_logp(x)
    assert lo < old_lo <= hi
    print('Decimal.ln rounding-mode adversary: DETECTED_AND_REPAIRED')
    print('old_floor_equals_old_ceiling=',old_lo==old_hi,sep='')
    print('guard_digits=',GUARD.prec,sep='')
    print('repaired_ln2_width=',hi-lo,sep='')

if __name__=='__main__':
    audit_rounding_defect()
    ns['certify']()
