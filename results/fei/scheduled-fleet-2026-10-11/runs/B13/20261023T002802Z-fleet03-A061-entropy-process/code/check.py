"""Independent core-only normalized transport and complete pending-booking DP."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,hashlib,time,sys
ROOT=Path(__file__).resolve().parents[1]
COUNT=0;NODES=0;QUERIES=0;RECORDS=[];BASIS=1<<96
def ck(b,label='assertion'):
 global COUNT
 COUNT+=1
 if not b:raise AssertionError(label)
def plus(*terms):
 d={}
 for a,x in terms:
  for p,v in x.items():d[p]=d.get(p,F())+a*v
 return {p:v for p,v in d.items() if v}
def const(x):return {2:F(x)} if x else {}
@lru_cache(None)
def factor(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p=3 if p==2 else p+2
 if n>1:out[n]=out.get(n,0)+1
 return out
def log(x):
 ck(x>0,'positive logarithm')
 return plus((1,{p:F(v) for p,v in factor(x.numerator).items()}),(-1,{p:F(v) for p,v in factor(x.denominator).items()}))
def ln_unit(x):
 z=(x-1)/(x+1);ck(0<=z<=F(1,3),'atanh range');s=F();power=z
 for k in range(32):s+=power/F(2*k+1);power*=z*z
 lo=2*s;hi=lo+2*power/(65*(1-z*z));return lo,hi
LN2=ln_unit(F(2))
@lru_cache(None)
def plog(p):
 if p==2:return F(1),F(1)
 e=p.bit_length()-1;x=F(p,1<<e);lo,hi=ln_unit(x)
 a=e+lo/LN2[1];b=e+hi/LN2[0]
 return F(a.numerator*BASIS//a.denominator,BASIS),F(-((-b.numerator*BASIS)//b.denominator),BASIS)
def interval(d):
 lo=F();hi=F()
 for p,a in d.items():
  l,h=plog(p)
  lo+=a*(l if a>=0 else h);hi+=a*(h if a>=0 else l)
 return lo,hi
def nonneg(d,label):
 if d:ck(interval(d)[0]>=0,label)
 else:ck(True,label)
def strict(d,label):ck(bool(d) and interval(d)[0]>0,label)
def maximum(x,y):
 d=plus((1,x),(-1,y))
 if not d:return x
 lo,hi=interval(d);ck(lo>0 or hi<0,'resolved max sign')
 return x if lo>0 else y
def positive(d):return maximum(d,{})
def entropy(p):return plus(*[(-x,log(x)) for x in p if x])
def kl(p,q):
 ck(len(p)==len(q),'KL domain')
 ck(all(not a or b>0 for a,b in zip(p,q)),'reference supports actual source')
 return plus(*[(a,log(a/b)) for a,b in zip(p,q) if a])
def fw(a):
 a=list(a);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
@lru_cache(None)
def stats(table):
 N=len(table);n=N.bit_length()-1;w=fw(table);p=tuple(F(v*v,N*N) for v in w);ck(sum(p)==1,'Parseval')
 ds=[]
 for j in range(n):
  d=sum((p[s] for s in range(N) if s>>j&1),F());edges=F(sum(table[s]!=table[s^(1<<j)] for s in range(N)),N)
  ck(d==edges,'independent physical influence');ds.append(d)
 H=entropy(p);M=plus(*[(1,entropy([d,1-d])) for d in ds]);TC=plus((1,M),(-1,H));nonneg(TC,'Gibbs TC')
 return p,tuple(ds),H,M,TC
def insert(s,j,b):return (s&((1<<j)-1))|((s>>j)<<(j+1))|(b<<j)
def child(t,j,b):return tuple(t[insert(s,j,b)] for s in range(len(t)//2))
def transport(table,j,R):
 p,ds,H,M,TC=stats(table);ck(sum(R)==1,'reference normalized');K=kl(p,R)
 cs=[child(table,j,b) for b in [0,1]];pc=[stats(c)[0] for c in cs]
 pe=tuple(p[insert(s,j,0)]+p[insert(s,j,1)] for s in range(len(p)//2));Re=tuple(R[insert(s,j,0)]+R[insert(s,j,1)] for s in range(len(p)//2))
 un=[];reach=[]
 for b in [0,1]:
  z=tuple(Re[s]*(pc[b][s]/(2*pe[s]) if pe[s] else F(1,2)) for s in range(len(pe)))
  un.append(z);reach.append(sum(z))
 ck(sum(reach)==1 and all(x>0 for x in reach),'positive normalized predictions')
 Rc=[tuple(x/reach[b] for x in un[b]) for b in [0,1]]
 Kc=[kl(pc[b],Rc[b]) for b in [0,1]];O=plus((F(-1,2),log(4*reach[0]*reach[1])));E=plus((1,K),(-1,kl(pe,Re)))
 ck(not plus((1,K),(-1,E),(-1,O),(F(-1,2),Kc[0]),(F(-1,2),Kc[1])),'exact common-kernel chain')
 nonneg(E,'nonnegative erasure');nonneg(O,'nonnegative outcome cost')
 childds=[stats(c)[1] for c in cs]
 for k in range(len(ds)-1):
  orig=k if k<j else k+1;ck(ds[orig]==(childds[0][k]+childds[1][k])/2,'surviving influence martingale')
 drop=plus((1,M),(F(-1,2),stats(cs[0])[3]),(F(-1,2),stats(cs[1])[3]));nonneg(drop,'marginal entropy supermartingale')
 return cs,Rc,reach,O,E,Kc,sum((Re[s] for s in range(len(pe)) if not pe[s]),F())
def enc(d):return {str(p):str(v) for p,v in sorted(d.items())}
def value(d):return {'exact':enc(d),'interval':[str(x) for x in interval(d)]}
def refhash(R):return hashlib.sha256(','.join(map(str,R)).encode()).hexdigest()
def analyze(table,R,depth,ids,path,pilot=False):
 global NODES,QUERIES
 NODES+=1;p,ds,H,M,TC=stats(table);K=kl(p,R);b=positive(plus((1,TC),(-1,K)));Bs=[b for _ in range(depth+1)];candidates=[]
 for i in (range(len(ids)) if not pilot else ([0] if ids else [])):
  if not depth:break
  QUERIES+=1;cs,Rc,reach,O,E,Kc,refs=transport(table,i,R)
  children=[analyze(cs[z],Rc[z],depth-1,ids[:i]+ids[i+1:],path+[(ids[i],z)],pilot) for z in [0,1]]
  for d in range(1,depth+1):
   candidate=plus((F(1,2),children[0][d-1]),(F(1,2),children[1][d-1]),(-1,E));Bs[d]=maximum(Bs[d],candidate)
  candidates.append((E,children,O))
 for d,B in enumerate(Bs):
  nonneg(plus((1,M),(-1,B)),'pending B<=same original M envelope')
  nonneg(plus((1,K),(1,B),(-1,TC)),'complete terminal TC retained')
  if d:nonneg(plus((1,B),(-1,Bs[d-1])),'nested policy bookings')
 for E,ch,O in candidates:
  for d in range(1,depth+1):nonneg(plus((1,E),(1,Bs[d]),(F(-1,2),ch[0][d-1]),(F(-1,2),ch[1][d-1])),'every queried potential drift pays O')
 RECORDS.append({'path':path,'remaining_ids':ids,'depth':depth,'reference_sha256':refhash(R),'H':value(H),'M':value(M),'K':value(K),'TC':value(TC),'B_by_depth':[value(x) for x in Bs]})
 return Bs
def mul(a,b,l,poly):
 c=0
 while b:
  if b&1:c^=a
  b>>=1;a<<=1
  if a>>l:a^=poly
 return c
def core(l):
 q=1<<l;poly={1:3,2:7,3:11}[l];h=[]
 for s in range(q**3):
  a=s&(q-1);b=(s>>l)&(q-1);x=s>>(2*l)
  h.append((-1 if a&1 else 1)*(-1 if x==mul(a,b,l,poly) else 1))
 return tuple(h)
def initial(h):
 p=stats(h)[0];N=len(h);wh=tuple(F(0) if s==0 else F(1) if p[s] else F(1,2) for s in range(N));wg=tuple(1-x for x in wh)
 rh=sum(wh)/N;rg=sum(wg)/N
 return tuple(x/(N*rh) for x in wh),tuple(x/(N*rg) for x in wg),rg,rh
def run(l,pilot):
 beforeN,beforeQ=NODES,QUERIES;h=core(l);p,ds,H,M,TC=stats(h);R,RG,rg,rh=initial(h);m=3*l;q=1<<l
 ck(p[0]==0,'balanced actual core');ck(rg==F(1,2*q),'original full-support selector prediction including reference-only rows')
 pp=F(2,q)-F(2,q*q);formula=plus((2*l,entropy([pp,1-pp])),(l,entropy([F(2,q),1-F(2,q)])))
 ck(M==formula,'physical marginal entropy field formula')
 S=plus((1,const(2*m+2)),(F(-1,2),H));cap=F(3) if l==2 else F(39*l,32)
 Bs=analyze(h,R,2,list(range(m)),[],pilot);Ws=[plus((F(1,2),x)) for x in Bs]
 nonneg(plus((1,const(cap)),(F(-1,2),M)),'original rational envelope covers M/2')
 strict(plus((F(13,48),S),(-1,const(cap))),'strict13/48 original-owner cap')
 strict(plus((F(3,4),S),(-1,const(cap)),(F(-23,48),S)),'old quarter remains spent and>23/48 survives')
 nonneg(plus((1,Ws[2]),(-1,Ws[1])),'SECOND total includes first booking')
 strict(plus((F(1,50),S),(-1,Ws[1])),'reproduced original first-query frontier')
 # Constant G branch has M=0, hence exact B=0 for all ordinary histories.
 g=(1,)*len(h);ck(not stats(g)[3],'constant G has zero marginal reserve');nonneg(kl(stats(g)[0],RG),'G inherited KL')
 return {'l':l,'m':m,'queries':QUERIES-beforeQ,'nodes':NODES-beforeN,'r_G':str(rg),'S_original':value(S),'M_original':value(M),'W_depth0_1_2':[value(x) for x in Ws],'second_topup':value(plus((1,Ws[2]),(-1,Ws[1]))),'total_cap':str(cap),'unused_fraction_after_oldquarter':'>23/48','full_terminal_H_and_TC_retained':True}
def main():
 start=time.perf_counter();pilot='pilot' in sys.argv
 # Excluded l=1 boundary must not be silently included in the all-l support formula.
 boundary=core(1);_,_,rg,rh=initial(boundary);ck(rg==F(5,16) and rg!=F(1,4),'excluded width1 boundary')
 ck(3**12>2**19,'all-l h2(1/4)<13/16 exact scalar sign');ck(288<299,'width2 bank comparison')
 rows=[run(l,pilot) for l in ([2] if pilot else [2,3])]
 if not pilot:ck(QUERIES==219 and NODES==440,'exact frozen coverage')
 else:ck(QUERIES==3 and NODES==7,'pilot frozen coverage')
 elapsed=time.perf_counter()-start;ck(elapsed<55,'frozen runtime')
 out={'status':'PASS','exact_assertions':COUNT,'queries':QUERIES,'nodes':NODES,'seconds':elapsed,'roots':rows,'records':RECORDS,'arithmetic':'Fraction normalized transport, exact prime-log chain identities, outward rational atanh signs; no float entropy sign'}
 (ROOT/'out').mkdir(exist_ok=True);(ROOT/'out'/('PILOT.json' if pilot else 'SECOND_QUERY.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ['records','roots']}));print(json.dumps(rows))
if __name__=='__main__':main()
