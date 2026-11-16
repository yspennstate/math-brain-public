"""PROVED: ordered-cone matrix certificate for an interval of gap ratios.

Imports the small exact construction, then retains dependence on u and w
instead of using a uniform perturbation norm bound.
"""
import contextlib
with open('sharpen_rank_one.out','a') as log, contextlib.redirect_stdout(log):
    import sharpen_rank_one as base
import itertools,json
import sympy as s
z=base.z
pert=((s.Rational(7,6)*base.p*base.t**2+s.Rational(11851,1200)*base.t**3
       -s.Rational(497,10)*base.q*base.t)*base.R
      +(140*base.p*base.t-64*base.t**2)*base.C)
pc={mon:s.zeros(3) for mon in base.coeff}
for i in range(3):
    for j in range(i,3):
        for mon,c in s.Poly(s.expand(pert[i,j]),*z).terms():
            assert mon in pc
            pc[mon][i,j]=pc[mon][j,i]=c
def bad_at(r):
    negatives=[]
    for mon,ct in base.coeff.items():
        mat=ct['E']+r*pc[mon]-s.Rational(249,5)*r*r*ct['T']
        for k in range(1,4):
            for inds in itertools.combinations(range(3),k):
                if mat.extract(inds,inds).det()<0: negatives.append((mon,inds))
    return negatives
for r in [s.Rational(1,70),s.Rational(1,50),s.Rational(1,30),s.Rational(1,20),s.Rational(1,15),s.Rational(1,10)]:
    bad=bad_at(r)
    print('PROVED: matrix certificate succeeds at' if not bad else 'NUMERICAL: matrix certificate fails at',r,'negative minors',len(bad),flush=True)
lo,hi=0,1501
while lo+1<hi:
    mid=(lo+hi)//2
    if bad_at(s.Rational(mid,10000)): hi=mid
    else: lo=mid
r=s.Rational(lo,10000)
assert not bad_at(r)
records=[]
for mon,ct in sorted(base.coeff.items()):
    mat=ct['E']+r*pc[mon]-s.Rational(249,5)*r*r*ct['T']
    den=s.ilcm(*[x.q for x in mat])
    records.append(dict(monomial=mon,denominator=int(den),
                        matrix=[[int(den*x) for x in mat.row(i)] for i in range(3)]))
with open('ratio_matrices.json','w') as out:
    json.dump(dict(r=str(r),records=records),out,indent=2)
print('PROVED: exported exact endpoint certificate r =',r,flush=True)
