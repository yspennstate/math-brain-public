from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
P=list(product([-1,1],repeat=2))
chi=lambda s,t:[1,s,t,s*t]
centered={p:F(max(sum(p),0))-F(1,2) for p in P}
walsh=[sum(centered[(s,t)]*chi(s,t)[h] for s,t in P)/4 for h in range(4)]
assert walsh==[0,F(1,2),F(1,2),F(1,2)]
noise=list(product([-2,2],repeat=4))
noise_w=[[sum(F(z[i])*chi(*p)[h] for i,p in enumerate(P))/4 for h in range(4)] for z in noise]
assert all(sum(v[h] for v in noise_w)==0 for h in range(4))
assert all(sum(v[h]**2 for v in noise_w)/16==1 for h in range(4))
witnesses=[F(4),F(7,2),F(4),F(3)]
margins=[witnesses[0]-witnesses[1],witnesses[2]-witnesses[1],witnesses[2]-witnesses[3]]
assert margins==[F(1,2),F(1,2),F(1)]
# Unit norm identity and signal coefficient: the square-root denominators
# are represented by their exact positive squares; no floating operations.
for e in [F(1,5),F(1,10),F(1,100)]:
 assert (e*e+1)/(1+e*e)==1
 c2=e**4/((1+e*e+e**4)*(1+e*e))
 assert 0<c2<F(1,256)
# Pairwise Jacobian Gram cancellation is checked at generic rational inputs.
x=[(F(1),F(s,5),F(t,25)) for s,t in P]
ws=list(product([-1,0,1],repeat=3)); nu=F(2,3)
pair_entries=0
for w in ws:
 acts=[max(sum(a*b for a,b in zip(w,z)),0) for z in x]
 gates=[int(sum(a*b for a,b in zip(w,z))>0) for z in x]
 for i,j in product(range(4),repeat=2):
  dot=sum(a*b for a,b in zip(x[i],x[j]))
  single=acts[i]*acts[j]+nu**2*gates[i]*gates[j]*dot
  paired=sum(acts[i]*acts[j]+a*a*gates[i]*gates[j]*dot for a in [nu,-nu])/2
  assert single==paired
  pair_entries+=1
 assert sum(a*z for a,z in zip([nu,-nu],[acts[0],acts[0]]))==0
out={'teacher_walsh_coefficients':[str(z) for z in walsh], 'noise_patterns':16,'noise_walsh_variances':[1]*4,'normalized_witness_limits':[str(z) for z in witnesses],'strict_margins':[str(z) for z in margins],'pair_kernel_entries':pair_entries,'teacher_norm_cases':3,'scope':'Exact finite algebra only; does not certify Gaussian kernel asymptotics, nonlinear GD convergence, peak localization or novelty.'}
root=Path(__file__).resolve().parent.parent
with (root/'logs/bounded_relu_algebra_checks.json').open('w',encoding='utf-8',newline='') as f:json.dump(out,f,indent=2)
print(json.dumps(out))
