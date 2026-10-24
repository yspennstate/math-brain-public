import itertools,json,math
from pathlib import Path
from collections import Counter
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
from scipy.special import dawsn

result={'date':'2026-10-12','exact_parity':[],'quadrature':[],'monte_carlo':[]}
for n in range(2,10):
 signs=[s for s in itertools.product((-1,1),repeat=n) if math.prod(s)==1]
 assert len(signs)==2**(n-1)
 for j in range(n):
  for subset in itertools.combinations(range(n),j):
   counts=Counter(tuple(s[i] for i in subset) for s in signs)
   assert len(counts)==2**j and set(counts.values())=={2**(n-j-1)}
 result['exact_parity'].append({'n':n,'all_proper_subsets_checked':True})
A=lambda t:2/math.sqrt(math.pi)*dawsn(t/math.sqrt(2))
c=.5*math.sqrt(2/math.pi)*math.exp(-.5)
for n in [1,3,5,7,9,15,31]:
 val,err=quad(lambda t:A(t)**n/t if t else (math.sqrt(2/math.pi) if n==1 else 0),0,math.inf,epsabs=1e-13,epsrel=1e-10,limit=150)
 lower=math.log(2)/math.pi*c**n
 assert val/math.pi+err/math.pi>=lower
 result['quadrature'].append({'n':n,'absolute_probability_error':val/math.pi,'estimated_quad_error':err/math.pi,'proved_lower_bound':lower,'signed_direction':(-1)**((n-1)//2)})
rng=np.random.default_rng(170)
N=200000
for n in [3,5,7]:
 hits=0
 for start in range(0,N,10000):
  signs=rng.choice([-1,1],size=(10000,n))
  signs[:,-1]=np.prod(signs[:,:-1],axis=1)
  x=signs*np.abs(rng.standard_normal((10000,n)))
  hits+=int(np.sum(np.sum(x,axis=1)>=0))
 observed=hits/N-.5
 exact=next(v for v in result['quadrature'] if v['n']==n)
 target=exact['absolute_probability_error']*exact['signed_direction']
 se=math.sqrt((.5+target)*(.5-target)/N)
 result['monte_carlo'].append({'n':n,'samples':N,'observed_signed_error':observed,'quadrature_signed_error':target,'standard_error':se,'z_score':(observed-target)/se})
 assert abs(observed-target)<6*se
root_cases=0
for multiplicities in itertools.product(range(5),repeat=3):
 degree=sum(multiplicities)
 if not 1<=degree<=6:continue
 roots=[(r,m) for r,m in zip([-1,0,1],multiplicities) if m]
 for leading in [-1,1]:
  def polynomial(x):return leading*math.prod((x-r)**m for r,m in roots)
  base=int(polynomial(Fraction(-3))>=0)
  terms=[]
  for r,m in roots:
   left=polynomial(Fraction(r)-Fraction(1,4))>0
   right=polynomial(Fraction(r)+Fraction(1,4))>0
   if m%2:
    if right:terms.append((1,r,True))
    else:terms.append((-1,r,False))
   elif not left:terms.extend([(1,r,True),(-1,r,False)])
  assert sum(abs(c) for c,r,closed in terms)<=degree
  for x in [Fraction(i,4) for i in range(-12,13)]:
   representation=base+sum(coef*int(x>=r if closed else x>r) for coef,r,closed in terms)
   assert representation==int(polynomial(x)>=0)
  root_cases+=1
result['exact_root_representation']={'polynomials_checked':root_cases,'grid':'all quarter-integers from -3 to 3, including every root','arithmetic':'exact Fraction','max_degree':6,'leading_signs':'both'}
result['constants']={'c':c,'cdf_constant_bound':717/23,'claimed_cdf_constant':32,'root_atom_example':'q(s)=-s^2: event is singleton {0}; requires coefficient cost 2'}
assert 717/23<32
# Numerical kernel checks use a finite cutoff and proved tail error bounds.
def K(v):return 3/(4*math.pi)*(math.sin(v/2)/(v/2))**4 if v else 3/(4*math.pi)
cut=100.
norm,ne=quad(K,0,cut,epsabs=1e-11,limit=200)
moment,me=quad(lambda v:v*K(v),0,cut,epsabs=1e-11,limit=200)
result['kernel']={'normalization_truncated':2*norm,'normalization_tail_upper':8/(math.pi*cut**3),'first_absolute_moment_truncated':2*moment,'first_moment_tail_upper':12/(math.pi*cut**2),'proved_first_moment_upper':51/(4*math.pi)}
assert abs(1-2*norm)<=8/(math.pi*cut**3)+2*ne
assert 2*moment+12/(math.pi*cut**2)<51/(4*math.pi)
Path('checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2),flush=True)
