from fractions import Fraction as F
from math import comb
import json,pathlib

def compositions(total,m):
 if m==1:
  yield (total,); return
 for k in range(total+1):
  for tail in compositions(total-k,m-1): yield (k,)+tail
checked=0
for m in range(2,7):
 for total in range(9):
  states=list(compositions(total,m)); incoming={e:F(0) for e in states}; outgoing={e:F(0) for e in states}
  q=F(2,3); rate=F(1,2)
  for e in states:
   w=(1-q)**m*q**sum(e)
   for j in range(m):
    if e[j]>0:
     target=list(e); target[j]-=1; target[(j+1)%m]+=1; target=tuple(target)
     incoming[target]+=w*rate; outgoing[e]+=w*rate
  assert incoming==outgoing
  checked+=len(states)
u,v=F(1,3),F(2,3)
mean=((u/(1-u))+(v/(1-v)))/2
empty=((1-u)+(1-v))/2
joint=((1-u)**2+(1-v)**2)/2
cov=joint-empty**2
assert mean==F(5,4) and cov==F(1,36)
c=F(1,2); top=F(3,4)
normalization=16*(top-c)**2; critical=c*32*(top-c)
assert normalization==1 and critical==4 and F(10,2)>critical
assert 1-c/top==F(1,3)<F(1,2)
# Verify iid-limit covariance on an exact grid of allowed site rates.
for a in (F(9,16),F(5,8),F(11,16)):
 for b in (F(9,16),F(5,8),F(11,16)):
  h0,h2=1-c/a,1-c/b
  computed=(1+h0*h2)/2-(1+h0)*(1+h2)/4
  assert computed==c*c/(4*a*b)>0
result={'finite_cycle_states':checked,'cycles':[2,3,4,5,6],'total_occupations':list(range(9)),'mean':str(mean),'stationary_covariance':str(cov),'disorder_integral':str(normalization),'critical_density':str(critical),'initial_density':5,'critical_empty_probability_supremum':'1/3 (not attained)','persistent_empty_probability_lower_bound':'1/2','limit_covariance_grid_pairs':9,'all_assertions_passed':True}
pathlib.Path('independent_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
