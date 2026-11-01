from fractions import Fraction as F
from finite_dp import partitions,ROOT
import json,math
checks=0;exact_remainders=0
for n in range(2,21):
 for p in partitions(n):
  k=len(p);J=F(2,n)*sum((F(1,x) for x in p),F(0))+F(2*(k-2),n*n)
  rhs=F(0);rem=F(0)
  for i,x in enumerate(p):
   for y in p[i+1:]:
    d=F(1,x)+F(1,y)-F(1,x+y)
    delta=F(2,n)*d+F(2,n*n)
    rhs+=F(x*y,2)*delta*delta
    rem+=F(2*x*y,n*n)*(F(1,x+y)-F(1,n))**2
  assert rhs-J==rem
  assert rem>=0
  count_rate=sum((F(2,n)*x*y*(F(1,x)+F(1,y)-F(1,x+y))+F(2*x*y,n*n)
                  for i,x in enumerate(p) for y in p[i+1:]),F(0))
  assert count_rate>=F(3,2)*(k-1)
  if k==1: assert J==0
  if k==2: assert J==F(2,p[0]*p[1])
  if k>2: assert rem>0
  exact_remainders+=1
  if 1 in p:
   others=list(p);others.remove(1)
   hazard=sum((F(2,n)*(y+F(1,y+1))+F(2*y,n*n) for y in others),F(0))
   a=3-F(1,n)-F(2,n*n)
   assert hazard<=a
   assert hazard<=2+F(k,n)
   checks+=1
finite=[]
costs={r['n']:r for r in json.loads((ROOT/'certified_costs.json').read_text())}
for n in [2,3,4,8,16,32,100,1000,1000000]:
 a=3-1/n-2/n**2;t=n**(-1/(2*a));c=(.5-1/n)**2
 upper=2+2/n-4/n**2-c*((1-t**(2*a-1))/(2*a-1)-(1/n)*(1/t-1))
 if n in costs:
  assert costs[n]['display_midpoint']<=upper+1e-12
 finite.append({'n':n,'cutoff':t,'upper_display':upper})
result={'exact_sum_of_squares_states':exact_remainders,'exact_singleton_hazard_states':checks,
        'component_death_rate_comparison_states':exact_remainders,
        'sharper_singleton_hazard_comparison_states':checks,
        'finite_upper_comparisons':finite,'asymptotic_hazard_bound':39/20,
        'earlier_poisson_domination_bound':(33-18*math.exp(1/3))/4,
        'strongest_component_comparison_bound':(63-3*math.exp(-4/3))/32}
(ROOT/'referee_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
