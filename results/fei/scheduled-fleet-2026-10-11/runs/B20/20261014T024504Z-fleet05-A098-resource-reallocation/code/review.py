from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json,time,sys
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';start=time.perf_counter();count=0
def ck(x):
 global count
 count+=1;assert x,count
 assert time.perf_counter()-start<55,'Runtime guard'
@lru_cache(None)
def factor(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def addlog(a,weight,x):
 assert x>0
 for p,k in factor(x.numerator).items():a[p]+=weight*k
 for p,k in factor(x.denominator).items():a[p]-=weight*k
def clean(a):return {p:x for p,x in a.items() if x}
def combine(*terms):
 a=defaultdict(F)
 for coef,form in terms:
  for p,x in form.items():a[p]+=coef*x
 return clean(a)
def lnseries(x):
 z=(x-1)/(x+1);N=12
 lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
 return lo,lo+2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
ln2=lnseries(F(2))
@lru_cache(None)
def log2bounds(x):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=lnseries(x)
 return F(k)+lo/ln2[1],F(k)+hi/ln2[0]
def interval(form):
 lo=hi=F(0)
 for p,c in form.items():
  a,b=log2bounds(F(p));lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def decimal_out(x,upper=False):
 scale=10**12;v=(x.numerator*scale)//x.denominator
 if upper and F(v,scale)!=x:v+=1
 return str(F(v,scale))
def save(name,j):(OUT/name).write_text(json.dumps(j,indent=2)+'\n',encoding='utf-8')

pilot='--pilot' in sys.argv;results=[]
with (OUT/('PILOT_CASES.jsonl' if pilot else 'REVIEW_CASES.jsonl')).open('w',encoding='utf-8') as log:
 for d in ([2] if pilot else [2,4,6,8,10]):
  delta=F(1,2**d);t=F(1,2**(d//2));e=delta/2;n=d+2;size=2**n
  truth=[]
  for x in range(size):
   y=x&((1<<d)-1);u=x>>d&1;v=x>>(d+1)&1
   b=-1 if sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,d,2))%2 else 1
   truth.append(-1 if y==0 and u and v else b)
  a=truth[:];step=1
  while step<size:
   for base in range(0,size,2*step):
    for j in range(base,base+step):
     x,y=a[j],a[j+step];a[j]=x+y;a[j+step]=x-y
   step*=2
  p=[F(x*x,size*size) for x in a];ck(sum(p)==1);ck(all(x>0 for x in p))
  for s in range(size):
   core=s&((1<<d)-1);uv=s>>d
   sigma=-1 if sum(((core>>j)&1)*((core>>(j+1))&1) for j in range(0,d,2))%2 else 1
   expected=sigma*t-delta/2 if uv==0 else (-delta/2 if uv==3 else delta/2)
   ck(F(a[s],size)==expected)
  influences=[]
  for i in range(n):
   physical=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(size)),size)
   spectral=sum(p[s] for s in range(size) if s>>i&1)
   ck(physical==spectral);ck(physical==(e if i>=d else (1+delta)/2));influences.append(physical)
  ck(sum(influences)==F(d,2)+(F(d,2)+1)*delta)
  for i in [d,d+1]:
   partner=2*d+1-i;r={};mu={};groups=[[],[]]
   full=defaultdict(F)
   for s in range(size):
    if s>>i&1:continue
    r[s]=p[s]+p[s|(1<<i)];mu[s]=p[s|(1<<i)]/e
    groups[s>>partner&1].append(s)
    ck(mu[s]==delta/2);ck(r[s]>0)
    addlog(full,mu[s],mu[s]/r[s])
   ck(sum(r.values())==sum(mu.values())==1)
   rb=[sum(r[s] for s in g) for g in groups];mb=[sum(mu[s] for s in g) for g in groups]
   ck(rb==[1-e,e] and mb==[F(1,2),F(1,2)])
   binary=defaultdict(F);cond=defaultdict(F)
   for b in [0,1]:
    addlog(binary,mb[b],mb[b]/rb[b])
    for s in groups[b]:
     um=mu[s]/mb[b];rr=r[s]/rb[b]
     ck(um==delta)
     if b==1:ck(um==rr)
     else:addlog(cond,um,um/rr)
   ck(not combine((1,full),(-1,binary),(-F(1,2),cond)))
   lo,hi=interval(cond);ck(lo>0);ck(hi<F(1,2)-F(1,128))
   losslo,losshi=e*lo/2,e*hi/2
   ck(2*losshi<delta/4);ck(2*losshi<influences[0]/10)
   M=defaultdict(F);addlog(M,F(1),1/e)
   M=combine((1,M),(-1,full));ml,mh=interval(M)
   ck(ml>F(d,2)+F(3,4))
   row={'d':d,'query':i,'e':str(e),'D0_interval':[str(lo),str(hi)],
        'loss_over_e_outward_12digits':[decimal_out(lo/2),decimal_out(hi/2,True)],
        'M_over_e_lower_exceeds':str(F(d,2)+F(3,4)),
        'complete_conditional_KL_identity':'EXACT_PRIME_LOG_ZERO','reserve':'two losses < core_y1 influence /10; remainder only'}
   results.append(row);log.write(json.dumps(row)+'\n');log.flush()
  ck(F(d+2,1)/sum(influences)<=2+F(4,d))
 ck(7**128<2**63*5**128)
summary={'status':'PASS','function_cases':1 if pilot else 5,'queried_rows':len(results),'assertions':count,
 'runtime_seconds':time.perf_counter()-start,'memory_estimate_mb':70,
 'arithmetic':'exact Fraction/prime-log identity, fixed N12 rational error bounds','source_code_imported':False}
save('PILOT_CHECK.json' if pilot else 'REVIEW_CHECK.json',summary)
if not pilot:save('REMAINDER_ROWS.json',results)
print(json.dumps(summary))
