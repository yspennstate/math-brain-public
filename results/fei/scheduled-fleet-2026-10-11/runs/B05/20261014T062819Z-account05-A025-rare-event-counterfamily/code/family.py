from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from functools import lru_cache
import json,time,math
P=Path(__file__).resolve().parents[1];start=time.monotonic();CK=0;SCALE=1<<100;CERT=[]
def check(x):
 global CK
 assert x;CK+=1
 if time.monotonic()-start>60:raise TimeoutError('frozen pilot cap')
def series(t):
 z=(t-1)/(t+1);p=z;s=Q(0)
 for j in range(36):s+=2*p/(2*j+1);p*=z*z
 return s,s+2*p/(73*(1-z*z))
LN2=series(Q(2))
@lru_cache(None)
def log(n):
 k=n.bit_length()-1
 if n==1<<k:return k*SCALE,k*SCALE
 a,b=series(Q(n,1<<k));a=(k+a/LN2[1])*SCALE;b=(k+b/LN2[0])*SCALE
 return a.numerator//a.denominator,-((-b.numerator)//b.denominator)
def cert(expr,label):
 terms={n:c for n,c in expr.items() if c and n>1};den=1
 for c in terms.values():den=math.lcm(den,c.denominator)
 terms=sorted((n,int(c*den)) for n,c in terms.items());lo=hi=0
 for n,c in terms:
  a,b=log(n);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
 check(not terms or lo>0 or hi<0);sign=0 if not terms else(1 if lo>0 else -1)
 CERT.append({'label':label,'terms':[[str(n),str(c)] for n,c in terms],'denominator':str(den),'sign':sign,'low':str(lo),'high':str(hi)});return sign
def fw(vals):
 a=vals[:];h=1
 while h<len(a):
  for k in range(0,len(a),h*2):
   for j in range(k,k+h):u,v=a[j],a[j+h];a[j]=u+v;a[j+h]=u-v
  h*=2
 return a
def entropy(vals):
 N=len(vals);e=Counter({N*N:Q(1)})
 for x in fw(vals):
  if x:e[x*x]-=Q(x*x,N*N)
 return e
def combine(dst,src,scale=Q(1)):
 for n,c in src.items():dst[n]+=scale*c
def erasure(vals,i):
 a=fw(vals);N=len(a);out=Counter();d=Q(0)
 for j in range(N):
  if j>>i&1:continue
  u,v=a[j]**2,a[j^(1<<i)]**2;t=u+v;d+=Q(v,N*N)
  for n,c in ((t,t),(u,-u),(v,-v)):
   if n:out[n]+=Q(c,N*N)
 return out,d
def influences(vals):
 N=len(vals);return [Q(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N) for i in range(N.bit_length()-1)]
def split(vals,i,bit):
 return [vals[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(len(vals)//2)]
def build(m,t):
 data=[]
 for x in range(1<<(m+2)):
  y=x% (1<<m);xbit=x>>m&1;z=-1 if x>>(m+1)&1 else 1;b=(-1)**sum((y>>(2*k)&1)*(y>>(2*k+1)&1) for k in range(m//2));g=z*b
  data.append([g,g*(-1 if y==0 and not xbit else 1),g*(-1 if y==1 and not xbit else 1)])
 cores=[[row[j] for row in data] for j in range(3)]
 vals=[data[x%len(data)][0 if x>>(m+2)&1 else(1 if x>>(m+3)&1 else 2)] for x in range(len(data)*4)]
 if t:
  cores=[[g[x>>t] if x%(1<<t)==0 else 1 for x in range(len(g)<<t)] for g in cores];vals=[vals[x>>t] if x%(1<<t)==0 else 1 for x in range(len(vals)<<t)]
 return cores,vals
def bank(cores):
 pi=[Q(1,2),Q(1,4),Q(1,4)];return 2*sum(pi[i]*pi[j]*sum(influences([a*b for a,b in zip(cores[i],cores[j])])) for i in range(3) for j in range(i+1,3))
def compressed(m):
 delta=Q(1,1<<m);D=1<<(2*m+2);root=Counter({2:3*delta/4});counts=[(1,(1<<(m-2))+(1<<(m//2-1))),(-1,(1<<(m-2))-(1<<(m//2-1)))]
 for sig,count in counts:
  a=(sig*(1<<(m//2+1))-1)**2
  root[a+1]+=Q(count*(a+1),D);root[a]-=Q(count*a,D)
 d=delta/2;release=3*delta/4;target=root.copy();target[2]-=4*d+release;sgn=cert(target,['B-4d-release',m])
 check(sum(c for _,c in counts)==1<<(m-1));check(Q(1,D)*sum(c for _,c in counts)==delta/8)
 if m>=18:check(sgn>0);check(Q(m,4)+Q(3,2)>Q(11,2))
 return root,{'m':m,'d':str(d),'release':str(release),'I':str(1+Q(m,2)+(m+2)*delta/2),'root_bank':str((3*m+2)*delta/4),'remaining_expected_bank':str((3*m-1)*delta/4),'B_over_d_rigorous_lower':str(Q(3,2)+Q(m,4)),'B_minus_4d_release_sign':sgn}
rows=[]
with (P/'out/ROWS.jsonl').open('w') as out:
 for m in range(4,33,2):
  expr,row=compressed(m)
  for t in (0,m):
   entry=dict(row,t=t,n=m+4+t,activation_scale=str(Q(1,1<<t)));rows.append(entry);out.write(json.dumps(entry)+'\n');out.flush()
direct=[]
for m in (4,6,8):
 baseB,_=compressed(m)
 for t in (0,1):
  a=Q(1,1<<t);delta=Q(1,1<<m);cores,vals=build(m,t);i=m+t;actual=influences(vals);B,d=erasure(vals,i);c0=split(vals,i,0);c1=split(vals,i,1);R=bank(cores);R0=bank([split(g,i,0) for g in cores]);R1=bank([split(g,i,1) for g in cores]);release=R-(R0+R1)/2
  expectedI=a*(1+Q(m,2)+(m+2)*delta/2+t);check(sum(actual)==expectedI);check(d==actual[i]==a*delta/2);check(release==a*3*delta/4)
  for k in range(3):check(sum(cores[k])==0 if not t else sum(cores[k])==len(cores[k])*(1-a))
  # Exact rational-log cancellation at direct dimensions uses power transport:
  # evaluate sign of each difference only after prime normalization.
  difference=B.copy();combine(difference,baseB,-a)
  normalized=Counter()
  for n,c in difference.items():
   p=2;v=n
   while p*p<=v:
    while v%p==0:normalized[p]+=c;v//=p
    p+=1 if p==2 else 2
   if v>1:normalized[v]+=c
  check(not any(normalized.values()))
  H=entropy(vals);combine(H,entropy(c0),Q(-1,2));combine(H,entropy(c1),Q(-1,2));combine(H,B,Q(-1));check(cert(H,['JS_nonnegative',m,t])>0)
  rate=entropy(vals);rate[2]-=6*expectedI;check(cert(rate,['H-6I',m,t])<0)
  direct.append({'m':m,'t':t,'n':m+4+t,'I':str(sum(actual)),'d':str(d),'R_root':str(R),'release':str(release),'erasure_compression':'exact prime cancellation PASS'})
result={'status':'PASS','compressed_entries':len(rows),'direct_cases':len(direct),'assertions':CK,'certificates':CERT,'certificate_count':len(CERT),'seconds':time.monotonic()-start,'rows':rows,'direct':direct,'scale':str(SCALE)}
(P/'out/RESULTS.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k not in ('rows','direct','certificates')}))
