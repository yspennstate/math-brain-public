from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util,json,time,argparse,hashlib

RUN=Path(__file__).resolve().parents[1]
OLD=Path(__file__).with_name('log_intervals.py')
sp=importlib.util.spec_from_file_location('own_logs',OLD); c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
c.lg=lru_cache(None)(c.lg)
S=c.S
count=0
def ck(x):
 global count
 count+=1
 assert x
class E:
 def __init__(self,value=0,logs=None):self.value=F(value);self.logs={q:v for q,v in (logs or {}).items() if v};self.cache=None
 def interval(self):
  if self.cache is None:
   z=c.exact(self.value)
   for q,v in self.logs.items():z=c.add(z,c.mul(c.exact(v),c.lg(q)))
   self.cache=z
  return self.cache
 def __getitem__(self,j):return self.interval()[j]
def iv(x):return E(x)
def log(q):
 q=F(q);ck(q>0)
 n,d=q.numerator,q.denominator
 if n&(n-1)==0 and d&(d-1)==0:return E(n.bit_length()-d.bit_length())
 return E(0,{q:F(1)})
def plus(*xs):
 value=F(0);terms={}
 for x in xs:
  value+=x.value
  for q,v in x.logs.items():terms[q]=terms.get(q,F(0))+v
 return E(value,terms)
def scale(q,x):return E(F(q)*x.value,{t:F(q)*v for t,v in x.logs.items()})
def sub(a,b):return plus(a,scale(-1,b))
def le(a,b):ck(sub(b,a)[0]>=0)
def serial(a):return c.serial(a.interval())
@lru_cache(None)
def law(v):
 N=len(v)
 w=[sum(sign*(-1 if (s&x).bit_count()%2 else 1) for x,sign in enumerate(v)) for s in range(N)]
 ck(w==c.fw(v))
 p=tuple(F(z*z,N*N) for z in w);ck(sum(p)==1)
 return p
def entropy_ce(p,q):
 z=E()
 for mass,ref in zip(p,q):
  if mass:z=plus(z,scale(-mass,log(ref)))
 return z
def CE(v,q):return entropy_ce(law(tuple(v)),q)
def inf(v,j):return F(sum(x!=v[k^(1<<j)] for k,x in enumerate(v)),len(v))
def influence(v):return sum(inf(v,j) for j in range((len(v)-1).bit_length()))
def tab(a,b,r):
 return tuple(1-2*int(x% (1<<a)==0)+2*int(x==0) for x in range(1<<(a+b+r)))
def source(a,b):return tuple(1-2*int(x%(1<<a)==0) for x in range(1<<(a+b)))
def calibrate(q,m):
 ck(sum(q)==1 and 0<=m<=1)
 if m==1:return tuple([F(1)]+[F(0)]*(len(q)-1))
 ck(q[0]<1)
 z=tuple([m]+[v*(1-m)/(1-q[0]) for v in q[1:]])
 ck(sum(z)==1);return z
def model(a,b,kind):
 p=law(source(a,b));mu=F(1)-F(2,1<<a)
 if kind=='matching':return p
 w=[F((j+1)**2) if kind=='ascending' else F(100 if j==(1<<(a+b-1)) else 1) for j in range(1<<(a+b))]
 z=sum(w);return calibrate(tuple(x/z for x in w),mu*mu)
def floor(a,b,r,R):
 v=tab(a,b,r);p=law(v);n=a+b;t=F(1,1<<n);s=F(1,1<<a);e=F(2,1<<(n+r));h=e/s;mu=1-2*s
 data=c.marginal(p,n) if r==1 else tuple(sum(p[T|(U<<n)] for U in range(1<<r)) for T in range(1<<n))
 rp=tuple((1-h)*R[T]+h*mu*int(T==0)+2*e*t for T in range(1<<n))
 ck(sum(rp)==1 and all(x>0 for x in data))
 Q=tuple(rp[x% (1<<n)]*p[x]/data[x% (1<<n)] for x in range(len(p)))
 ck(sum(Q)==1 and all(Q[x]>0 for x,z in enumerate(p) if z))
 return v,Q
def erase(v,j):
 p=law(tuple(v));m=c.marginal(p,j)
 return sub(entropy_ce(p,p),entropy_ce(m,m))
