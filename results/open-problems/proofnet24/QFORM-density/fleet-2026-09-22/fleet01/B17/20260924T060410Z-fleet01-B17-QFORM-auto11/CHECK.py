import sympy as sp
import json

k=sp.symbols('k', integer=True, positive=True)
m=k**4
alpha=1+1/m
eta=k/m

assert sp.simplify(alpha*(m-k-1)/m+eta-(1-(k+1)/k**8))==0
assert sp.simplify((3*m-3)*eta-(3*k-3/k**3))==0
row_action=sp.simplify(alpha**2/m+eta**2*(1-1/m))
row_expected=(k**2*(k**4-1)+(k**4+1)**2)/k**12
assert sp.simplify(row_action-row_expected)==0

same_plus=k**4+1-3*k
same_minus=k**4+1+3*k
diag_plus=k**4+1+3*k*(k**4-1)
diag_minus_abs=3*k*(k**4-1)-(k**4+1)
for K in range(2,100):
    vals=[same_plus.subs(k,K),same_minus.subs(k,K),diag_plus.subs(k,K),diag_minus_abs.subs(k,K)]
    assert all(v>0 for v in vals)

assert sp.Rational(1,80)-sp.Rational(1,12)**2==sp.Rational(1,180)

eps,R=sp.symbols('eps R', positive=True)
ell=1-eps
x=sp.symbols('x', real=True)
mu2=sp.integrate(x**2,(x,-ell/2,ell/2))+2*sp.integrate(x**2,(x,R-eps/4,R+eps/4))
mu4=sp.integrate(x**4,(x,-ell/2,ell/2))+2*sp.integrate(x**4,(x,R-eps/4,R+eps/4))
mu2_formula=ell**3/sp.Integer(12)+eps*R**2+eps**3/sp.Integer(48)
mu4_formula=ell**5/sp.Integer(80)+eps*R**4+eps**3*R**2/sp.Integer(8)+eps**5/sp.Integer(1280)
assert sp.simplify(mu2-mu2_formula)==0
assert sp.simplify(mu4-mu4_formula)==0

tau=sp.Rational(1,12)
profile=sp.simplify(3*sp.sqrt(2)/(1+12*tau))
assert profile==3/sp.sqrt(2)
assert float(profile)<2.13

print(json.dumps({
  'status':'PASS',
  'theorem':'QFORM-ESCAPING-MODE-DIVERGENT-SUBCRITICAL-MASS-v1',
  'principal_bound_at_s_m_minus_k_minus_1':str(sp.simplify(alpha*(m-k-1)/m+eta)),
  'residual_l1_spectral_mass':str(sp.simplify((3*m-3)*eta)),
  'row_action_sq':str(row_action),
  'uniform_var_x2':'1/180',
  'satellite_mu2_formula':str(mu2_formula),
  'satellite_mu4_formula':str(mu4_formula),
  'profile_tau_1_over_12':str(profile),
  'profile_tau_1_over_12_float':float(profile)
}, indent=2))
