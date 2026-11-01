from pathlib import Path
import json,math,random
R=Path(__file__).resolve().parent
results=[]
def record(name,details): results.append({'check':name,**details})
# Two free sites in a chain with zero endpoints, H=|x|+|x-y|+|y|.
# Full-wall Z=1/2 and f_i(0)=1. Test f_i(t)=(2t+1)e^-2t,
# F_i(t)=1-(t+1)e^-2t against the degree-2 contact bound.
errors=[]
for h in [0,.001,.1,.5,1,2,4,8]:
 F=1-(h+1)*math.exp(-2*h)
 bound=(math.exp(2*h)-1)/2
 errors.append(F-bound)
record('two_site_chain_contact',{'Z_positive':.5,'contact_sum':2,'boundary_edges':2,'max_probability_minus_bound':max(errors),'exact_mean':.75})
# Compare the exact free marginal MGF to the flow-product bound.
# Unit electrical flow is (2/3,1/3,1/3), energy 2/3.
diff=[]
for k in range(1,990):
 lam=k/1000
 exact=(2/3)*sum(1/(2+s*lam)**2+1/(2+s*lam) for s in [-1,1])
 bound=1/((1-lam*lam*4/9)*(1-lam*lam/9)**2)
 diff.append(exact-bound)
record('two_site_chain_mgf',{'lambda_grid':'0.001 through 0.989','max_exact_minus_flow_bound':max(diff)})
# Rank-one determinant identity randomized arithmetic check.
rng=random.Random(72); worst=0
for _ in range(1000):
 a,b,c,u,v,r=[rng.uniform(-3,3) for _ in range(6)]
 left=(a+r*u*u)*(c+r*v*v)-(b+r*u*v)**2
 right=a*c-b*b+r*(a*v*v+c*u*u-2*b*u*v)
 worst=max(worst,abs(left-right))
record('rank_one_det',{'trials':1000,'max_absolute_error':worst})
# Exact rational Polya-urn endpoint probabilities and flow bounds, including
# early killing on an off-centre finite square/cube. Small jobs only.
from fractions import Fraction
for d in [2,3,4]:
 for N in [1,2,3]:
  for start in [tuple([0]*d),tuple([N]*d),tuple([-N]*d)]:
   live={start:Fraction(1)};energy=Fraction(0);out=Fraction(0);k=0;maxedge=Fraction(0)
   while live:
    nxt={}
    shell_energy=Fraction(0)
    for pos,p in live.items():
     for j in range(d):
      t=p*Fraction(pos[j]-start[j]+1,k+d)
      maxedge=max(maxedge,t);shell_energy+=t*t
      q=list(pos);q[j]+=1;q=tuple(q)
      if q[j]>N:out+=t
      else:nxt[q]=nxt.get(q,Fraction(0))+t
    M=math.comb(k+d-1,d-1)
    assert shell_energy<=Fraction(1,M)
    energy+=shell_energy;live=nxt;k+=1
   assert out==1 and maxedge<=1
   K=1+math.log(4*N+2) if d==2 else 2
   assert float(energy)<=K
   record('stopped_flow',{'d':d,'N':N,'start':start,'exit_mass':str(out),'energy':float(energy),'K_bound':K,'steps':k})
(R/'checks.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for x in results[:3]:print(json.dumps(x))
print('Exact rational flow checks passed:',len(results)-3,'configurations')
