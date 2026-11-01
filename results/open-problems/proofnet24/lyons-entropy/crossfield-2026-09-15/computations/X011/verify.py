from pathlib import Path
from itertools import combinations
import json
import sympy as s

out=Path(__file__).resolve().parent
I=s.I
R=s.Matrix([[1,s.Rational(1,3),I/4,0],[s.Rational(1,3),1,s.Rational(1,5),I/6],[-I/4,s.Rational(1,5),1,s.Rational(1,7)],[0,-I/6,s.Rational(1,7),1]])
E=s.diag(s.Rational(1,5),2,5,s.Rational(1,3))
L=E*R*E
K=L*(s.eye(4)+L).inv()
A=s.Matrix([[0,-I,0,0],[I,0,0,0],[0,0,1,0],[0,0,0,1]])
assert A*A==s.eye(4)
Pplus=(s.eye(4)+A)/2
Pminus=(s.eye(4)-A)/2
assert s.trace(Pplus)==3 and s.trace(Pminus)==1
J_A=0
J_I=0
crossmean=0
Vmean=0
hess=0
rem1=0
rem2=0
p_sum=0
margin_acc=[0]*4
atoms=[]
t=s.symbols('t')
delta=s.factor(1/R.det()-1)
for mask in range(16):
    occ=[i for i in range(4) if (mask>>i)&1]
    holes=[i for i in range(4) if i not in occ]
    M=K-s.diag(*[int(i in holes) for i in range(4)])
    B=M.inv()
    p=s.factor((-1)**len(holes)*M.det())
    score=s.factor(s.trace(A*B))
    q=s.factor(s.trace(A*B*A*B))
    qi=s.factor(s.trace(B*B))
    scoreI=s.factor(s.trace(B))
    C=s.factor(s.trace(Pplus*B*Pminus*B))
    V=s.factor(qi-score**2/4)
    assert p>0 and C>=0 and V>=0
    assert s.simplify(qi-q-4*C)==0
    f=-s.log(R.extract(occ,occ).det()) if occ else s.Integer(0)
    assert 0<=float(f.evalf())<=float(delta)
    J_A += p*score**2
    J_I += p*scoreI**2
    crossmean += p*C
    Vmean += p*V
    acc=s.factor(p*(score**2-q))
    hess += p*score**2+acc*s.log(p)
    rem1 += p*f*V
    rem2 += p*(delta-f)*(3*score**2/4+4*C)
    p_sum+=p
    for i in occ: margin_acc[i]+=acc
    # Only one exact determinant polynomial is needed for the nonreal-root test.
    if mask==1:
        poly=s.Poly(s.factor((-1)**len(holes)*(M+t*A).det()),t)
        roots=poly.nroots(maxsteps=200)
        poly_coeff=[str(x) for x in poly.all_coeffs()]
        real_count=poly.count_roots(-s.oo,s.oo)
    atoms.append({'mask':mask,'probability':str(p),'score':str(score),'q':str(q),'cross_energy':str(C),'trace_free_energy':str(V)})
J_A=s.factor(J_A)
J_I=s.factor(J_I)
crossmean=s.factor(crossmean)
assert s.simplify(p_sum-1)==0
assert all(s.simplify(x)==0 for x in margin_acc)
assert s.simplify(4*crossmean-(J_I-J_A))==0
bound=s.factor((1+delta/4)*J_A-delta*J_I)
assert bound>0
assert J_A/J_I>s.Rational(49,100)
assert delta<s.Rational(9,25)
integer_poly=s.Poly(228789991*poly.as_expr(),t)
discriminant=s.factor(integer_poly.discriminant())
assert discriminant<0
residue=(hess-bound-rem1-rem2).evalf(60)
assert abs(residue)<s.Float('1e-50')
assert real_count<4
summary={'status':'PASS','dimension':4,'inertia_A':[3,1],'det_R':str(R.det()),'delta':str(delta),'J_A':str(J_A),'J_abs':str(J_I),'J_ratio':str(s.factor(J_A/J_I)),'bound':str(bound),'minus_entropy_hessian':str(hess.evalf(40)),'bound_decimal':str(bound.evalf(25)),'remainder_identity_residual':str(residue),'nonreal_atom_mask':1,'polynomial_coefficients':poly_coeff,'real_root_count':int(real_count),'polynomial_roots':[str(x) for x in roots],'integer_polynomial_discriminant':str(discriminant),'simple_Fisher_lower_coefficient':'1741/4900'}
(out/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
(out/'atoms.json').write_text(json.dumps(atoms,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['J_A','J_abs','J_ratio','bound','polynomial_coefficients']},indent=2))
print('J_A/J_abs =',float(J_A/J_I))
