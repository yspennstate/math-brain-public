from fractions import Fraction as F
import itertools,json,pathlib,math
# Exact local hidden-chain verification and noise bounds.
r=F(3,4)
local=[]
for t in [F(0),F(1,100),F(1,20),F(1,10)]:
 P=[[1-(1-r)*t,(1-r)*t],[(1-r)*(1-t),r+(1-r)*t]]
 assert (1-t)*P[0][1]==t*P[1][0]
 assert P[0][0]*P[1][1]-P[0][1]*P[1][0]==r
 a=F(1,10)+t/10;b=F(3,4)+t/10
 assert b-a==F(13,20)
 local.append({'t':str(t),'transition_determinant':str(r),'emission_determinant':str(b-a)})
comparisons=0
for s,t in itertools.combinations([F(-1,10),F(-1,20),F(0),F(1,100),F(1,20),F(1,10)],2):
 delta=(t-s)/10
 for S1,S2 in [(0,0),(0,1),(1,1)]:
  if s<=0 and S1==1:continue
  if t<=0 and S2==1:continue
  p1=F(1,10)+s/10+F(13,20)*S1
  p2=F(1,10)+t/10+F(13,20)*S2
  assert p1<=p2*(1-delta)
  assert p1+delta*(1-p1)<=p2
  comparisons+=1
z=r*F(3,4);u=(2*z-1)/(z*z);theta=F(3,4)*(1-(1-z*u)**3)
assert theta==F(193,486)
enhancement=(F(1,2)-F(1,10))/(1-F(1,10));assert enhancement==F(4,9)
chi=F(1,10)+3*F(1,10)**2/(1-2*F(1,10));assert chi==F(11,80)
pmax=F(11,100);chimax=pmax+3*pmax*pmax/(1-2*pmax)
upper=1+4*chimax;assert upper<2
out={'local_hidden_chain_checks':local,'exact_noise_comparison_cases':comparisons,'selected_internal_survival':str(theta),'independent_enhancement_threshold':str(enhancement),'endpoint_susceptibility_unconditional':str(chi),'upper_theta_over_t_bound':str(upper),'all_checks_passed':True}
pathlib.Path('second_countermodel_checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
