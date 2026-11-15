"""Independent finite-kernel and sampler checks; useful for the mathematical reduction."""
import math, json, random, collections, os
from pathlib import Path
from perimeter import h,hdown,w,step,nu_negative_pure,boundary_step
assert os.getpriority(os.PRIO_PROCESS,0)>=10

checks=[]
for p in [1,2,8,97]:
 for K in [2,4,32,1024]:
  a=h(p+K-1)/(h(p)*h(K))
  up=a+sum(nu_negative_pure(m,K)*h(p-m)/h(p) for m in range(1,p))
  down=hdown(p+K-1)/h(K)+sum(nu_negative_pure(m,K)*hdown(p-m) for m in range(1,p+1))
  checks.append(dict(p=p,K=K,up_residual=up-1,down_residual=down-hdown(p)))
assert max(abs(x['up_residual']) for x in checks)<2e-10
assert max(abs(x['down_residual']) for x in checks)<2e-10

# Check original-corner absorption against all four elementary oriented gluings.
class FixedRng:
 def __init__(self,edge=0,side=0): self.edge=edge; self.side=side
 def randrange(self,n): return self.edge%n
 def getrandbits(self,n): return self.side
b=[1,2,4,8,16,32,64,128]
assert boundary_step(FixedRng(),b,-1)==[5,8,16,32,64,128]
assert boundary_step(FixedRng(side=1),b,-1)==[130,64,32,16,8,4]
assert boundary_step(FixedRng(),b,1)==[1,0,0,2,4,8,16,32,64,128]
assert boundary_step(FixedRng(),b,-3)==[65,128]

hist=[]
p=8;n=30000
for model in ['quadrangulation','octangulation','dyadic_beta_080','dyadic_beta_035']:
 if model=='quadrangulation': components=[(2,1.)]
 elif model=='octangulation': components=[(4,1.)]
 else:
  beta=.8 if '080' in model else .35
  t=2**(-beta)
  components=[(2**j,(1-t)*t**(j-1)) for j in range(1,101)]
 expected={-m:sum(r*nu_negative_pure(m,K)*h(p-m)/h(p) for K,r in components) for m in range(1,p)}
 expected['positive']=sum(r*h(p+K-1)/(h(p)*h(K)) for K,r in components)
 rng=random.Random(571111)
 counts=collections.Counter()
 for _ in range(n):
  d=step(rng,p,model);counts[d if d<0 else 'positive']+=1
 zmax=0.
 for cat,prob in expected.items():
  observed=counts[cat]/n
  z=(observed-prob)/math.sqrt(prob*(1-prob)/n)
  zmax=max(zmax,abs(z))
  hist.append(dict(model=model,category=cat,expected=prob,observed=observed,z=z))
 assert zmax<5.0
out=dict(kernel_checks=checks,sampler_checks=hist,n_per_model=n,
         max_kernel_error=max(abs(x['up_residual']) for x in checks),
         max_sampler_z=max(abs(x['z']) for x in hist),
         boundary_cases=4,nice=os.getpriority(os.PRIO_PROCESS,0))
Path('data/verification.json').write_text(json.dumps(out,indent=2)+'\n')
print('kernel error',out['max_kernel_error'],'sampler max |z|',out['max_sampler_z'],'boundary cases pass')
