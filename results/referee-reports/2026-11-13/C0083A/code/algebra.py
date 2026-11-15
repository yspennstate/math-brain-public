"""Independent symbolic checks for normalization and one-line cycle counts."""
import json
from pathlib import Path
import sympy as s

d, z, x, b = s.symbols('d z x b', positive=True)
A = (2*d*d-1)/(2*(d-1)**2)
a2 = s.factor(1/d+A/d**2)
F = x**3*(2-x)/(1-x)**2
C1 = s.factor(d*F.subs(x,1/d)/2)
C2 = s.factor((d*(b*s.diff(F,x)-x*x*s.diff(F,x,2)/2)/2).subs(x,1/d))
series = s.series(1/(d*(1/z-1))+A/(d*(1/z-1))**2,z,0,3)
assert s.simplify(series.removeO().coeff(z,2)-a2) == 0
G = x**3/(1-x)
assert s.simplify(F-(x*s.diff(G,x)-G)) == 0
result = {'A_degree':str(A),'a2_n':str(a2),'F':str(F),
          'weighted_cycles_n^-1':str(C1),'weighted_cycles_n^-2':str(C2),
          'weighted_cycles_n^-2_at_b=a2':str(s.factor(C2.subs(b,a2))),
          'small_d':{str(i):str(a2.subs(d,i)) for i in range(3,10)}}
root=Path(__file__).resolve().parents[1]
(root/'data'/'algebra.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
