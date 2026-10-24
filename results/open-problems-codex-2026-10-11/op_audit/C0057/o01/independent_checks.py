from fractions import Fraction as F
from math import comb, sqrt, log
import json, pathlib, mpmath as mp
BASE=pathlib.Path(__file__).resolve().parent
mp.mp.dps=65
def d(n): return F(comb(2*n,n),4**n)
def h(n): return 2*n*d(n)
exact_rows=0
maxima={k:0.0 for k in ['delta','neg_second','pos_second','pos_tail','large_jump','log_drift','log_second']}
min_swallow=1e9
laws=[{1:F(1)},{2:F(1)},{7:F(1)},{31:F(1)}, {1:F(1,3),2:F(1,3),31:F(1,3)}, {1:F(1,2),7:F(1,4),31:F(1,4)}]
kernel_integral_checks=0
for beta in laws:
 # beta[m]=(m+1)*a_(m+1), so sum beta=1 imposes criticality.
 pos={m:b/((2*m+1)*d(m)) for m,b in beta.items()}
 Z=1/sum(F(m,m+1)*b for m,b in beta.items())
 def T(k): return sum(F(m)*b/F(m+k) for m,b in beta.items())
 def neg(k): return d(k)*T(k)/F(2*k-1)
 for k in range(1,26):
  # Integrate r^(k-1) J'(r) directly, independently of T notation.
  integral=Z*sum(b*(F(1,k)-F(1,k+m)) for m,b in beta.items())
  direct=F(1,2)/Z*d(k-1)*integral
  assert direct==neg(k)
  kernel_integral_checks+=1
 assert T(1)==1/Z
 for p in [1,2,3,4,5,8,9,16,17,32,64,127,256]:
  weights={p+m:v*h(p+m)/h(p) for m,v in pos.items()}
  weights.update({p-k:neg(k)*h(p-k)/h(p) for k in range(1,p)})
  assert sum(weights.values())==1
  delta=1-sum(pos.values())-sum(neg(k) for k in range(1,p))
  reciprocal=sum(v*h(p)/h(y) for y,v in weights.items())
  assert reciprocal==1-delta
  assert h(p+1)/h(p)==1+F(1,2*p)
  rate=float(T(p))/sqrt(p)
  large=sum(float(v) for y,v in weights.items() if abs(y-p)>p/2)
  increments=[(float(v),log(float(h(y)/h(p)))) for y,v in weights.items() if abs(y-p)<=p/2]
  drift=sum(v*u for v,u in increments)
  second=sum(v*u*u for v,u in increments)
  tests={'delta':float(delta),'neg_second':float(sum(F(k*k,p*p)*neg(k) for k in range(1,p+1))),
   'pos_second':float(sum(F(m*m,p*p)*v for m,v in pos.items() if m<=p)),
   'pos_tail':sum(sqrt(m/p)*float(v) for m,v in pos.items() if m>p/2),
   'large_jump':large,'log_drift':abs(drift),'log_second':second}
  for name,value in tests.items(): maxima[name]=max(maxima[name],value/rate)
  if p>=8:
   b=sum(neg(k+1)*h(p-k-1)/h(p)/2 for k in range((p+1)//2,p-1))
   min_swallow=min(min_swallow,float(b)/rate)
  exact_rows+=1
# Exact boundary-distance check: selected occurrence at 0, target at t;
# one side always has directed distance <=p and swallowed arc reaches past it.
geometry_cases=0
for p in range(8,101):
 for t in range(1,2*p):
  distance=min(t,2*p-t)
  assert distance<=p
  for k in range((p+1)//2,min((3*p)//4,p-2)+1):
   assert 2*k+1>distance
   geometry_cases+=1
# Independent high-precision quadrature of the zeta example.
C=1/(mp.zeta(3)-1); Z=(mp.zeta(3)-1)/(mp.zeta(3)-mp.zeta(4))
example=[]
for j in [1,2,7,20,100]:
 exact=Z*C*(-mp.zeta(3)/(j*(j+1))+mp.zeta(2)/(j*j)-(mp.digamma(j+1)+mp.euler)/j**3)
 quad=mp.quad(lambda r: r**j*Z*C*(mp.zeta(3)-(mp.polylog(3,r)/r if r else 1)),[0,mp.mpf('0.5'),1])
 example.append({'j':j,'absolute_error':str(abs(quad-exact)),'j_squared_I':str(j*j*exact)})
 assert abs(quad-exact)<mp.mpf('1e-58')
D=1+Z*C/2*(mp.zeta(2)-3*mp.zeta(3)+2*mp.zeta(4))
assert abs(2*D-Z*C*(mp.zeta(2)-mp.zeta(3)))<mp.mpf('1e-60')
result={'exact_transition_rows':exact_rows,'exact_kernel_integrals':kernel_integral_checks,
 'maximum_observed_ratios_to_R':maxima,'minimum_swallow_ratio_to_R_p_at_least_8':min_swallow,
 'boundary_geometry_cases':geometry_cases,'zeta_example_quadrature':example,
 'scope':'Finite exact laws and example checks only. Infinite-tail claims assessed analytically, not inferred from experiments.'}
(BASE/'independent_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
