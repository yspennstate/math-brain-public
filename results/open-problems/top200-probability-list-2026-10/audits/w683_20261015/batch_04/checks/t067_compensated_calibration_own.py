"""Exact orbit density-correction tensor and calibrated cubic operator."""
import sympy as S
from itertools import permutations
from pathlib import Path
import json
x,y=S.symbols('x y'); a=S.Matrix([x,y,-x-y]); P=S.eye(3)-S.ones(3)/3
A=(a.T*a)[0]; b=-P*a.applyfunc(lambda z:z*z)/2
assert S.expand((b.T*b)[0]-A*A/24)==0
tensor=S.zeros(3)
for order in permutations(range(3)):
    z=S.Matrix([a[i] for i in order]); q=-P*z.applyfunc(lambda k:k*k)/2
    tensor+=z[0]*(z*q.T+q*z.T)/6
normalized=tensor.applyfunc(lambda z:S.cancel(z/A**2))
assert not any(z.free_symbols for z in normalized)
assert normalized.eigenvals()=={S.Rational(-1,12):1,S.Rational(1,12):1,S.Integer(0):1}
p=[x,y,1-x-y]
def D(i,f):return S.expand(x*(int(i==0)-p[i])*S.diff(f,x)+y*(int(i==1)-p[i])*S.diff(f,y))
def ell(i,f):
    j,k=[r for r in range(3) if r!=i]
    return (sum(D(r,D(r,D(r,f))) for r in range(3))-D(i,f)-D(j,D(j,f))+2*D(j,D(k,f))-D(k,D(k,f)))/4
weighted=S.expand(sum(p[i]*ell(i,p[i]) for i in range(3)))
e2=p[0]*p[1]+p[0]*p[2]+p[1]*p[2];e3=S.prod(p)
assert S.expand(weighted+e2*(e2-9*e3))==0
out={'complete':True,'density_correction_tensor_divided_by_U':[[str(normalized[i,j]) for j in range(3)] for i in range(3)],'eigenvalues':['-1/12','0','1/12'],'nuclear_norm_divided_by_U':'1/6','bb_norm_divided_by_U':'1/24','calibrated_cubic_identity':'sum_i p_i ell_i(F_i)=-e2(e2-9e3)=S_A/9'}
Path('checks/t067_compensated_calibration_own.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))
