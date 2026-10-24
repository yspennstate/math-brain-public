"""Symbolic reconstruction of the critical derivatives, on 0<x<pi/2."""
from pathlib import Path
import sympy as s
import json,time
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter()
x=s.symbols('x',real=True)
L=s.log(s.cos(x))-s.log(s.sin(x))
# Logs are valid on this proof domain, since sin(x), cos(x)>0.
psi=-2*s.sin(x)**2*s.log(s.sin(x))-2*s.cos(x)**2*s.log(s.cos(x))
forms=[2*s.sin(2*x)*L,
       4*s.cos(2*x)*L-4,
       -8*(s.sin(2*x)*L+s.cot(2*x)),
       16*(1+1/s.sin(2*x)**2-s.cos(2*x)*L)]
checks=[]
prev=psi
for k,expected in enumerate(forms,1):
    residual=s.trigsimp(s.expand_trig(s.diff(prev,x)-expected))
    if residual!=0:residual=s.trigsimp(residual,method='fu')
    if residual!=0:
        # Exact rationalization with t=tan(x), using the twice-double-angle
        # identity cos(4x)=(1-6t^2+t^4)/(1+t^2)^2. The interval excludes poles.
        t=s.symbols('t',positive=True)
        residual=s.cancel(residual.subs(s.cos(4*x),(1-6*t*t+t**4)/(1+t*t)**2).subs(s.tan(x),t))
    assert residual==0,(k,residual)
    checks.append({'derivative_order':k,'residual':str(residual)})
    prev=expected
# Reconstruct the fourth derivative separately in y=cot(2x) coordinates.
y=s.symbols('y',real=True)
third=-8*(s.asinh(y)/s.sqrt(1+y*y)+y)
fourth=s.simplify(s.diff(third,y)*(-2*(1+y*y)))
assert s.simplify(fourth-16*(2+y*y-y*s.asinh(y)/s.sqrt(1+y*y)))==0
checks.append({'representation':'y-coordinate derivative','residual':'0'})
out={'sympy_version':s.__version__,'domain':'0<x<pi/2; natural-log psi (bit conversion divides by ln2)','checks':checks,'runtime_seconds':time.perf_counter()-start,'scope':'symbolic differentiation only; asinh bound, strict concavity, and zero-count proof are mathematical arguments in PROOF.md','independent_acceptance':False}
(ROOT/'out'/'DERIVATIVE_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out),flush=True)
