#!/usr/bin/env python3
"""Exact signed-power obstruction; rational endpoints are authoritative."""
from fractions import Fraction as F
from math import isqrt
from collections import Counter
import hashlib,json,pathlib
from verify import fwht,ln_interval,encl,test_enclosures

def sqrt_interval(q,bits=110):
    q=F(q);scale=1<<bits
    a=isqrt((q.numerator*scale*scale)//q.denominator)
    lo=F(a,scale);hi=F(a+1,scale)
    assert lo*lo<=q<=hi*hi
    return lo,hi

def scale(a,c):
    return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])

def add(*args):return sum((a[0] for a in args),F(0)),sum((a[1] for a in args),F(0))

def record(a):return {'rational_lower':str(a[0]),'rational_upper':str(a[1]),'outward_decimal_summary':encl(a)}

def main():
    test_enclosures();w=json.loads(pathlib.Path('witness.json').read_text());f=[-1 if x in w['negative_f'] else 1 for x in range(128)];W=fwht(f)
    assert dict(Counter(W))=={-6:48,-2:60,26:16,30:4}
    coarse=(52*F(36055,10000)+15*F(38729,10000)-36*F(17321,10000)-15)/128
    assert F(36055,10000)**2<13 and F(38729,10000)**2<15 and F(17321,10000)**2>3
    assert coarse>F(1314,1000)
    power=scale(add(scale(sqrt_interval(13),52),scale(sqrt_interval(15),15),scale(sqrt_interval(3),-36),(F(-15),F(-15))),F(1,128))
    direct=add(*(scale(sqrt_interval(F(abs(a),128)),F(a,128)) for a in W))
    assert max(power[0],direct[0])<=min(power[1],direct[1])
    assert power[0]>F(1314,1000) and power[1]<F(1315,1000)
    derivative=add(scale(ln_interval(F(2)),-6),scale(ln_interval(F(3)),F(-21,16)),scale(ln_interval(F(13)),F(13,4)),scale(ln_interval(F(5)),F(15,16)))
    assert derivative[0]>4
    tensor=[a*b for b in f for a in f];WT=fwht(tensor)
    assert WT==[a*b for b in W for a in W]
    out={'status':'PASS','full_FEI':'OPEN','coarse_exact_lower':str(coarse),'power_three_halves_at_origin':record(power),'derivative_at_one_natural_units':record(derivative),'actual_tensor_truth_table_inputs':len(tensor),'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256(pathlib.Path('verify.py').read_bytes()).hexdigest()}
    pathlib.Path('power_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
