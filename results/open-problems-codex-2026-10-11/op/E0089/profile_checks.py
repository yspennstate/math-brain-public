from pathlib import Path
import itertools,json,math
from fractions import Fraction as Q
N=4;size=16;verified=0
for truth in range(1,2**16-1):
 f=[(truth>>x)&1 for x in range(16)]
 if any(f[x]>f[x|1<<i] for x in range(16) for i in range(4) if not x&(1<<i)):continue
 g=[Q(sum(f[x] for x in range(16) if x.bit_count()==m),math.comb(4,m)) for m in range(5)]
 edges=sum(f[x|1<<i]-f[x] for x in range(16) for i in range(4) if not x&(1<<i))
 I=Q(edges,8)
 assert I==4*sum(Q(math.comb(3,m),8)*(g[m+1]-g[m]) for m in range(4))
 ones=sum(f);joint=sum(3**(4-(x^y).bit_count()) for x in range(16) for y in range(16) if f[x] and f[y]);cov=Q(joint-16*ones**2,4096)
 assert cov>=Q(1,2)*Q(1,4)*I*I/4
 for a in range(4):
  for b in range(a+1,5):
   beta=min(Q(math.comb(3,m),8) for m in range(a,b))
   assert cov>=Q(1,2)*Q(1,4)*4*beta*beta*(g[b]-g[a])**2
 verified+=1
out=dict(nonconstant_monotone_functions=verified,bits=4,p='1/2',eps='1/2',checks=['Bernstein profile/Russo identity','degree-one noise covariance bound','all fixed-layer profile bounds'],arithmetic='exact Python Fraction')
assert verified==166
Path('profile_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(out)
