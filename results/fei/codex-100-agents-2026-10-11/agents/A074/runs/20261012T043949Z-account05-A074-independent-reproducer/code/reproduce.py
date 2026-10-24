from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,hashlib,time,argparse
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]
SCALE=1<<64
checks=0
def check(x):
 global checks
 checks+=1
 assert x
def save(name,data):
 def encode(x):
  if isinstance(x,F):return str(x)
  if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
  if isinstance(x,(tuple,list)):return [encode(v) for v in x]
  return x
 (ROOT/'out'/name).write_text(json.dumps(encode(data),indent=2)+'\n',encoding='utf-8')
def lnunit(x):
 t=1-F(1)/x
 lo=sum((t**k/F(k) for k in range(1,41)),F(0))
 return lo,lo+t**41/(41*(1-t))
LN2=lnunit(F(2))
@lru_cache(None)
def log_interval(x):
 x=F(x);check(x>0);k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 if x==1:return F(k),F(k)
 a,b=lnunit(x)
 return F(k)+a/LN2[1],F(k)+b/LN2[0]
def add(acc,w,v):
 a,b=v
 if w<0:a,b=b,a
 return acc[0]+w*a,acc[1]+w*b
def scaled(v):return (v[0]*SCALE).__floor__(),(v[1]*SCALE).__ceil__()
KINT=(F(4),F(4))
KINT=add(KINT,F(5,2),log_interval(5))
KINT=add(KINT,-F(9,2),log_interval(3))
KS=scaled(KINT)
@lru_cache(None)
def packet(a,b):
 if not a or not b:return 0,0
 v=(F(0),F(0))
 for z,w in [(a+b,a+b),(a,-a),(b,-b)]:v=add(v,w,log_interval(z))
 return scaled(v)
@lru_cache(None)
def factors(z):
 out={};p=2
 while p*p<=z:
  while z%p==0:out[p]=out.get(p,0)+1;z//=p
  p+=1
 if z>1:out[z]=out.get(z,0)+1
 return out
def form_add(d,z,w):
 for p,k in factors(z).items():
  d[p]=d.get(p,F(0))+w*k
  if not d[p]:del d[p]
def erasure_form(squares,i,N):
 d={}
 for s in range(N):
  if s>>i&1:continue
  a,b=squares[s],squares[s|(1<<i)]
  if not a or not b:continue
  for z,w in [(a+b,a+b),(a,-a),(b,-b)]:form_add(d,z,F(w,N*N))
 return d
def form_interval(d):
 v=(F(0),F(0))
 for p,w in d.items():v=add(v,w,log_interval(p))
 return v
@lru_cache(None)
def chars(n):
 N=1<<n
 return [sum(1<<x for x in range(N) if (x&s).bit_count()%2) for s in range(N)]
def walsh(mask,n):
 N=1<<n;k=mask.bit_count()
 # Character sum of f=1-2*1_A; nonzero characters sum to zero.
 return [N-2*k]+[-2*(k-2*(mask&ch).bit_count()) for ch in chars(n)[1:]]
def edge_counts(mask,n):
 N=1<<n
 return [sum(((mask>>x)^(mask>>(x^(1<<i))))&1 for x in range(N) if not(x>>i&1)) for i in range(n)]
def restrict(mask,n,i,z):
 def lift(x):return (x&((1<<i)-1))|((x>>i)<<(i+1))|(z<<i)
 return sum(((mask>>lift(x))&1)<<x for x in range(1<<(n-1)))
