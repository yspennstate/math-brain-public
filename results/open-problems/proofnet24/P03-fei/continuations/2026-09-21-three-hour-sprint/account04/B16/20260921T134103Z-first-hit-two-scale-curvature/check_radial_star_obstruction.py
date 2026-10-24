#!/usr/bin/env python3
from fractions import Fraction
import json

def split_energy(coeff):
    micro=Fraction(0); radial=Fraction(0)
    for A,cA in coeff.items():
        r=A.bit_count()
        for B,cB in coeff.items():
            s=B.bit_count(); h=(A&B).bit_count()
            if not h: continue
            u=(A|B).bit_count()
            micro += cA*cB*(Fraction(h,u)-Fraction(h,r+s-1))
            radial += cA*cB*(Fraction(h,r+s-1)-Fraction(h,r*s))
    return micro,radial

def star(d):
    return {
        (1<<0)|(1<<i)|(1<<j): Fraction(1)
        for i in range(1,d+1) for j in range(i+1,d+1)
    }

def closed(d):
    micro=Fraction(d*d*(d-1),10)
    radial=Fraction(d*(d-1)*(d-1)*(d+4),45)
    ratio=Fraction(2*(d-1)*(d+4),9*d)
    return micro,radial,ratio

def main():
    direct=0
    for d in range(2,13):
        micro,radial=split_energy(star(d))
        cm,cr,q=closed(d)
        assert micro==cm and radial==cr and radial/micro==q
        direct+=1
    rows={}
    for d in (2,8,64):
        micro,radial,q=closed(d)
        rows[str(d)]={"internal":str(micro),"radial":str(radial),"ratio":str(q),"ratio_float":float(q)}
    print(json.dumps({
        "status":"PASS",
        "direct_pair_kernel_star_cases":direct,
        "internal_formula":"d^2(d-1)/10",
        "radial_formula":"d(d-1)^2(d+4)/45",
        "ratio_formula":"2(d-1)(d+4)/(9d)",
        "ratio_asymptotic":"(2/9)d",
        "examples":rows
    },indent=2,sort_keys=True))

if __name__=="__main__":
    main()
