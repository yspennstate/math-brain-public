from fractions import Fraction as F
from pathlib import Path
import json

u,v=F(1,3),F(2,3)
m1=((1-u)+(1-v))/2
m2=((1-u)**2+(1-v)**2)/2
rho=(u/(1-u)+v/(1-v))/2
assert m2-m1*m1 == F(1,36)
assert rho == F(5,4)
c,h=F(1,2),F(1,4)
normalization=32*h*h/2
critical_density=c*32*h
assert normalization==1 and critical_density==4
assert 5>critical_density
upper_empty=1-c/(c+h)
assert upper_empty==F(1,3)<F(1,2)
results={'arithmetic':'exact rational, all assertions passed',
 'stationary_example_density':str(rho),'covariance':str(m2-m1*m1),
 'disorder_normalization':str(normalization),'critical_density':str(critical_density),
 'critical_empty_probability_upper_bound':str(upper_empty)}

# Exhaustive global balance on small periodic parity chains, restricted to
# configurations with total particle count at most 8. Every move stays in
# this finite set, so this is a meaningful finite-state stationarity check.
import itertools
def compositions(total,n):
 if n==1:
  yield (total,)
 else:
  for k in range(total+1):
   for rest in compositions(total-k,n-1): yield (k,)+rest
checked=0
for n in range(2,7):
 for total in range(9):
  for eta in compositions(total,n):
   outgoing=sum(x>0 for x in eta)
   incoming=0
   for j in range(n):
    k=(j+1)%n
    if eta[k]>0:
     pred=list(eta); pred[j]+=1; pred[k]-=1
     assert sum(pred)==sum(eta)
     incoming+=1
   assert incoming==outgoing
   checked+=1
results['finite_cycle_global_balance_states']=checked
aa,bb=F(3,5),F(7,10)
h0,h2=1-c/aa,1-c/bb
limit_cov=(1+h0*h2)/2-((1+h0)/2)*((1+h2)/2)
assert limit_cov==c*c/(4*aa*bb)==F(25,168)
results['iid_actual_limit_covariance_example']=str(limit_cov)
results['new_covariance_check']='exact rational, passed'
Path('checks.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,indent=2))
