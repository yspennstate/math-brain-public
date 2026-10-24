import json,pathlib
import sympy as s
P=pathlib.Path(__file__).resolve().parent
t,e=s.symbols('t e',real=True)
d3=t**3-3*t*e**2+2*e**3;d2=t**2-2*e**2
assert s.expand(d3**2-d2**3-e**3*(4*t**3-3*t**2*e-12*t*e**2+12*e**3))==0
H=s.diag(s.Matrix([[0,1,1],[1,0,1],[1,1,0]]),s.Matrix([[0,s.sqrt(2)],[s.sqrt(2),0]]))
assert all(sum(H[i,j]**2 for j in range(5))==2 for i in range(5))
assert s.factor((t*s.eye(3)+e*H[:3,:3]).det()-d3)==0
assert s.factor((t*s.eye(2)+e*H[3:,3:]).det()-d2)==0
v={t:s.Rational(1,2),e:s.Rational(1,100)}
margin=s.factor((d3**2-d2**3).subs(v));assert margin>0
report={'target':'false extension to constant-row-energy kernels; NOT C0036','t':'1/2','epsilon':'1/100','row_energies':[2]*5,'d3':str(d3.subs(v)),'d2':str(d2.subs(v)),'strict_power_comparison_margin':str(margin),'event':'the two-site component is fully present'}
P.joinpath('boundary_extension_results.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2));print('EXACT_ROW_ENERGY_EXTENSION_COUNTEREXAMPLE_PASS')
