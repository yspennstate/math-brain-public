"""Independent symbolic and numerical checks used in the report."""
import os
for key in ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[key] = "1"
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad
import sympy as s

assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
x,z=s.symbols('x z', real=True)
U=x**4/20-4*x**3/15+x**2/5+8*x/5
M=(z-2)**2/5
W=(s.diff(U,x).subs(x,z)-M*s.sqrt(z*z-4))/2
expansion=s.series(W,z,s.oo,5)
rho=lambda t: (t+2)**.5*(2-t)**2.5/(10*np.pi)
mass=quad(rho,-2,2,epsabs=1e-12)[0]
rows=[]
for k in [0,1,2,3]:
 p=s.Rational(1,2*k+1);a=s.Rational(k,2*k+1);d=s.Rational(1,4*k+3)
 assert s.simplify(1-2*a-p)==0
 assert s.simplify(d*(2+p)-p)==0
 rows.append(dict(k=k,p=str(p),a=str(a),mesh_exponent=str(d),
                  eigenvalue_exponent=str(2*d),operator_tail=str(s.Rational(3,2)-a),
                  kernel_tail=str(s.Rational(4*k+3,2))))
D,L=s.symbols('D L')
aa=(-D+L)/2;bb=1-(D+L)/4
stationary=s.expand((aa**3+6*aa*bb**2-4*aa**2-8*bb**2+2*aa+8)/10)
mass_profile=s.expand(1-bb**2*(3*aa**2+3*bb**2-8*aa+2)/5)
assert s.series(stationary.subs(L,s.Rational(5,128)*D**3),D,0,4).removeO()==0
assert s.series(mass_profile.subs(L,s.Rational(5,128)*D**3),D,0,4).removeO()==D**3/8
result=dict(priority=os.getpriority(os.PRIO_PROCESS,0),quartic=str(U),
 stieltjes_expansion=str(expansion),mass=mass,exponents=rows,
 cv_edge_scale=float(6**(2/7)),
 formal_quartic_c=2,formal_quartic_gamma=float(2**(-6/7)),
 profile_stationarity=s.factor(stationary).__str__(),profile_mass=s.factor(mass_profile).__str__(),
 trial_A=10,trial_B_k1=30*float(s.beta(s.Rational(10,3),3).evalf()),
 trial_C_k1=900*float(s.beta(s.Rational(13,3),5).evalf()))
Path('data').mkdir(exist_ok=True)
Path('data/algebra_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