def embed(R,total):return tuple(R[j] if j<len(R) else F(0) for j in range(1<<total))
def do(a0,b0,r0,kind,k,exitkind,inside):
 a,b,r=a0,b0,r0;R=model(a,b,kind);v,Q=floor(a,b,r,R);rootv=v
 rootc=CE(source(a,b),R);Ig=influence(source(a,b));If=influence(v);eroot=F(2,1<<(a+b+r))
 quota=scale(18*If,iv(1)) if kind=='matching' else plus(iv(10*If),scale(2*If/Ig,rootc))
 reach=F(1);book=iv(0);siblings=iv(0)
 for step in range(k):
  ck(a>=2)
  marg=c.marginal(Q,0);book=plus(book,scale(reach,erase(v,0)))
  off=c.restrict(v,0,1);siblings=plus(siblings,scale(reach/2,CE(off,marg)))
  R=calibrate(c.marginal(R,0),(1-F(4,1<<a))**2)
  a-=1;v,Q=floor(a,b,r,R);reach/=2
 currentc=CE(source(a,b),R);e=F(2,1<<(a+b+r));s=F(1,1<<a);mu=1-2*s;h=e/s
 ck(h<=F(1,2))
 gamma=(1-h)/(1+h/2);L=scale(-1,log(gamma))
 le(scale(4*s,L),iv(11*e))
 create=a if exitkind=='D' else a+b
 eQ=c.marginal(Q,create);ev=c.restrict(v,create,1);onv=c.restrict(v,create,0)
 Bb=erase(v,create);book=plus(book,scale(reach,Bb))
 ae,be,re=a,b-int(exitkind=='D'),r-int(exitkind=='C')
 Ron=R if exitkind=='C' else calibrate(c.marginal(R,a),mu*mu)
 _,onQ=floor(ae,be,re,Ron);onterm=scale(reach/2,CE(onv,onQ))
 ck(tuple(ev)==source(ae,be)* (1<<re))
 ck(eQ[0]>=mu*mu)
 for T in range(1<<a):
  if T:ck(eQ[T]>=gamma*R[T])
 insidej=0 if inside=='A' else ae if inside=='D' else ae+be
 qchild=c.marginal(eQ,insidej);zv=c.restrict(ev,insidej,0);ov=c.restrict(ev,insidej,1)
 Bexit=erase(ev,insidej)
 # Descendant source: marginalize ORIGINAL R, then calibrate ONCE at the final true child.
 rem=R
 if exitkind=='D':rem=c.marginal(rem,a)
 if inside in ['A','D']:rem=c.marginal(rem,insidej)
 pz=law(tuple(zv));actualmean2=pz[0]
 # All true control frequencies are empty. Data marginal carries the exact vacuum pz[0].
 rem=calibrate(rem,actualmean2)
 total=(len(zv)-1).bit_length();fresh=embed(rem,total)
 ck(sum(fresh)==1 and all(fresh[j]>0 for j,z in enumerate(pz) if z))
 newce=CE(zv,fresh);oldce=CE(zv,qchild);other=CE(ov,qchild)
 if inside=='A':
  ck(all(x==ov[0] for x in ov))
  V0=R[0]+R[1];ck(V0>0 and qchild[0]>=R[0]+gamma*R[1])
  oldconst=scale(-1,log(V0))
  le(sub(other,oldconst),scale(1-mu*mu,L))
  le(plus(Bexit,scale(F(1,2),plus(newce,oldconst))),currentc)
 else:
  ck(inf(ev,insidej)==0 and law(tuple(zv))==law(tuple(ov)))
  le(other,CE(ev,eQ))
  le(newce,currentc)
 exitledger=plus(Bexit,scale(F(1,2),plus(newce,other)))
 le(exitledger,plus(currentc,iv(F(11,2)*e)))
 # Actual creating-parent transaction uses its actual on-floor terminal, not a renewed bank.
 local=plus(Bb,scale(F(1,2),plus(CE(onv,onQ),exitledger)))
 W=plus(currentc,iv(10*e*(a+b+r)))
 le(local,plus(W,iv(F(19,4)*e)))
 book=plus(book,scale(reach/2,Bexit))
 ledger=plus(book,siblings,onterm,scale(reach/4,plus(newce,other)))
 le(ledger,sub(quota,iv(12*eroot)))
 Z=scale(reach/4,sub(newce,oldce))
 witness=None
 if Z[0]>0 and k:
  witness={'actual_zero_child':list(zv),'actual_one_child':list(ov),'true_zero_spectrum':[str(x) for x in law(tuple(zv))],'true_one_spectrum':[str(x) for x in law(tuple(ov))],'incoming_child_reference':[str(x) for x in qchild],'new_zero_reference':[str(x) for x in fresh],'unchanged_one_reference':[str(x) for x in qchild],'current_original_source':[str(x) for x in R],'old_whole_exit_reference':[str(x) for x in eQ]}
 return {'root':[a0,b0,r0,kind],'prefix_active':k,'exit':exitkind,'inside_query':inside,'root_reach_to_exit':str(reach/2),'old_query_debit_interval':serial(book),'signed_reset_interval':serial(Z),'positive_signed_reset_certified':Z[0]>0,'root_reserve_interval':serial(sub(quota,ledger)),'local_excess_interval':serial(sub(local,W)),'e_current':str(e),'both_exit_query_children_nonconstant':influence(zv)>0 and influence(ov)>0,'same_old_complementary_terminal':True,'reference_target':'direct original-source marginal, ONE final calibration','root_truth_table':list(rootv) if Z[0]>0 and k else None,'exact_positive_transaction':witness}

def domain(pilot):
 for a in ([2] if pilot else [1,2,3]):
  for b in ([1] if pilot else [0,1]):
   for r in ([2] if pilot else [1,2]):
    if b+r<2:continue
    for mode in ['matching','ascending','spiked']:
     for k in range(a):
      for e in (['D'] if b else [])+(['C'] if r>=2 else []):
       aa,bb,rr=a-k,b-int(e=='D'),r-int(e=='C')
       for j in ['A']+(['D'] if bb else [])+(['C'] if rr else []):yield a,b,r,mode,k,e,j

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();start=time.perf_counter()
 rows=[do(*x) for x in domain(args.pilot)]
 roots={tuple(x['root']) for x in rows}
 result={'status':'PASS','transactions':len(rows),'roots':len(roots),'assertions':count,'mathematical_seconds':time.perf_counter()-start,'positive_resets':sum(x['positive_signed_reset_certified'] for x in rows),'positive_after_active_prefix':sum(x['positive_signed_reset_certified'] and x['prefix_active']>0 for x in rows),'rows':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'log_helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest()}
 (RUN/'out'/('PILOT.json' if args.pilot else 'EXACT_EXIT.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 if not args.pilot:
  witness=next((x for x in rows if x['positive_signed_reset_certified'] and x['prefix_active']>0),None)
  (RUN/'out/POSITIVE_RESET.json').write_text(json.dumps(witness,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
