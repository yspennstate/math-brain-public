"""Interval boundary probes with exact rational inputs and closed formulas."""
import json,time,resource
from pathlib import Path
from fractions import Fraction as F
from interval_core import iv,rat,bounds,pos,full_certificate

def main():
    start=time.monotonic();iv.dps=220
    out=dict(precision_decimal=iv.dps,structured=[],cyclic=[])
    # Q=(1-delta) direct-sum a nearly projecting two-point block, connected
    # by equal positive edges e. Everything here is an exact rational.
    for k in (1,2,3,4,6,8,10,12):
        delta=F(1,10**k);e=delta**2
        xx=[1-delta,F(1,2),F(1,2),e,0,e,0,-F(1,2)+e,0]
        assert (1-delta)*e>2*e*e and delta*(1-e)>2*e*e
        row=dict(k=k,delta=str(delta),e=str(e),coordinates=list(map(str,xx)),
                 strictness_minors=[str((1-delta)*e-2*e*e),str(delta*(1-e)-2*e*e)])
        row.update(full_certificate([rat(z) for z in xx]));out['structured'].append(row)
        print('structured',k,row['margin'],flush=True)
    # k is an integer ratio of atom probabilities, not the previous exponent.
    # Strictness is exact: r^2=(k-1)/(4(3k+1)) lies strictly between 0 and 1/12.
    for exponent in (1,2,4,8,16,32,100,1000):
        kk=iv.mpf(10)**exponent;L=iv.log(kk)
        coeff=(6*kk**2+6*kk-4)/(kk*(3*kk+1))
        determinant=36*(-L**2+coeff*L+3*(kk-1)**2/kk)
        f22=9*(kk-1)**2*(kk+3)/(kk*(3*kk+1))
        schur=determinant/(f22+6*L);margin=schur/(9*L+schur)
        assert pos(determinant) and pos(margin)
        out['cyclic'].append(dict(k='10^'+str(exponent),margin=bounds(margin,50),
                                  theta=bounds(1-margin,50),schur=bounds(schur,50)))
        print('cyclic',exponent,bounds(margin,25),flush=True)
    out['seconds']=time.monotonic()-start
    out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
    Path('data/boundary.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
