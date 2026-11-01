import json,time
from fractions import Fraction as F
import transitive as base
import transitive_v2 as bounded
base.ln_norm=bounded.ln_norm;base.LN2=bounded.LN2;base.logint=bounded.logint
START=time.perf_counter()
def rawadd(d,k,v):
 if k>1 and v:d[k]=d.get(k,0)+v
def canonical(raw,D):
 e={}
 for v,c in raw.items():base.addlog(e,v,F(c,D))
 return e
def statistics(name,f,n,meta):
 N=1<<n;D=N*N;W=base.walsh(f);squares=[v*v for v in W]
 assert sum(squares)==D
 rawH={2:2*n*D}
 for a in squares:rawadd(rawH,a,-a)
 H=canonical(rawH,D);bi=[];influences=[]
 for i in range(n):
  bit=1<<i;raw={};d=F(sum(squares[s] for s in range(N) if s&bit),D)
  assert d==F(sum(f[x]!=f[x^bit] for x in range(N)),N)
  for t in range(N):
   if not t&bit:
    a,b=squares[t],squares[t|bit]
    if a and b:rawadd(raw,a+b,a+b);rawadd(raw,a,-a);rawadd(raw,b,-b)
  bi.append(canonical(raw,D));influences.append(d)
 assert all(d==influences[0] for d in influences)
 assert all(e==bi[0] for e in bi)
 B=base.mul(bi[0],n);I=sum(influences);HH=base.interval(H);BB=base.interval(B)
 result={'name':name,'n':n,**meta,'I':str(I),'I_i':str(influences[0]),'H_prime_log':base.serial(H),'B_prime_log':base.serial(B),'H_interval':base.iv(HH),'B_interval':base.iv(BB),'H_over_I':base.iv((HH[0]/I,HH[1]/I)),'B_over_I':base.iv((BB[0]/I,BB[1]/I)),'B_over_H':base.iv(base.divide(BB,HH)) if HH[0]>0 else None,'support_count':sum(v!=0 for v in W),'Walsh':W}
 with (base.ROOT/'out'/'transitive_rows_v3.jsonl').open('a',encoding='utf-8') as out:out.write(json.dumps(result)+'\n')
 if time.perf_counter()-START>55:raise RuntimeError('v3 bounded pilot limit')
 return result,H,B,influences[0],W
if __name__=='__main__':
 assert not (base.ROOT/'out'/'transitive_rows_v3.jsonl').exists(), 'use a new version if restarting'
 base.statistics=statistics;base.main()
 for name in ['transitive_certificates.json','transitive_summary.json']:
  p=base.ROOT/'out'/name;r=json.loads(p.read_text(encoding='utf-8'))
  r['helper_version']='A026-transitive-true-erasure-v3'
  r['rounding']='All logarithm intervals outward-rounded to denominator 2^140'
  p.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print('Final output helper_version: A026-transitive-true-erasure-v3')
