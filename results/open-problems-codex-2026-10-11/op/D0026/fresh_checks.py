"""Small finite-cycle spectral and form checks; not an infinite-volume proof."""
import json,math,pathlib,time
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parent
start=time.monotonic(); records=[]
for n in range(3,8):
 for q in [0.03,0.1,0.3,0.5,0.8]:
  p=1-q;r=q/p;states=list(range(1,1<<n));index={a:i for i,a in enumerate(states)}
  mass=np.array([r**a.bit_count() for a in states]);rootmass=np.sqrt(mass)
  matrices={name:np.zeros((len(states),len(states))) for name in ['F','B','Q']}
  def add(name,a,b,rate):
   if a!=b:
    i=index[a];j=index[b];matrices[name][i,j]+=rate;matrices[name][i,i]-=rate
  for a in states:
   for x in range(n):
    l=(x-1)%n;rr=(x+1)%n;k=((a>>l)&1)+((a>>rr)&1)
    flip=p if a>>x&1 else q
    if k:
     add('F',a,a^(1<<x),flip);add('B',a,a^(1<<x),k*flip)
    if a>>x&1:
     base=a&~((1<<l)|(1<<rr))
     for b in [0,1]:
      for c in [0,1]:
       add('Q',a,base|(b<<l)|(c<<rr),(q if b else p)*(q if c else p))
  H={name:-L*rootmass[:,None]/rootmass[None,:] for name,L in matrices.items()}
  symerr=max(float(np.max(abs(M-M.T))) for M in H.values());assert symerr<1e-10
  eig={name:np.linalg.eigvalsh(M) for name,M in H.items()}
  gaps={name:float(e[1]) for name,e in eig.items()}
  assert gaps['Q']+1e-10>=gaps['F']/2
  forms={key:float(np.linalg.eigvalsh(M)[0]) for key,M in
    [('B-F',H['B']-H['F']),('2Q-B',2*H['Q']-H['B']),('B-Q',H['B']-H['Q'])]}
  assert min(forms.values())>=-1e-10
  lamb,V=np.linalg.eigh(H['Q']);A=index[1];t=4.0
  norm2=float(np.sum(np.exp(-2*t*lamb)*V[A,:]**2)/mass[A])
  Z=(1+r)**n-1
  rhs=math.exp(-2*gaps['Q']*t)/mass[A]+(1-math.exp(-2*gaps['Q']*t))/Z
  assert norm2<=rhs+1e-9
  records.append({'n':n,'q':q,'gaps':gaps,'form_min_eigenvalues':forms,
    'symmetry_error':symerr,'finite_density_norm2':norm2,'corrected_bound':rhs})

# Check the combinatorial generating-function bound in exact rational arithmetic.
from fractions import Fraction
entropy_checks=0
for L in range(1,41):
 for k in range(L+1):
  for r in [Fraction(1,9),Fraction(1),Fraction(4)]:
   theta=Fraction(1,5)
   lhs=sum(Fraction(math.comb(L,j))*r**j for j in range(k+1))
   rhs=theta**(-k)*(1+r*theta)**L
   assert lhs<=rhs
   entropy_checks+=1
result={'spectral_checks':records,'exact_weighted_binomial_checks':entropy_checks,
 'seconds':time.monotonic()-start,
 'scope':'No uniform-in-volume gap or long-time occupation conclusion is inferred from these small numerical matrices.'}
(ROOT/'fresh_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print('PASS:',len(records),'spectral/form cases;',entropy_checks,'exact binomial cases; seconds',result['seconds'])
