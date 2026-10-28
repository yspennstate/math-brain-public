from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
import exact as e
import sys,json,time,hashlib
R=Path(__file__).resolve().parents[1]
e.eta=lru_cache(None)(e.eta)
CHECKS=0
def ck(x):
 global CHECKS
 assert x
 CHECKS+=1
def overlap(a,b):
 ck(a[0]<=b[1] and b[0]<=a[1])
 ck(max(a[1]-a[0],b[1]-b[0])<e.SCALE//10**25)
def restrict(v,i,s):return [v[x] for x in range(len(v)) if ((x>>i)&1)==s]
def influence(v,i):return Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def B(v,i,tf=e.fwht):
 a=tf(v);return e.add(*(e.phi(a[j]**2,a[j|(1<<i)]**2) for j in range(len(v)) if not(j&(1<<i))))
def D(v,i,tf=e.fwht):return e.add(e.H(v,tf),e.neg(e.times(e.add(*(e.H(restrict(v,i,s),tf) for s in (0,1))),Q(1,2))))
def bent(x,m):return (-1)**sum(((x>>(2*j))&3)==3 for j in range(m//2))
def wrapper(g,m):return [g[y] if x==0 else bent(x,m) for y in range(len(g)) for x in range(1<<m)]
def case(g,m,tf=e.fwht):
 c=Q(1,1<<m);mu=Q(sum(g),len(g));gh=tf(g);f=wrapper(g,m);fh=tf(f);N=1<<m
 ck(all(x in (-1,1) for x in f));ck(sum(x*x for x in fh)==1)
 for i in range(len(g).bit_length()-1):
  beta=gh[1<<i];t=influence(g,i);bg=B(g,i,tf);bf=B(f,m+i,tf);df=D(f,m+i,tf)
  ck(abs(beta)<=t);ck(influence(f,m+i)==c*t)
  S=e.add(*(e.phi((Q(bent(s,m),1<<(m//2))+(mu-1)*c)**2,beta*beta*c*c) for s in range(N)))
  predicted=e.add(e.times(bg,c),e.neg(e.times(e.phi(mu*mu,beta*beta),c)),S)
  overlap(bf,predicted)
  js=e.add(df,e.neg(bf));ck(js[1]>=0)
  # JS <= 2*c*t nats, equivalently <=2*c*t/ln2 bits.
  ck(js[0]<=2*c*t*e.SCALE)
  if beta:
   # Lower bound S >= c beta^2 (m-2) bits for m>=4.
   ck(S[1]>=e.times(e.ln(Q(2)),c*beta*beta*(m-2))[0])
   # Review the primary source inequality without its looser final constant.
   norm=1-c+c*mu*mu
   upper=e.times(e.add((e.SCALE,e.SCALE),e.ln(1+norm/(c*beta*beta))),c*beta*beta)
   ck(S[0]<=upper[1])
  else:overlap(S,(0,0))
 return len(g).bit_length()-1
def tree(v,order):
 if not order:return Q(0)
 i=order[0];b=e.fwht(v)[1<<i];mu=Q(sum(v),len(v));children=[restrict(v,i,s) for s in (0,1)]
 mus=[Q(sum(w),len(w)) for w in children]
 ck(sum(u*u for u in mus)/2-mu*mu==b*b)
 rest=[j-(j>i) for j in order[1:]]
 return b*b+sum((tree(w,rest) for w in children),Q(0))/2
def named():
 return {'AND3':[-1 if x==0 else 1 for x in range(8)],'Maj3':[1 if x.bit_count()<=1 else -1 for x in range(8)],'parity3':[(-1)**x.bit_count() for x in range(8)],'dictator3':[(-1)**(x&1) for x in range(8)]}
def run(mode):
 t0=time.perf_counter();rows=[];queries=trees=0
 if mode in ('pilot','reproduce'):
  tf=e.direct if mode=='reproduce' else e.fwht
  for mask in range(16):queries+=case([(-1)**((mask>>x)&1) for x in range(4)],4,tf)
 elif mode=='main':
  for mask in range(256):
   g=[(-1)**((mask>>x)&1) for x in range(8)];queries+=case(g,4)
   mu=Q(sum(g),8)
   for order in permutations(range(3)):
    ck(tree(g,list(order))==1-mu*mu);trees+=1
  for mask in range(16):queries+=case([(-1)**((mask>>x)&1) for x in range(4)],6)
  for m in (6,8):
   for g in named().values():queries+=case(g,m)
 elif mode=='limits':
  for m in (4,6,8,10):
   c=Q(1,1<<m);hb=e.H([bent(x,m) for x in range(1<<m)]);hbflip=e.H([-1 if x==0 else bent(x,m) for x in range(1<<m)])
   for name,g in named().items():
    mu=Q(sum(g),len(g));var=1-mu*mu
    terminal=e.add(e.times(hb,(1+mu)/2),e.times(hbflip,(1-mu)/2))
    total=e.add(e.H(wrapper(g,m)),e.neg(terminal))
    # Fixed finite internal tree has bounded c-scaled baseline; normalized deficit tends Var(g).
    rows.append({'m':m,'g':name,'mu':str(mu),'variance':str(var),'full_actual_terminals':[e.serial(hb),e.serial(hbflip)],'complete_internal_D_over_cm':e.serial(e.times(total,1/(c*m)))})
    ck(sum((e.fwht(g)[1<<i]**2 for i in range(3)),Q(0))==0 if name=='parity3' else True)
    ck(tree(g,[0,1,2])==var)
 else:raise ValueError(mode)
 elapsed=time.perf_counter()-t0;ck(elapsed<55)
 out={'status':'PASS','mode':mode,'checks':CHECKS,'root_queries':queries,'complete_trees':trees,'elapsed_s':elapsed,'rows':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (R/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
 print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':run(sys.argv[1])
