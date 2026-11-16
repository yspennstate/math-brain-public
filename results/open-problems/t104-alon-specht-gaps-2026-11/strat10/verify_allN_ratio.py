"""PROVED: exact coefficient and PSD replay of the all-N ratio strip."""
import json
from fractions import Fraction as F
from sympy.polys.domains import QQ
from verify_small_ratio import psd
from allN_ratio_polynomial import construct

def main():
    data=json.load(open('allN_ratio_certificate.json'));rho=F(data['rho'])
    assert 0<rho<F(3,7) and len(data['padding'])==3
    count=0
    for index,group in enumerate(data['padding']):
        rr,polys=construct(rho,index)
        assert len(group)==3
        if index==0:
            from small_ratio_polynomial import construct as original
            assert polys==original(rho)[1]
        for control,expect in zip(group,polys):
            assert not control['failed'];actual=rr.zero;seen=set();mons=control['monomials']
            assert len(mons)==6 and len({tuple(m)for m in mons})==6 and all(sum(m)==2 for m in mons)
            for rec in control['records']:
                mon=tuple(rec['monomial']);assert sum(mon)==10 and mon not in seen;seen.add(mon)
                rows=rec['matrix'];assert len(rows)==6 and all(len(row)==6 for row in rows)
                psd(rows);sc=F(rec['scale'])/rec['denominator'];assert rec['denominator']>0 and sc>0
                for i in range(6):
                    for j in range(6):
                        full=mon+tuple(a+b for a,b in zip(mons[i],mons[j]));c=sc*rows[i][j]
                        actual+=rr.from_dict({full:QQ(c.numerator,c.denominator)})
                count+=1
            assert actual==expect
    print('PROVED: all',count,'rational Gram matrices and coefficients checked; T_N>=0 at every admissible scale for N>=6 and 0<r<=',rho)
if __name__=='__main__':main()
