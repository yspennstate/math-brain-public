from pathlib import Path
import json
import sympy as s
I=s.I
K=s.Matrix([[s.Rational(2,5),s.Rational(1,10),I/20],[s.Rational(1,10),s.Rational(1,2),s.Rational(3,50)],[-I/20,s.Rational(3,50),s.Rational(3,5)]])
A=s.Matrix([[s.Rational(3,8),5*I/8,0],[-5*I/8,s.Rational(3,8),0],[0,0,s.Rational(1,2)]])
assert A.eigenvals()=={s.Rational(-1,4):1,s.Rational(1):1,s.Rational(1,2):1}
kappa=s.trace(A*A)
assert kappa==s.Rational(21,16)
L=K*(s.eye(3)-K).inv()
detR=s.factor(L.det()/s.prod(L[i,i] for i in range(3)))
delta=1/detR-1
JA=JI=Ez=0
remainder=entropy=0
sumP=0
for mask in range(8):
    occ=[i for i in range(3) if (mask>>i)&1]
    holes=[i for i in range(3) if i not in occ]
    M=K-s.diag(*[int(i in holes) for i in range(3)])
    B=M.inv()
    p=s.factor((-1)**len(holes)*M.det())
    assert p>0
    score=s.factor(s.trace(A*B))
    q=s.factor(s.trace(A*B*A*B))
    qi=s.factor(s.trace(B*B))
    Z=s.factor(qi-q)
    V=s.factor(qi-score**2/kappa)
    assert Z>=0 and V>=0
    f=-s.log(s.factor(L.extract(occ,occ).det()/s.prod(L[i,i] for i in occ))) if occ else s.Integer(0)
    assert 0<=float(f.evalf())<=float(delta)
    JA+=p*score**2
    JI+=p*s.trace(B)**2
    Ez+=p*Z
    entropy+=p*score**2+p*(score**2-q)*s.log(p)
    remainder+=p*(f*V+(delta-f)*((1-1/kappa)*score**2+Z))
    sumP+=p
JA,JI,Ez=map(s.factor,[JA,JI,Ez])
assert sumP==1
assert s.factor(Ez-(JI-JA))==0
residual=(entropy-(1+delta/kappa)*JA+delta*JI-remainder).evalf(60)
assert abs(residual)<s.Float('1e-50')
result={'status':'PASS','dimension':3,'direction_eigenvalues':['1','1/2','-1/4'],'kappa':str(kappa),'mean_contraction_defect':str(Ez),'FI_majorant_minus_FI_direction':str(s.factor(JI-JA)),'exact_remainder_residual':str(residual),'minus_entropy_hessian':str(entropy.evalf(30))}
Path(__file__).with_name('majorant_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