def witness(n,mask,cutoff):
 N=1<<n;W=walsh(mask,n);a=[w*w for w in W];edges=edge_counts(mask,n)
 check(sum(a)==N*N)
 mu=[F(x,N*N) for x in a];rows=[]
 for x in range(N):check(sum(W[s]*(-1 if (x&s).bit_count()%2 else 1) for s in range(N))==N*(-1 if mask>>x&1 else 1))
 for i in range(n):
  inf=F(2*edges[i],N);check(inf==sum(mu[s] for s in range(N) if s>>i&1));check(inf>0)
  joint=[];B=(F(0),F(0));numeric=mp.mpf(0)
  for s in range(N):
   if s>>i&1:continue
   p0,p1=mu[s],mu[s|(1<<i)];q=p0+p1
   if not q:continue
   cond=[p0/q,p1/q];joint.append({'retained_mask':s,'joint':[p0,p1],'marginal':q,'conditional':cond})
   for p,c in zip([p0,p1],cond):
    if p:
     B=add(B,-p,log_interval(c))
     numeric-=mp.mpf(p.numerator)/p.denominator*mp.log(mp.mpf(c.numerator)/c.denominator,2)
  ratio=(B[0]/inf,B[1]/inf)
  check(ratio[0]>cutoff);check(ratio[0]>KINT[1])
  form=erasure_form(a,i,N);check(form_interval(form)[0]<=B[1] and B[0]<=form_interval(form)[1])
  children=[]
  for z in [0,1]:
   childmask=restrict(mask,n,i,z);cw=walsh(childmask,n-1);cmu=[F(w*w,(N//2)**2) for w in cw]
   check(sum(cmu)==1);children.append({'negative_mask':childmask,'spectrum':cmu})
  for j in range(1<<(n-1)):
   s=(j&((1<<i)-1))|((j>>i)<<(i+1))
   check((children[0]['spectrum'][j]+children[1]['spectrum'][j])/2==mu[s]+mu[s|(1<<i)])
  rows.append({'coordinate':i,'influence':inf,'edge_count':edges[i],'joint_packets':joint,'B_interval':B,'ratio_interval':ratio,'B_prime_log':form,'ratio_prime_log':{p:v/inf for p,v in form.items()},'mpmath_ratio_60digits':mp.nstr(numeric/(mp.mpf(inf.numerator)/inf.denominator),60),'children':children})
 first=min(range(n),key=lambda i:rows[i]['ratio_interval'][0]);minimum=[]
 for i in range(n):
  if rows[i]['ratio_prime_log']==rows[first]['ratio_prime_log']:minimum.append(i)
  else:check(rows[i]['ratio_interval'][0]>rows[first]['ratio_interval'][1])
 source=Path(f'~/brain_workers/FEI100_20261011/agents/A072/runs/20261012T004036Z-account05-A072-exact-walsh-engine/out/witness_n{n}.json')
 data=source.read_bytes();src=json.loads(data)
 check(W==src['certificate']['walsh']);check(mu==list(map(F,src['certificate']['spectrum'])));check(minimum==src['minimum_coordinates'])
 check(rows[first]['ratio_prime_log']=={int(p):F(v) for p,v in src['minimum_prime_log'].items()})
 for row,other in zip(rows,src['certificate']['coordinates']):
  check(row['influence']==F(other['influence']));check(row['B_prime_log']=={int(p):F(v) for p,v in other['B_prime_log'].items()})
 result={'n':n,'negative_mask':mask,'negative_assignments':[x for x in range(N) if mask>>x&1],'walsh':W,'spectrum':mu,'minimum_coordinates':minimum,'minimum_prime_log':rows[first]['ratio_prime_log'],'minimum_interval':rows[first]['ratio_interval'],'cutoff':cutoff,'coordinates':rows,'source_matches':True,'source_sha256':hashlib.sha256(data).hexdigest(),'mpmath_is_evidence_only':True}
 save(f'witness_n{n}.json',result)
 return {'n':n,'minimum_coordinates':minimum,'minimum_decimal':rows[first]['mpmath_ratio_60digits'],'source_matches':True}
def census(n,cap):
 start=time.perf_counter();N=1<<n;strict=equal=constants=0;ties=[];digest=hashlib.sha256();chosen={}
 path=ROOT/'out'/f'census_n{n}_decisions.jsonl'
 with path.open('w',encoding='utf-8',newline='\n') as out:
  for mask in range(1<<N):
   W=walsh(mask,n);a=[x*x for x in W];check(sum(a)==N*N)
   edges=edge_counts(mask,n);candidates=[];uncertain=[]
   for i in range(n):
    L=sum(a[s] for s in range(N) if s>>i&1);check(L==2*edges[i]*N)
    if not L:continue
    Glo=Ghi=0
    for s in range(N):
     if not(s>>i&1):
      lo,hi=packet(*sorted((a[s],a[s|(1<<i)])));Glo+=lo;Ghi+=hi
    if KS[0]*L>Ghi:candidates.append(i)
    elif KS[1]*L>=Glo:uncertain.append((i,L))
   if candidates:
    strict+=1;i=candidates[0];chosen[i]=chosen.get(i,0)+1;decision=[mask,'strict',i]
   elif not any(edges):constants+=1;decision=[mask,'constant',None]
   else:
    certified=[]
    for i,L in uncertain:
     d={2:F(4*L,N*N),5:F(5*L,2*N*N),3:-F(9*L,2*N*N)}
     for p,v in erasure_form(a,i,N).items():
      d[p]=d.get(p,F(0))-v
      if not d[p]:del d[p]
     if not d:certified.append(i)
    check(len(certified)==sum(e>0 for e in edges));equal+=1;ties.append(mask);decision=[mask,'equal',certified]
   line=json.dumps(decision,separators=(',',':'))+'\n';out.write(line);digest.update(line.encode())
   if mask%1024==0:check(time.perf_counter()-start<cap)
 expected=set()
 if n>=3:
  for free in range(n):
   inds=[i for i in range(n) if i!=free]
   for x in range(N):
    # Only n=3,4 can be embedded three-bit point defects at this stage.
    if n==3:pts=[x]
    elif n==4:pts=[x,x^(1<<free)]
    else:continue
    m=sum(1<<p for p in pts);expected.add(m);expected.add(((1<<N)-1)^m)
 check(set(ties)==expected)
 summary={'n':n,'tables':1<<N,'nonconstant':strict+equal,'strict':strict,'equal':equal,'constants':constants,'failures':0,'equality_masks':ties,'equality_class':'exactly embedded three-variable point defects (or output complements)' if n>=3 else 'none','decision_sha256':digest.hexdigest(),'chosen_coordinate_counts':chosen,'runtime_seconds':time.perf_counter()-start,'packet_cache_size':packet.cache_info().currsize}
 save(f'census_n{n}.json',summary);print(json.dumps(summary));return summary
def main():
 (ROOT/'out').mkdir(exist_ok=True);mp.mp.dps=60
 parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
 start=time.perf_counter();summaries=[]
 witnesses=[witness(5,4194372,F(539,200)),witness(6,1103806792023,F(368,125))]
 for n in range(4 if args.pilot else 5):summaries.append(census(n,55 if args.pilot else 240))
 result={'pilot':args.pilot,'witnesses':witnesses,'census':[{'n':s['n'],'tables':s['tables'],'strict':s['strict'],'equal':s['equal'],'constants':s['constants'],'failures':s['failures']} for s in summaries],'exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'Kstar_interval':KINT,'fixed_point_scale':SCALE,'float_sign_decisions':0}
 save('pilot_summary.json' if args.pilot else 'summary.json',result);print(json.dumps({k:v for k,v in result.items() if k!='Kstar_interval'}))
if __name__=='__main__':main()
