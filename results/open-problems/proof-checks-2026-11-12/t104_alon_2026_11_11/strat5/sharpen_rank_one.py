"""PROVED if assertions pass: strengthen the supplied ordered-cone certificate.

Construct E R0 and t^3 R0 separately, then test rational lower bounds E>=c.
Only exact rational principal minors determine the reported certificate.
"""
import itertools,json
import sympy as s
z=s.symbols('z0:4')
U=s.Matrix([sum(((5-j) if i<j else -j)*z[j-1] for j in range(1,5)) for i in range(5)])
t=(U.T*U)[0]
q=sum(x**4 for x in U)
d=sum(x**3 for x in U)
p=-U[0]*U[4]
delta=U[0]-U[4]
K=s.zeros(5,3)
for j in range(3):
    K[0,j]=U[4]-U[j+1]
    K[j+1,j]=delta
    K[4,j]=U[j+1]-U[0]
assert s.expand(s.ones(1,5)*K)==s.zeros(1,3)
assert s.expand(U.T*K)==s.zeros(1,3)
R=K.T*K
C=K.T*s.diag(*[x*x for x in U])*K
F=K.T*s.diag(*list(U))*K
ev=K.T*s.Matrix([x*x for x in U])
alpha=140*p*q-28*p*t*t-47*q*t+13*t**3+24*d*d
EE=alpha*R+(140*p*t-41*t*t)*C+6*t*ev*ev.T+18*t*d*F
TT=t**3*R
coeff={}
for name,mat in [('E',EE),('T',TT)]:
    for i in range(3):
        for j in range(i,3):
            for mon,c in s.Poly(s.expand(mat[i,j]),*z).terms():
                assert sum(mon)==8
                if mon not in coeff: coeff[mon]={'E':s.zeros(3),'T':s.zeros(3)}
                coeff[mon][name][i,j]=coeff[mon][name][j,i]=c
def check(c):
    negatives=[]
    for mon,ct in coeff.items():
        mat=ct['E']-c*ct['T']
        for k in range(1,4):
            for inds in itertools.combinations(range(3),k):
                if mat.extract(inds,inds).det()<0: negatives.append((mon,inds))
    return negatives
for c in [s.Rational(1,2),s.Rational(3,5),s.Rational(2,3),s.Rational(7,10),s.Rational(3,4),s.Rational(4,5)]:
    bad=check(c)
    print(('PROVED: E >= '+str(c)) if not bad else ('NUMERICAL: certificate not obtained at c='+str(c)),
          'coefficient matrices',len(coeff),'negative principal minors',len(bad),flush=True)
valid=[s.Rational(k,1000) for k in range(500,801)]
lo,hi=0,len(valid)
while lo+1<hi:
    mid=(lo+hi)//2
    if check(valid[mid]): hi=mid
    else: lo=mid
c=valid[lo]
assert not check(c)
records=[]
for mon,ct in sorted(coeff.items()):
    mat=ct['E']-c*ct['T']
    assert all((1000*x).is_Integer for x in mat)
    records.append(dict(monomial=mon,matrix_times_1000=[[int(1000*x) for x in mat.row(i)] for i in range(3)]))
with open('sharpen_rank_one_matrices.json','w') as out:
    json.dump(dict(c=str(c),records=records),out,indent=2)
print('PROVED: exported exact certificate E >=',c,flush=True)
