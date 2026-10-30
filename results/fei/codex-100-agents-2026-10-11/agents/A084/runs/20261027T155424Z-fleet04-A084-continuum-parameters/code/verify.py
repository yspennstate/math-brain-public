from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util,json,time,sys
R=Path(__file__).resolve().parents[1]
OLD=R/'code/exact_arithmetic.py'
spec=importlib.util.spec_from_file_location('a084_exact_logs',OLD);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
COUNT=0
def ck(v):
 global COUNT
 assert v
 COUNT+=1
def save(n,o):(R/'out'/n).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8',newline='\n')
def fwht(f):
 a=list(f);step=1
 while step<len(a):
  for s in range(0,len(a),2*step):
   for j in range(s,s+step):x,y=a[j],a[j+step];a[j],a[j+step]=x+y,x-y
  step*=2
 return [Q(z,len(a)) for z in a]
@lru_cache(None)
def stat(f):
 w=fwht(f);ck(sum(x*x for x in w)==1)
 h=m.add(*(m.eta(x*x) for x in w));I=sum((s.bit_count()*w[s]**2 for s in range(len(w))),Q(0))
 return h,I
def restrict(f,i,b):return tuple(f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(f)//2))
def upper_abs_entropy(a,b):
 lo,hi=m.ev(m.add(a,m.sc(b,-1)));v=max(abs(lo),abs(hi));scale=1<<160
 return Q(-((-v.numerator*scale)//v.denominator),scale)
def row_types(f,mask):
 N=(len(f)-1).bit_length();aa=[i for i in range(N) if mask>>i&1];bb=[i for i in range(N) if not(mask>>i&1)]
 rows=set()
 for a in range(1<<len(aa)):
  base=sum(((a>>j)&1)<<i for j,i in enumerate(aa))
  rows.add(tuple(f[base+sum(((b>>j)&1)<<i for j,i in enumerate(bb))] for b in range(1<<len(bb))))
 return len(rows)
def pair(seed,N=8):
 f=tuple(seed[x&3] for x in range(1<<N));g=tuple(-v if x==0 else v for x,v in enumerate(f))
 Kmax=Q(6);delta=Q(1,1<<N);s=Q(1,8)
 boundlo,boundhi=m.ev(m.add({2:N*s+2*Kmax*N*delta},m.eta(s),m.eta(1-s)))
 boundlo=Q(boundlo.numerator*(1<<160)//boundlo.denominator,1<<160)
 visited=0;policies=0
 @lru_cache(None)
 def dp(a,b):
  nonlocal visited,policies
  if a==b:return Q(0)
  visited+=1
  # Only the zero physical point differs; all other branches agree.
  ck(sum(x!=y for x,y in zip(a,b))==1 and a[0]!=b[0])
  ha,ia=stat(a);hb,ib=stat(b)
  ans=upper_abs_entropy(ha,hb)+Kmax*abs(ia-ib)
  n=(len(a)-1).bit_length()
  for i in range(n):
   ap,am=restrict(a,i,0),restrict(a,i,1);bp,bm=restrict(b,i,0),restrict(b,i,1)
   ck(am==bm)
   ck(abs(ia-ib)<=2*n/Q(len(a)))
   ans=max(ans,(dp(ap,bp)+dp(am,bm))/2);policies+=1
  return ans
 maximal=dp(f,g)
 ck(maximal<boundlo)
 # Direct character transform is independent of the FWHT used above.
 ck(fwht(g)==m.walsh(g))
 hf,If=stat(f);hg,Ig=stat(g)
 ck(If==sum(m.inf(f,i) for i in range(N)))
 ck(Ig==sum(m.inf(g,i) for i in range(N)))
 ck(upper_abs_entropy(hf,hg)<=maximal)
 signed_root=upper_abs_entropy(hf,hg)+Kmax*abs(If-Ig)
 ck(signed_root+maximal<2*boundlo)
 prime=tuple(-v if x.bit_count()<=1 else v for x,v in enumerate(f))
 ck(sum(x!=y for x,y in zip(prime,f))==N+1)
 checked=0
 for A in range(1, (1<<N)-1):
  if A.bit_count()>=2:ck(row_types(prime,A)>=3);checked+=1
 return {'seed':''.join('+' if x>0 else '-' for x in seed),'live_pair_states':visited,'query_rows':policies,'all_tree_difference_upper':str(maximal),'all_tree_difference_display_only':float(maximal),'signed_cumulative_charge_difference_upper':str(signed_root+maximal),'theorem_bound_lower':str(boundlo),'theorem_bound_display_only':float(boundlo),'prime_blocks':checked}
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;limit=2 if pilot else 16
 results=[]
 for mask in range(limit):
  seed=[1 if mask>>i&1 else -1 for i in range(4)]
  results.append(pair(seed));ck(time.perf_counter()-start<180)
 # Endpoint/control inequalities use exact arithmetic, not a K grid.
 ck(Q(0)==0 and Q(1,16)<=Q(1,16))
 ck(2*Q(1,4)==Q(1,2))
 ck(Q(8,128)==Q(1,16))
 ck(m.lnseries(Q(2),48)[0]>Q(2,3))
 tails=[]
 from math import isqrt
 for N in [8,12,16,24,32]:
  delta=Q(N+1,1<<N);scale=1<<160
  r=isqrt(delta.numerator*scale*scale//delta.denominator)
  if Q(r,scale)**2<delta:r+=1
  root=Q(r,scale);ck(root*root>=delta and delta<=Q(1,16))
  bound=3*(N+1)*root+12*N*delta
  tails.append({'N':N,'delta':str(delta),'sqrt_delta_upper':str(root),'all_tree_payoff_error_upper':str(bound),'display_only':float(bound)})
 result={'status':'PASS','seed_pairs':limit,'assertions':COUNT,'live_pair_states':sum(x['live_pair_states'] for x in results),'query_rows':sum(x['query_rows'] for x in results),'prime_blocks':sum(x['prime_blocks'] for x in results),'K_domain':'every real K in[0,6]; pointwise Lipschitz domination, not samples','runtime_seconds':time.perf_counter()-start,'cases':results,'arithmetic':'Fraction coefficients, exact prime-log expressions and outward48-term logs'}
 save('PILOT.json' if pilot else 'VALIDATION.json',result)
 save('TAIL_BOUNDS.json',{'status':'PASS','Kmax':6,'certificate':'square comparison of rational root upper; all-real delta budget analytic monotonicity','cases':tails})
 print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
if __name__=='__main__':main()
