"""Exact rational rank-two factors and interval curvature certificates.

The rounded factors define new exact rank-two directions. Directions are not
obtained by rounding the entries of a rank-two matrix, which could raise rank.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,resource
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
from interval_audit import bounds,pos
iv=mp.iv;iv.dps=100
DEN=10**10

def rational(z):return sp.Rational(round(float(z.real)*DEN),DEN)+sp.I*sp.Rational(round(float(z.imag)*DEN),DEN)
def enc(m):return [[[str(sp.re(z)),str(sp.im(z))] for z in row] for row in m.tolist()]
def num(z):
    z=sp.cancel(z);assert z.is_Rational,z
    return iv.mpf(int(z.p))/int(z.q)

def certify(path):
    zz=np.load(path);n=len(zz['Q']);qq=zz['Q'];q=sp.zeros(n)
    for i in range(n):
        q[i,i]=sp.re(rational(qq[i,i]))
        for j in range(i):q[i,j]=rational(qq[i,j]);q[j,i]=sp.conjugate(q[i,j])
    u=sp.Matrix([[rational(z) for z in row] for row in zz['factor']])
    w=[sp.re(rational(complex(z))) for z in zz['weights']]
    aa=(u*sp.diag(*w)*u.conjugate().T).applyfunc(sp.expand)
    assert aa.rank()==2
    for m in (q,sp.eye(n)-q):assert all(sp.cancel(m[:k,:k].det())>0 for k in range(1,n+1))
    norm2=sp.cancel(sp.trace(aa*aa));total=iv.mpf(0);mass=0;dsum=0;ddsum=0
    minp=sp.Rational(1);independent=True
    tt=sp.symbols('t')
    for s in range(1<<n):
        bb=q-sp.diag(*[0 if s>>i&1 else 1 for i in range(n)]);sgn=(-1)**(n-s.bit_count())
        pp=sp.cancel(sgn*bb.det());assert pp>0;minp=min(minp,pp)
        cc=bb.inv()*aa;dp=sp.cancel(pp*sp.trace(cc));ddp=sp.cancel(pp*(sp.trace(cc)**2-sp.trace(cc*cc)))
        if n==3:
            # Independent polynomial determinant coefficients, without inverses.
            pol=sp.Poly(sp.expand(sgn*(bb+tt*aa).det()),tt)
            independent &= sp.cancel(pol.nth(0)-pp)==0 and sp.cancel(pol.nth(1)-dp)==0 and sp.cancel(2*pol.nth(2)-ddp)==0
        mass+=pp;dsum+=dp;ddsum+=ddp
        total-=num(dp)**2/num(pp)+num(ddp)*iv.log(num(pp))
    assert independent and sp.cancel(mass-1)==0 and sp.cancel(dsum)==0 and sp.cancel(ddsum)==0
    total/=num(norm2);assert pos(-total)
    inp=dict(Q=enc(q),factor=enc(u),weights=list(map(str,w)),frobenius_norm_squared=str(norm2))
    name=Path(path).stem
    Path('data/'+name+'_rational.json').write_text(json.dumps(inp,indent=2)+'\n')
    return dict(witness=name,n=n,rank=2,signature='positive' if all(z>0 for z in w) else 'indefinite',curvature_normalized=bounds(total),min_atom=str(minp),independent_polynomial_check=(n==3))

def main():
    start=time.monotonic();rows=[]
    paths=[f'data/psd_optimized_{i}.npz' for i in range(8)]+[f'data/ranktwo_n{n}_sign{sign}.npz' for n in (3,4) for sign in (1,-1)]
    for path in paths:
        row=certify(path);rows.append(row);print(row['witness'],row['curvature_normalized'],flush=True)
    out=dict(precision_decimal=100,rounding_denominator=DEN,rows=rows,seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
    Path('data/ranktwo_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
