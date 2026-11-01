from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from functools import lru_cache
import json,time,math
P=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0;CERT={};SCALE=1<<100
def check(v):
 global checks
 assert v;checks+=1
 if time.monotonic()-start>60:raise TimeoutError('frozen pilot cap')
def series(t):
 z=(t-1)/(t+1);zz=z*z;p=z;a=Q(0)
 for k in range(30):a+=2*p/(2*k+1);p*=zz
 return a,a+2*p/(61*(1-zz))
ln2=series(Q(2))
@lru_cache(None)
def log(n):
 k=n.bit_length()-1
 if n==1<<k:return k*SCALE,k*SCALE
 a,b=series(Q(n,1<<k));a=(k+a/ln2[1])*SCALE;b=(k+b/ln2[0])*SCALE
 return a.numerator//a.denominator,-((-b.numerator)//b.denominator)
@lru_cache(None)
def factors(n):
 ans=[];p=2
 while p*p<=n:
  c=0
  while n%p==0:n//=p;c+=1
  if c:ans.append((p,c))
  p+=1 if p==2 else 2
 if n>1:ans.append((n,1))
 return ans
def certificate(expr):
 normalized=Counter()
 for n,c in expr.items():
  for p,e in factors(n):normalized[p]+=c*e
 normalized={p:c for p,c in normalized.items() if c};den=1
 for c in normalized.values():den=math.lcm(den,c.denominator)
 terms=tuple(sorted((p,int(c*den)) for p,c in normalized.items()))
 if terms in CERT:return CERT[terms]['sign']
 low=high=0
 for p,c in terms:
  a,b=log(p);low+=c*(a if c>=0 else b);high+=c*(b if c>=0 else a)
 check(not terms or low>0 or high<0)
 sign=0 if not terms else (1 if low>0 else -1)
 CERT[terms]={'terms':[[str(p),str(c)] for p,c in terms],'denominator':str(den),'sign':sign,'low':str(low),'high':str(high)}
 return sign
def fw(vals):
 a=vals[:];h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):x,y=a[j],a[j+h];a[j]=x+y;a[j+h]=x-y
  h*=2
 return a
def ent(vals):
 N=len(vals);expr=Counter({N*N:Q(1)})
 for x in fw(vals):
  if x:expr[x*x]-=Q(x*x,N*N)
 return expr
def influence(vals):
 N=len(vals);n=N.bit_length()-1;out=[]
 for i in range(n):out.append(Q(2*sum(vals[x]!=vals[x^(1<<i)] for x in range(N) if not x>>i&1),N))
 return out
def B(vals):
 a=fw(vals[::2]);b=fw(vals[1::2]);den=len(vals)**2;expr=Counter()
 for u,v in zip(a,b):
  x=(u+v)**2;y=(u-v)**2;t=x+y
  for n,c in ((t,t),(x,-x),(y,-y)):
   if n:expr[n]+=Q(c,den)
 return expr
def combine(dst,src,c=Q(1)):
 for n,v in src.items():dst[n]+=c*v
def case(G,H,s,label):
 alpha=Q(1,1<<s);gamma=Q(sum(g!=h for g,h in zip(G,H)),len(G));IG=influence(G);IH=influence(H);product=[g*h for g,h in zip(G,H)];IP=influence(product)
 vals=[H[x>>s] if x% (1<<s)==0 else G[x>>s] for x in range(len(G)<<s)];IF=influence(vals)
 IS=2*s*alpha*gamma;IT=(1-alpha)*sum(IG)+alpha*sum(IH);R=2*alpha*(1-alpha)*sum(IP)
 check(sum(IF[:s])==IS);check(sum(IF[s:])==IT);check(sum(IF)==IS+IT)
 for a,b,k,actual in zip(IG,IH,IP,IF[s:]):
  check(actual==(1-alpha)*a+alpha*b);check(k<=a+b);check(2*alpha*(1-alpha)*k<=2*alpha*((1-alpha)*a)+2*(1-alpha)*(alpha*b))
 E=Counter();live=vals;reach=Q(1)
 for j in range(s):combine(E,B(live),reach);live=live[::2];reach/=2
 check(live==H)
 target=E.copy();target[2]-=Q(5,2)*IS+R;check(certificate(target)<=0)
 delta=ent(vals);combine(delta,ent(G),-(1-alpha));combine(delta,ent(H),-alpha);delta[2]-=Q(11,2)*IS+R;check(certificate(delta)<=0)
 if gamma:
  # Verify the sharp geometric bound using c<=81/56; all other terms exact.
  bound=E.copy();b=4*alpha*gamma*(1-alpha);bound[2]-=2*(1-2*alpha)*IS+b*Q(81,56);bound[gamma.denominator]-=b;bound[gamma.numerator]+=b;check(certificate(bound)<=0)
 return {'label':label,'s':s,'gamma':str(gamma),'I_selector':str(IS),'I_terminal':str(IT),'R':str(R),'checks':'PASS'}
rows=[]
with (P/'out/REVIEW_ROWS.jsonl').open('w') as out:
 for gm in range(16):
  G=[1 if gm>>x&1 else -1 for x in range(4)]
  for hm in range(16):
   H=[1 if hm>>x&1 else -1 for x in range(4)]
   for s in (1,2,3):
    row=case(G,H,s,[gm,hm]);rows.append(row);out.write(json.dumps(row)+'\n');out.flush()
 for m in (4,6):
  seed=[(-1)**sum(((x>>(2*k))&1)*((x>>(2*k+1))&1) for k in range(m//2)) for x in range(1<<m)];edit=seed[:];edit[0]*=-1
  G=[seed[x%(1<<m)]*(-1 if x>>m else 1) for x in range(1<<(m+1))];H=[edit[x%(1<<m)]*(-1 if x>>m else 1) for x in range(1<<(m+1))]
  for s in (1,2):
   row=case(G,H,s,['bent_edit',m]);rows.append(row);out.write(json.dumps(row)+'\n');out.flush()
result={'cases':len(rows),'assertions':checks,'distinct_certificates':len(CERT),'seconds':time.monotonic()-start,'status':'PASS','rows':rows,'certificates':list(CERT.values()),'scale':str(SCALE),'scope':'A023 v3 additional whole-block entropy/erasure/reserve theorem; earlier bundled claims excluded'}
(P/'out/REVIEW_RESULTS.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k not in ('rows','certificates')}))
