"""A062-sparse-reference-v2: exact normalized point-reference histories."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,json,time
sys.dont_write_bytecode=True
import kernel as k
ROOT=Path(__file__).resolve().parents[1]
C=F(3,2)
LOGE_LO=F(1)/k.L2[1]

def exact(x):return k.exact(F(x))
def scale(a,c):
 c=F(c)
 return (k.floor(c*a[0]),k.ceil(c*a[1])) if c>=0 else (k.floor(c*a[1]),k.ceil(c*a[0]))
def plus(*xs):
 a=(0,0)
 for x in xs:a=k.add(a,x)
 return a
@lru_cache(None)
def integer_log(v):
 shift=max(0,v.bit_length()-64)
 if not shift:return k.log_bounds(v)
 a=v>>shift
 return (k.log_bounds(a)[0]+shift*k.SCALE,k.log_bounds(a+1)[1]+shift*k.SCALE)
@lru_cache(None)
def log(x):
 x=F(x);k.check(x>0)
 return k.sub(integer_log(x.numerator),integer_log(x.denominator))
def term(p,q):
 if not p:return (0,0)
 k.check(q>0)
 return scale(log(F(p)/q),p)
def hb(x):return plus(scale(log(x),-x) if x else (0,0),scale(log(1-x),x-1) if x!=1 else (0,0))
def bkl(p,q):return plus(term(p,q),term(1-p,1-q))
def stats(m,delta,r,eligible=True):
 if m==0:return {'m':0,'d':F(0),'I':F(0),'r':F(1),'c':F(0),'K':(0,0),'TC':(0,0),'H':(0,0),'M':(0,0)}
 d=F(1,1<<(m-1));p0=(1-d)**2;mu=1-p0;I=m*d;c=(1-r)/(1-(1-delta)**m)
 k.check(0<delta<1 and 0<=r<1 and c>0)
 if eligible:k.check(delta<=d)
 k.check(r+c*(1-(1-delta)**m)==1)
 H=plus(scale(log(p0),-p0) if p0 else (0,0),scale(log(d*d),-mu))
 M=scale(hb(d),m)
 CE=plus(scale(log(r),-p0) if p0 else (0,0),scale(log(c),-mu),scale(log(delta),-I),scale(log(1-delta),-(m*mu-I)))
 K=k.sub(CE,H);k.check(K[1]>=0);K=(max(0,K[0]),K[1])
 TC=k.sub(M,H);k.check(TC[1]>=0);TC=(max(0,TC[0]),TC[1])
 return {'m':m,'d':d,'I':I,'r':r,'c':c,'K':K,'TC':TC,'H':H,'M':M}

def step(row,delta):
 m=row['m'];d=row['d'];r=row['r'];c=row['c']
 if m==1:
  child=stats(0,delta,F(1));return child,exact(0),row['K'],F(1,2)
 q0=(1-d)**2+d*d;Rsingle=c*delta*(1-delta)**(m-1);R0=r+Rsingle
 alpha=(1-2*d)**2/(2*q0);pi=1-(1-alpha)*R0
 k.check(0<pi<1 and R0>0 and 0<=alpha<1)
 rr=alpha*R0/pi;child=stats(m-1,delta,rr)
 k.check(child['c']==c/pi)
 E=plus(scale(bkl(d*d/q0,Rsingle/R0),q0),scale(bkl(F(1,2),delta),1-q0))
 k.check(E[1]>=0);E=(max(0,E[0]),E[1]);O=bkl(F(1,2),pi)
 chain=k.sub(row['K'],plus(E,O,scale(child['K'],F(1,2))))
 k.check(chain[0]<=0<=chain[1]) # diagnostic only; exact KL chain is proved in PROOF.
 k.check(row['I']==d+child['I']/2)
 return child,O,E,pi

def history(n,choice):
 delta=F(1,1<<(n-1));r=(1-delta)**n if choice=='product' else (1-delta)**2
 row=stats(n,delta,r);rows=[row]
 while row['m']:
  child,O,E,pi=step(row,delta);row.update({'O':O,'E':E,'pi':pi});rows.append(child);row=child
 B=(0,0)
 for row in reversed(rows):
  T=k.sub(row['TC'],row['K']);obstacle=k.pos(T)
  B=obstacle if row['m']==0 else (max(obstacle[0],k.sub(scale(B,F(1,2)),row['E'])[0]),max(obstacle[1],k.sub(scale(B,F(1,2)),row['E'])[1]))
  row['B']=B
  k.check(B[0]>=0 and F(B[1],k.SCALE)<=LOGE_LO*row['I'])
  if row['m']>=3:
   m=row['m'];d=row['d'];q0=(1-d)**m;p0=(1-d)**2;bound=bkl(p0,q0)
   # The zero-atom choice saturates the projection bound when delta=d at root.
   k.check(T[0]<=bound[1])
   k.check(F(bound[1],k.SCALE)<LOGE_LO*row['I'])
  if row['m']<=2:k.check(row['TC']==(0,0))
 if choice=='source-empty' and n>=3:k.check(rows[0]['B'][0]>0)
 return rows

def ref_atoms(m,delta,row):
 return {s:(row['r'] if s==0 else row['c']*delta**s.bit_count()*(1-delta)**(m-s.bit_count())) for s in range(1<<m)}
def kl_atoms(p,R):return plus(*(term(v,R[s]) for s,v in p.items() if v))
def physical_raw(n,choice,rows):
 delta=F(1,1<<(n-1));queries=0
 for row in rows:
  m=row['m']
  if not m:continue
  N=1<<m;truth=bytes(int(x==0) for x in range(N));w=k.walsh(truth);p={s:F(v*v,N*N) for s,v in enumerate(w)};R=ref_atoms(m,delta,row)
  k.check(sum(p.values())==sum(R.values())==1)
  Kraw=kl_atoms(p,R);k.check(max(Kraw[0],row['K'][0])<=min(Kraw[1],row['K'][1]))
  for i in range(m):
   queries+=1;b=1<<i
   erase=lambda s:(s&(b-1))|((s>>(i+1))<<i)
   q={s:F(0) for s in range(1<<(m-1))};Qr=dict(q)
   for s,v in p.items():q[erase(s)]+=v;Qr[erase(s)]+=R[s]
   Et=k.sub(Kraw,kl_atoms(q,Qr));k.check(max(Et[0],row['E'][0])<=min(Et[1],row['E'][1]))
   a0,a1=k.children(truth,i);k.check(F(sum(x!=y for x,y in zip(a0,a1)),len(a0))==row['d'])
   predictions=[]
   for bchild,tt in enumerate((a0,a1)):
    ww=k.walsh(tt);pc={s:F(v*v,len(tt)**2) for s,v in enumerate(ww)}
    unnorm={s:Qr[s]*pc[s]/(2*q[s]) for s in q};pi=sum(unnorm.values());predictions.append(pi)
    rr={s:v/pi for s,v in unnorm.items()};k.check(sum(rr.values())==1)
    if bchild==0 and m>=2:
     expected=ref_atoms(m-1,delta,rows[n-m+1]);k.check(rr==expected and pi==row['pi'])
    else:k.check(rr[0]==1 and all(v==0 for s,v in rr.items() if s))
   k.check(sum(predictions)==1)
 return queries

def serial(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {s:serial(t) for s,t in v.items()}
 if isinstance(v,(list,tuple)):return [serial(t) for t in v]
 return v
def main():
 start=time.monotonic();pilot='--pilot' in sys.argv;ns=[2,3,4] if pilot else list(range(2,21));roots=[];rawqueries=0;histories=0
 for n in ns:
  for choice in ['product','source-empty']:
   rows=history(n,choice);histories+=len(rows)
   if n<=7:rawqueries+=physical_raw(n,choice,rows)
   roots.append({'n':n,'reference':choice,'rows':rows})
   (ROOT/'out'/('PILOT_PARTIAL.json' if pilot else 'PARTIAL.json')).write_text(json.dumps(serial({'roots':roots,'assertions':k.ASSERTIONS,'seconds':time.monotonic()-start})),encoding='utf-8')
   k.check(time.monotonic()-start<55)
 k.check(3**12>2**19)
 # Essential reference-shape hypothesis: R=p8 has delta=1/2>d8 and K=0.
 n=8;d=F(1,128);adverse=stats(n,F(1,2),(1-d)**2,eligible=False)
 actual=ref_atoms(n,F(1,2),adverse)
 k.check(actual=={s:((1-d)**2 if s==0 else d*d) for s in range(1<<n)})
 k.check(adverse['K'][0]<=0<=adverse['K'][1]);k.check(F(adverse['TC'][0],k.SCALE)>C*adverse['I'])
 adverse['K_exact_by_rational_law_identity']='0'
 out={'helper':'A062-sparse-reference-v2','scale':str(k.SCALE),'roots':len(roots),'histories':histories,'raw_query_candidates':rawqueries,'assertions':k.ASSERTIONS,'seconds':time.monotonic()-start,'cases':roots,'adversarial':adverse,'proof_rung':'finite exact certificates supporting written all-dimensional proof; no independent acceptance yet'}
 (ROOT/'out'/('PILOT.json' if pilot else 'EXACT.json')).write_text(json.dumps(serial(out),indent=2)+'\n',encoding='utf-8')
 print(json.dumps({s:out[s] for s in ['roots','histories','raw_query_candidates','assertions','seconds']}))

if __name__=='__main__':main()
