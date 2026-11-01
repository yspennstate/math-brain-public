import json,time
from fractions import Fraction as F
import transitive as base
import transitive_v2 as bounded
base.logint=bounded.logint
ROOT=base.ROOT
def expr_entropy(weights,den):
 raw={};base.addlog(raw,den,1)
 for v in weights:
  if v:base.addlog(raw,v,-F(v,den))
 return raw
def add(a,b,s=1):
 c=dict(a)
 for k,v in b.items():
  c[k]=c.get(k,F(0))+s*v
  if not c[k]:del c[k]
 return c
def mass_entropy(weights):
 den=weights[0].denominator
 # Separate denominators need no common allocation assumption.
 e={}
 for p in weights:
  if p:base.lograt(e,p,-p)
 return e
def erasure(weights,n,j):
 e={};bit=1<<j
 for s in range(1<<n):
  if not s&bit:
   a,b=weights[s],weights[s|bit]
   if a and b:base.phi(e,a,b)
 return e
def main():
 start=time.perf_counter();d=json.loads((ROOT/'out'/'transitive_certificates.json').read_text());out=[];exact_checks=0
 selected=None
 for r in d['records']:
  n=r['n'];W=r['Walsh'];N=1<<n
  # Independent inverse character sum for the selected overlapping benchmark.
  if r['name']=='cyclic-window-10-2-1':
   f=[1 if any((x>>j)&1 and (x>>((j+1)%n))&1 for j in range(n)) else -1 for x in range(N)]
   direct=[sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(f)) for s in range(N)]
   assert direct==W;exact_checks+=N;selected=r['name']
  pp=[F(v*v,N*N) for v in W]
  H={int(p):F(c) for p,c in r['H_prime_log'].items()}
  parentB={int(p):F(c)/n for p,c in r['B_prime_log'].items()}
  wc=[[(W[2*t]+sign*W[2*t+1])//2 for t in range(N//2)] for sign in [1,-1]]
  assert all((W[2*t]+sign*W[2*t+1])%2==0 for t in range(N//2) for sign in [1,-1])
  childlaws=[[F(v*v,(N//2)**2) for v in ws] for ws in wc]
  marginal=[(a+b)/2 for a,b in zip(*childlaws)]
  assert add(H,mass_entropy(marginal),-1)==parentB;exact_checks+=1
  for sign,law in zip([1,-1],childlaws):
   assert sum(law)==1
   entries=[];I=F(0)
   for j in range(n-1):
    inf=sum(p for s,p in enumerate(law) if s&(1<<j));I+=inf
    if not inf:continue
    e=erasure(law,n-1,j);bounds=base.interval(e)
    entries.append({'coordinate':j+1,'I_i':str(inf),'B_i_prime_log':base.serial(e),'ratio_interval':base.iv((bounds[0]/inf,bounds[1]/inf))})
    exact_checks+=1
    if not parentB:
     # Conditional joint entropy of original spectral bits (0,j+1).
     pair={}
     i_bit=1;j_bit=1<<(j+1)
     for s in range(N):
      if not s&i_bit and not s&j_bit:
       masses=[pp[s],pp[s|i_bit],pp[s|j_bit],pp[s|i_bit|j_bit]]
       q=sum(masses)
       if q:
        for p in masses:
         if p:base.lograt(pair,p,-p)
        base.lograt(pair,q,q)
     assert pair==e;exact_checks+=1
   if not parentB:
    assert law==[pp[2*t]+pp[2*t+1] for t in range(N//2)]
    assert mass_entropy(law)==H;exact_checks+=2
   # The minimum is enclosed without pretending uncertain near ties are ordered.
   minimum=base.iv((min(F(e['ratio_interval']['lower']) for e in entries),min(F(e['ratio_interval']['upper']) for e in entries))) if entries else None
   out.append({'parent':r['name'],'branch':sign,'I_child':str(I),'H_child_prime_log':base.serial(mass_entropy(law)),'min_relevant_B_over_I':minimum,'coordinate_rows':entries})
  parentI=F(r['I']);di=F(r['I_i'])
  assert parentI==di+(F(out[-1]['I_child'])+F(out[-2]['I_child']))/2;exact_checks+=1
  if time.perf_counter()-start>55:raise RuntimeError('bounded child check')
 assert len(out)==138
 result={'helper_version':'A026-first-child-erasure-v1','status':'PASS','cases':len(out),'exact_checks':exact_checks,'direct_Walsh_benchmark':selected,'elapsed_seconds':time.perf_counter()-start,'records':out}
 (ROOT/'out'/'child_certificates.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
if __name__=='__main__':main()
