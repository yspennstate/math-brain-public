"""Exact matrix certificate retaining the extreme-pair projection bound."""
import contextlib,itertools,json
with open('sharpen_rank_one.out','a') as log, contextlib.redirect_stdout(log):
    import sharpen_rank_one as base
import sympy as s
v=base.U[0]+base.U[4]
pert=((s.Rational(14,3)*base.p*base.t**2+s.Rational(193,20)*base.t**3
       -s.Rational(99,2)*base.q*base.t)*base.R
      +(140*base.p*base.t-64*base.t**2)*base.C
      +35*v*v*((base.q-base.t**2/5)*base.R+base.t*base.C))

# Sign reversal of u permits the half cone U_1+U_5>=0.
# Its six rays in the original ordered-cone coordinates are listed explicitly.
y=s.symbols('y0:6')
sub={base.z[0]:y[0]+y[2]+y[3],
     base.z[1]:y[1]+y[4]+3*y[5],
     base.z[2]:3*y[2]+y[4],base.z[3]:y[3]+y[5]}
coeff={}
for name,mat in [('E',base.EE),('P',pert),('T',base.TT)]:
    for i in range(3):
        for j in range(i,3):
            poly=s.Poly(s.expand(mat[i,j]).subs(sub,simultaneous=True).expand(),*y)
            for mon,c in poly.terms():
                assert sum(mon)==8
                if mon not in coeff:coeff[mon]={'E':s.zeros(3),'P':s.zeros(3),'T':s.zeros(3)}
                coeff[mon][name][i,j]=coeff[mon][name][j,i]=c
    print('PROVED: expanded',name,'on half cone; coefficient matrices',len(coeff),flush=True)

def bad_at(r,early=False):
    negatives=[]
    for mon,ct in coeff.items():
        mat=ct['E']+r*ct['P']-s.Rational(1581,32)*r*r*ct['T']
        for k in range(1,4):
            for inds in itertools.combinations(range(3),k):
                if mat.extract(inds,inds).det()<0:
                    negatives.append((mon,inds))
                    if early:return negatives
    return negatives

for rr in [s.Rational(1,20),s.Rational(7,100),s.Rational(1,10),s.Rational(3,20),s.Rational(1,5)]:
    bad=bad_at(rr)
    print('PROVED: certificate succeeds at' if not bad else 'NUMERICAL: no certificate at',rr,'negative minors',len(bad),flush=True)
lo,hi=0,3001
while lo+1<hi:
    mid=(lo+hi)//2
    if bad_at(s.Rational(mid,10000),early=True):hi=mid
    else:lo=mid
rr=s.Rational(lo,10000)
assert not bad_at(rr)
records=[]
for mon,ct in sorted(coeff.items()):
    mat=ct['E']+rr*ct['P']-s.Rational(1581,32)*rr*rr*ct['T']
    den=s.ilcm(*[x.q for x in mat])
    records.append(dict(monomial=mon,denominator=int(den),matrix=[[int(den*x) for x in mat.row(i)] for i in range(3)]))
with open('enhanced_ratio_matrices.json','w') as out:json.dump(dict(r=str(rr),records=records),out,indent=2)
print('PROVED: exported exact endpoint certificate r =',rr,flush=True)
