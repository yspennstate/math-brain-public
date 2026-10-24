from pathlib import Path
import json
import sympy as s
I=s.I
R=s.Matrix([[1,s.Rational(1,3),I/4,0],[s.Rational(1,3),1,s.Rational(1,5),I/6],[-I/4,s.Rational(1,5),1,s.Rational(1,7)],[0,-I/6,s.Rational(1,7),1]])
E=s.diag(s.Rational(1,5),2,5,s.Rational(1,3))
L=E*R*E
K=L*(s.eye(4)+L).inv()
A=s.Matrix([[0,-I,0,0],[I,0,0,0],[0,0,1,0],[0,0,0,1]])
Sigma=s.Matrix(4,4,lambda i,j: K[i,i]*(1-K[i,i]) if i==j else -s.expand(K[i,j]*s.conjugate(K[i,j])))
a=s.Matrix([A[i,i] for i in range(4)])
lower=s.factor((a.T*Sigma.inv()*a)[0])
upper=s.factor(s.trace((K*(s.eye(4)-K)).inv()))
delta=s.factor(1/R.det()-1)
bound=s.factor((1+delta/4)*lower-delta*upper)
assert bound>0
ratio=s.factor(lower/upper)
assert ratio>s.Rational(12,25)
result={'status':'PASS','FI_A_lower':str(lower),'FI_abs_upper':str(upper),'FI_ratio_lower':str(ratio),'lower_bound':str(bound),'FI_A_lower_decimal':str(lower.evalf(30)),'FI_abs_upper_decimal':str(upper.evalf(30)),'lower_bound_decimal':str(bound.evalf(30))}
Path(__file__).with_name('matrix_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
