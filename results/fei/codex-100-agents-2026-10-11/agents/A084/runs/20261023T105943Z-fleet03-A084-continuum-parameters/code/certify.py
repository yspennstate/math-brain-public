"""Factored actual seed, independent coefficient groups, and analytic-family controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json,time,sys
import seed_engine as e
from arithmetic import Q,log2,scale,plus
RUN=Path(__file__).resolve().parents[1]
CHECKS=0
def ck(v):
 global CHECKS
 assert v
 CHECKS+=1
def save(n,x): (RUN/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def const(x):
 x=F(x); q=x*Q
 return (q.numerator//q.denominator,-((-q.numerator)//q.denominator))
def times(a,x):
 x=F(x)
 return scale(a,x) if x>=0 else tuple(-v for v in scale(a,-x)[::-1])
def eta(q): return times(log2(q),-q) if q else (0,0)
def ep(p): return e.pack(p)
def activation(delta,mu,H):
 if not delta:return (0,0)
 a=1-mu;v=1-mu*mu;L=log2(1/delta)
 return plus(eta((1-delta*a)**2),plus(times(plus(eta(a*a),times(L,2*a*a)),delta-delta*delta),times(plus(e.ev(H),plus(times(eta(mu*mu),-1),times(L,2*v))),delta)))

def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv
 # Small direct sign seed before composing anything.
 t=tuple(-1 if x==0 else 1 for x in range(4));p=e.core(t)
 ck(p['H']=={2:F(2)} and p['I']==1)
 g=tuple(-1 if x in {0,1,2} else 1 for x in range(64))
 W=[sum(y*(-1 if (b&x).bit_count()%2 else 1) for x,y in enumerate(g)) for b in range(64)]
 ck(sum(w*w for w in W)==64*64)
 for x,y in enumerate(g):ck(sum(w*(-1 if (b&x).bit_count()%2 else 1) for b,w in enumerate(W))==64*y)
 mu=F(W[0],64)
 groups=Counter((F(W[b],64),b.bit_count()) for b in range(1,64))
 h=tuple(-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64))
 k=tuple(-h[4*z] for z in range(16))
 outer=[F(sum(y*(-1 if (b&x).bit_count()%2 else 1) for x,y in enumerate(k)),16) for b in range(16)]
 H={};I=F(0);norm=F(0);count=0;categories=[]
 for B in range(16):
  m=B.bit_count();L=sum(outer[T]*mu**(T.bit_count()-m) for T in range(16) if T&B==B)
  for choice in product(list(groups),repeat=m):
   multiplicity=1;coef=L;degree=0;logs=e.mul(e.lp(abs(L)),2) if L else {}
   for c,j in choice:
    multiplicity*=groups[(c,j)];coef*=c;degree+=j
    if c:logs=e.add(logs,e.mul(e.lp(abs(c)),2))
   count+=multiplicity
   mass=multiplicity*coef*coef;norm+=mass;I+=mass*degree
   if mass:H=e.add(H,e.mul(logs,-mass))
   categories.append({'B':B,'coefficient':str(coef),'multiplicity':multiplicity,'degree':degree})
 ck(count==2**24 and norm==1)
 old=e.full((e.G,)*4)
 ck(H==old['H'] and I==old['I'])
 mean=sum(y*e.prod((1-mu)/2 if x>>j&1 else (1+mu)/2 for j in range(4)) for x,y in enumerate(k))
 ck(mean==sum(outer[T]*mu**T.bit_count() for T in range(16)))
 A=e.add(H,{2:-4*I});ck(e.cmp(A,{2:F(7,256)})>0 and I<=24)
 Kmax=F(4097,1024);Amin=e.add(H,{2:-Kmax*I})
 ck(e.cmp(Amin,{2:F(1,256)})>0)
 ck(4*7-(24+3)==1)
 save('SEED_CERTIFICATE.json',{'H':ep(H),'I':str(I),'mean':str(mean),'A4':ep(A),'A4_interval':e.ev(A),'rate_interval':['4',str(Kmax)],'minimum_deficit':ep(Amin),'minimum_deficit_interval':e.ev(Amin),'strict_floor':'1/256','grouped_categories':len(categories),'integer_atom_count':count,'parity_bits':7,'checks_so_far':CHECKS+e.CHECKS})
 if pilot:
  result={'pilot':'PASS','assertions':CHECKS+e.CHECKS,'runtime_seconds':time.perf_counter()-start};save('PILOT.json',result);print(json.dumps(result));return
 rows=[]
 for d in range(17):
  delta=F(1,2**d);hd=activation(delta,mean,H)
  ck(hd[0]>=0 and hd[1]<=27*Q)
  if d==0:ck(hd[0]<=e.ev(H)[0]<=e.ev(H)[1]<=hd[1])
  if d>=3:
   upper=4*delta*(24+2*d+2);ck(hd[1]<const(upper)[0])
  for K in [F(4),F(8193,2048),Kmax]:
   If=7+delta*(I+d*(1-mean));slack=plus(const(K*If),times(hd,-1))
   ck(slack[0]>=Q)
   ak=e.add(H,{2:-K*I});ck(e.cmp(ak,{2:F(1,256)})>0)
   rows.append({'d':d,'K':str(K),'H_interval':hd,'physical_I':str(If),'slack_interval':slack,'rare_seed_deficit':ep(ak),'selector_allocator_increment':'0'})
 # Fixed rational bias faces control the analytic profile; not a grid proof.
 faces=[]
 for delta in [F(0),F(1,256),F(1,8),F(1,4)]:
  hd=activation(delta,mean,H);ck(0<=hd[0]<=hd[1]<=27*Q)
  a=1-mean;v=1-mean*mean
  ck((1-delta*a)**2+(delta-delta*delta)*a*a+delta*v==1)
  faces.append({'delta':str(delta),'entropy_interval':hd,'physical_only_if_dyadic':True,'zero_reach_capital':0 if not delta else 'positive-arrival obligation'})
 # Explicit51-bit account witness from the analytic, not searched, family.
 d=20;upper=F(4*(24+2*d+2),2**d);ck(upper<F(1,256))
 save('FAMILY_CONTROLS.json',rows);save('BIAS_FACES.json',faces)
 save('EXPLICIT_WITNESS.json',{'d':20,'physical_bits':51,'rate_interval':['4',str(Kmax)],'root_hull_upper':str(upper),'robust_capital_strict_lower':'1/256','bad_path_reach':str(F(1,2**20)),'root_hull_strictly_insufficient':True,'FEI_counterexample':False})
 result={'main':'PASS','assertions':CHECKS+e.CHECKS,'guard_rate_controls':len(rows),'bias_faces':len(faces),'grouped_categories':len(categories),'runtime_seconds':time.perf_counter()-start,'all_d_and_real_rates':'PROOF.md analytic argument; finite controls are not extrapolated'}
 ck(time.perf_counter()-start<55);save('VALIDATION.json',result);print(json.dumps(result))
if __name__=='__main__':main()
