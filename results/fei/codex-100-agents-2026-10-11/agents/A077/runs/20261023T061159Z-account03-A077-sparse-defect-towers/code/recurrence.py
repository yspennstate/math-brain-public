"""Independent rational recurrence audit, no main arithmetic imported."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json,time,itertools
root=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;cases=[]
def eq(a,b):
 global checks
 assert a==b,(a,b)
 checks+=1
 assert time.perf_counter()-start<55
for n in range(4,129,2):
 alpha=Q(comb(n,n//2),1<<n)
 odd={2*l+1:(-1)**l*alpha*Q(comb(n//2,l),comb(n,2*l)) for l in range(n//2+1)}
 beta=[odd[k+1] if k%2==0 else odd[k] for k in range(n+1)]
 for k in range(1,n,2):eq(odd[k+2],-Q(k,n-k)*odd[k])
 product=2*sum((comb(n-1,k)*abs(beta[k]*beta[k+1]) for k in range(n)),Q(0))
 even=sum((comb(n-1,k)*odd[k+1]**2 for k in range(0,n,2)),Q(0))
 influence=sum((comb(n-1,k)*beta[k+1]**2 for k in range(n)),Q(0))
 eq(product,4*even);eq(influence,alpha);eq(sum((comb(n,k)*beta[k]**2 for k in range(n+1)),Q(0)),1)
 eq(8*Q(1,1<<(n//2))+16*Q(1,1<<n)<=8*alpha,True)
 eq(4*(n+1)*Q(1,1<<(n+1))<=2*alpha,True)
 if n in (4,6,8):
  t=[1 if s.bit_count()<=n//2 else -1 for s in range(1<<n)]
  direct=[Q(sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(t)),len(t)) for s in range(len(t))]
  for s,a in enumerate(direct):eq(a,beta[s.bit_count()])
  for j in range(n):eq(Q(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)),alpha)
 cases.append({'n':n,'alpha':str(alpha),'adjacent_product_sum':str(product),'cross_upper_bound':str(8*Q(1,1<<(n//2))+16*Q(1,1<<n)),'extra_to_influence_ratio':str((8*Q(1,1<<(n//2))+16*Q(1,1<<n))/alpha)})
out={'status':'PASS','exact_assertions':checks,'even_dimensions':len(cases),'seconds':time.perf_counter()-start,'cases':cases,'all_dimensional_bridge':'PROOF sections1-2 exact recurrence and monotone ratio; finite checks alone not that bridge'}
(root/'out/RECURRENCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
