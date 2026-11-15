"""Exact arithmetic sanity checks for C32; not a proof of the frog coupling."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from datetime import datetime, timezone
import json

def check():
    cases = 0
    for d in (2, 3, 5):
        for p in (Q(1,10), Q(1,4), Q(1,3), Q(49,100)):
            beta=p/(1-p); q=(1-p)/d
            denominator=1-(d-1)*q*beta
            r=q/denominator
            assert denominator > 0 and 0 < r < 1
            assert denominator-q == p+(d-1)*q*(1-beta)
            assert r == q+(d-1)*q*beta*r
            previous=Q(0)
            for length in range(2,16):
                beta_l=(beta-beta**length)/(1-beta**length)
                r_l=q/(1-(d-1)*q*beta_l)
                assert previous < r_l < r
                previous=r_l
                cases+=1
            for k in range(0,9):
                masses=[Q(comb(k+1,i))*r**i*(1-r)**(k+1-i) for i in range(k+2)]
                assert sum(masses)==1
                assert masses[0] == (1-r)**(k+1)
                assert sum(Q(i)*v for i,v in enumerate(masses)) == (k+1)*r
                cases+=1
    a=Q(7,10)
    ratio4=2*a*a; ratio8=2*a**4
    assert ratio4==Q(49,50) and ratio8==Q(2401,5000)
    tail8=3*a*ratio8**6/(1-ratio8)
    assert tail8 < Q(1,20)
    for alpha in (4,8):
        for j in range(4096):
            n=j+2; k=1
            while 4**k < n**alpha: k+=1
            m=n.bit_length()-1
            assert k >= (alpha//2)*m
            cases+=1
    return {'at':datetime.now(timezone.utc).isoformat(),'result':'PASS',
            'checks':cases,'r_at_T3_quarter':'3/10',
            'alpha4_dyadic_ratio':str(ratio4),'alpha8_dyadic_ratio':str(ratio8),
            'alpha8_tail_from_j62':str(tail8),'tail_less_than':'1/20',
            'scope':'Exact algebra and boundary controls only; no independent audit, no activation or recurrence certificate.'}

if __name__=='__main__':
    result=check()
    Path('C32_EXACT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
