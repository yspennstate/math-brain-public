"""Exact coefficient tests for additional frame-moment bounds."""
import itertools,json
import sympy as s
z=s.symbols('z0:4')
U=s.Matrix([sum(((5-j) if i<j else -j)*z[j-1] for j in range(1,5)) for i in range(5)])
t=(U.T*U)[0]
q=sum(x**4 for x in U)
delta=U[0]-U[4]
K=s.zeros(5,3)
for j in range(3):
    K[0,j]=U[4]-U[j+1]
    K[j+1,j]=delta
    K[4,j]=U[j+1]-U[0]
R=K.T*K
C=K.T*s.diag(*[x*x for x in U])*K
for c in [s.Rational(5,24),s.Rational(7,30)]:
    co=s.Poly(s.expand(q-c*t*t),*z).coeffs()
    print('PROVED:' if min(co)>=0 else 'NUMERICAL: no coefficient certificate:', 'A>=',c,'negative coefficients',sum(int(bool(x<0)) for x in co),flush=True)
coeff={}
for i in range(3):
    for j in range(i,3):
        for mon,c in s.Poly(s.expand(q*R[i,j]+t*C[i,j]),*z).terms():
            if mon not in coeff:coeff[mon]=[s.zeros(3),s.zeros(3)]
            coeff[mon][0][i,j]=coeff[mon][0][j,i]=c
        for mon,c in s.Poly(s.expand(t*t*R[i,j]),*z).terms():
            if mon not in coeff:coeff[mon]=[s.zeros(3),s.zeros(3)]
            coeff[mon][1][i,j]=coeff[mon][1][j,i]=c
for c in [s.Rational(1,4),s.Rational(7,25),s.Rational(3,10)]:
    neg=0
    for m,n in coeff.values():
        mat=m-c*n
        for k in range(1,4):
            for inds in itertools.combinations(range(3),k):
                neg+=int(bool(mat.extract(inds,inds).det()<0))
    print('PROVED:' if not neg else 'NUMERICAL: no coefficient certificate:', 'A+C>=',c,'negative minors',neg,flush=True)
    if c==s.Rational(1,4):
        assert not neg
        records=[]
        for mon,(m,n) in sorted(coeff.items()):
            mat=m-c*n
            den=s.ilcm(*[x.q for x in mat])
            records.append(dict(monomial=mon,denominator=int(den),matrix=[[int(den*x) for x in mat.row(i)] for i in range(3)]))
        with open('moment_lower_matrices.json','w') as out:json.dump(records,out,indent=2)
