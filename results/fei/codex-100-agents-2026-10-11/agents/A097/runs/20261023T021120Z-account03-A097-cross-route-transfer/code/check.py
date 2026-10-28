"""Independent direct-character verifier for original-source canonical reset returns."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';OUT.mkdir(exist_ok=True)
START=time.perf_counter();COUNT=0;FIRST_POS=0;RETURN_NEG=0;RETURN_ZERO=0;OLD_NONCONST=0;WITNESS=None
def dump(name,obj):(OUT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def ck(v):
 global COUNT
 COUNT+=1
 if not v:raise AssertionError(COUNT)
 if time.perf_counter()-START>55:raise TimeoutError('55s frozen cap')
def ln(q):
 z=(q-1)/(q+1);term=z;val=F(0)
 for k in range(20):val+=2*term/(2*k+1);term*=z*z
 return val,val+2*term/(41*(1-z*z))
LN2=ln(F(2))
@lru_cache(None)
def lg(q):
 q=F(q);assert q>0
 k=q.numerator.bit_length()-q.denominator.bit_length();z=q/F(2)**k
 if z<1:k-=1;z*=2
 lo,hi=ln(z)
 return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def add(*xx):return sum((x[0] for x in xx),F(0)),sum((x[1] for x in xx),F(0))
def mul(a,x):return (a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0])
def sub(x,y):return add(x,mul(-1,y))
def CE(p,q):
 for a,b in zip(p,q):
  if a:ck(b>0)
 return add(*(mul(-a,lg(b)) for a,b in zip(p,q) if a))
@lru_cache(None)
def law(v):
 N=len(v)
 return tuple(F(sum(y*(-1 if (x&T).bit_count()%2 else 1) for x,y in enumerate(v)),N)**2 for T in range(N))
def marginal(p,j):
 out=[F(0)]*(len(p)//2)
 for x,u in enumerate(p):out[(x&((1<<j)-1))|((x>>(j+1))<<j)]+=u
 return tuple(out)
def restrict(v,j,b):return tuple(v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(v)//2))
def cal(p,z):
 if z==1:return (F(1),)+(F(0),)*(len(p)-1)
 assert p[0]<1
 return (z,)+tuple((1-z)*x/(1-p[0]) for x in p[1:])
def B(p,j):return sub(CE(p,p),CE(marginal(p,j),marginal(p,j)))

def tree(v,D,S,Q,path,kind,seen,m):
 global FIRST_POS,RETURN_NEG,RETURN_ZERO,OLD_NONCONST,WITNESS
 p=law(v);depth=len(path);n=len(v).bit_length()-1
 reset=(kind==0 and depth<=2) or (kind==1 and ((depth==1 and path[0]==0) or (depth==2 and path[-1]==0))) or (kind==2 and ((depth==1 and path[0]==1) or depth==2))
 if reset:
  fresh=cal(S,p[0]);ck(sum(fresh)==1)
  if seen:
   current=cal(Q,p[0]);ck(fresh==current)
   a,b=CE(p,fresh),CE(p,Q)
   if fresh==Q:RETURN_ZERO+=1
   else:ck(a[1]<=b[0]);RETURN_NEG+=1
   # Independent exact per-atom normalization formula, ghosts included.
   if p[0]<1:
    for j in range(1,len(p)):ck(fresh[j]*(1-Q[0])==(1-p[0])*Q[j])
  else:
   old,new=CE(p,Q),CE(p,fresh)
   if new[0]>old[1]:
    FIRST_POS+=1
    if WITNESS is None:WITNESS={'function':list(v),'path':list(path),'old_reference':list(map(str,Q)),'fixed_original_source_marginal':list(map(str,S)),'new_reference':list(map(str,fresh)),'positive_first_reset_lower':str(new[0]-old[1])}
  Q=fresh;seen=True
 stop=n==0 or (kind!=0 and depth>=2)
 if stop:
  if not seen and p[0]<1:OLD_NONCONST+=1
  return CE(p,Q)
 j=0 if kind!=2 else n-1
 childs=[restrict(v,j,b) for b in (0,1)]
 pp=[law(z) for z in childs];mp=marginal(p,j)
 ck(all((x+y)/2==z for x,y,z in zip(pp[0],pp[1],mp)))
 results=[tree(c,marginal(D,j),marginal(S,j),marginal(Q,j),path+(b,),kind,seen,m) for b,c in enumerate(childs)]
 return add(B(p,j),mul(F(1,2),results[0]),mul(F(1,2),results[1]))

def grid():
 cases=0
 for a in range(9):
  for b in range(9-a):
   for c in range(9-a-b):
    p=tuple(F(x,8) for x in (a,b,c,8-a-b-c));mp=marginal(p,0)
    for z in map(F,[0,F(1,4),F(1,2),F(3,4),1]):
     if p[0]==1 and z!=1:continue
     q=cal(p,z);mq=marginal(q,0)
     for w in map(F,[0,F(1,4),F(1,2),F(3,4),1]):
      if (z==1 or mp[0]==1 or mq[0]==1) and w!=1:continue
      ck(cal(mq,w)==cal(mp,w));cases+=1
 return cases

def main():
 pilot='--pilot' in sys.argv;n=2 if pilot else 3
 dump('FROZEN_PILOT.json' if pilot else 'FROZEN_SPEC.json',{'helper':'check.py v1; independent direct character sums','family':'EVERY labelled Boolean truth table on n bits; actual physical adaptive query trees','domain':{'n':n,'source_profiles':['exact','half-mass increasing','quarter-mass spiked'],'source_completion':['vacuum','uniform'],'gamma':['1/2','1/4'],'policies':3},'roots':(1<<(1<<n))*12,'policies':(1<<(1<<n))*36,'additional_grid':'all165 laws on4 atoms with denominator8;5 calibration targets each level, admissible endpoints only','symmetry':'none','arithmetic':'Fraction character spectra, exact normalized laws,20-term atanh rational log bounds with rigorous tail','memory_estimate_mb':120,'max_runtime_seconds':55})
 roots=policies=0
 for table in range(1<<(1<<n)):
  v=tuple(1 if (table>>x)&1 else -1 for x in range(1<<n));p=law(v);m=p[0];N=len(p)
  for mode in range(3):
   if mode==0:D=p
   else:
    weights=[F((i+1) if mode==1 else (N*N if i==N-1 else 1)) for i in range(1,N)];den=sum(weights);delta=F(1,2) if mode==1 else F(1,4)
    D=(m,)+tuple(delta*(1-m)*w/den for w in weights)
   for completion in range(2):
    spare=1-sum(D)
    S=tuple(d+spare*(int(i==0) if completion==0 else F(1,N)) for i,d in enumerate(D))
    ck(sum(S)==1 and all(s>=d for s,d in zip(S,D)))
    for gamma in [F(1,2),F(1,4)]:
     Q=[m]+[gamma*d for d in D[1:]];destination=next((i for i in range(1,N) if p[i]==0),N-1);Q[destination]+=1-sum(Q);Q=tuple(Q)
     ck(sum(Q)==1 and Q[0]>=m);ck(all(q>=gamma*d for q,d in zip(Q[1:],D[1:])))
     c=CE(p,D);bound=add(c,mul(-(1-m*m),lg(gamma)))
     roots+=1
     for kind in range(3):
      result=tree(v,D,S,Q,(),kind,False,m);ck(result[1]<=bound[0]);policies+=1
 gridcases=grid()
 # Scope falsifier: changing the nonempty conditional law can make a return positive.
 parity=tuple(-1 if x.bit_count()%2 else 1 for x in range(8));cp=law(restrict(parity,0,0));sib=law(restrict(parity,0,1))
 source=(F(0),)+(F(1,7),)*7;fresh=cal(marginal(source,0),cp[0]);other=(F(0),F(1,4),F(1,4),F(1,2))
 ck(cp[0]==sib[0]==0);ck(cp[3]==1);ck(sum(other)==1)
 gap=sub(CE(cp,fresh),CE(cp,other));ck(gap[0]>F(1,2))
 result={'status':'PASS','pilot':pilot,'Boolean_tables':1<<(1<<n),'source_floor_instances':roots,'adaptive_reset_policies':policies,'commutation_grid_cases':gridcases,'checks':COUNT,'positive_FIRST_resets':FIRST_POS,'strictly_negative_RETURN_resets':RETURN_NEG,'exactly_unchanged_RETURN_resets':RETURN_ZERO,'nonconstant_never_reset_old_terminals':OLD_NONCONST,'changed_nonempty_profile_return_gap_gt':'1/2 bit, actual parity3 query, both siblings nonconstant','runtime_seconds':time.perf_counter()-START}
 dump('PILOT.json' if pilot else 'VALIDATION.json',result)
 if WITNESS:dump('POSITIVE_FIRST_RESET_WITNESS.json',WITNESS)
 print(json.dumps(result))
if __name__=='__main__':main()
