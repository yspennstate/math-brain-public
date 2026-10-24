import lib as L
from lib import Q,add
from pathlib import Path
from functools import lru_cache
import time,json,itertools
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();assertions=0
def ck(b):
 global assertions
 assertions+=1;assert b,assertions;assert time.perf_counter()-start<58,'Frozen watchdog'
def lg(x):return add((1,L.factors(x.numerator)),(-1,L.factors(x.denominator)))
@lru_cache(None)
def ln_interval(x):
 z=(x-1)/(x+1);z2=z*z;t=z;s=Q(0)
 for j in range(40):s+=t/Q(2*j+1);t*=z2
 s*=2;tail=2*abs(t)/(81*(1-z2))
 return s-tail,s+tail
LN2=ln_interval(Q(2))
@lru_cache(None)
def log_interval(x):
 assert x>0;k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 a,b=ln_interval(x)
 return Q(k)+a/LN2[1],Q(k)+b/LN2[0]
def bounds(expr):
 lo=hi=Q(0)
 for prime,c in expr.items():
  a,b=log_interval(Q(prime))
  lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def scale_bounds(c,iv):return (c*iv[0],c*iv[1]) if c>=0 else (c*iv[1],c*iv[0])
def sum_bounds(*ivs):return sum((v[0] for v in ivs),Q(0)),sum((v[1] for v in ivs),Q(0))
def eta_bounds(x):return (Q(0),Q(0)) if not x else scale_bounds(-x,log_interval(x))
def phi_bounds(a,b):return sum_bounds(scale_bounds(-1,eta_bounds(a+b)),eta_bounds(a),eta_bounds(b))
@lru_cache(None)
def p(t):return tuple(x*x for x in L.fw(t))
@lru_cache(None)
def H(t):return L.entropy(p(t))
def inf(t,i):return L.inf(p(t),i)
def I(t):return sum((inf(t,i) for i in range((len(t)-1).bit_length())),Q(0))
def sl(t,i,s):return tuple(t[(b&((1<<i)-1))|((s<0)<<i)|((b>>i)<<(i+1))] for b in range(len(t)//2))
def down(prob,i):return add(*[(prob[t|(1<<i)],lg((prob[t]+prob[t|(1<<i)])/prob[t|(1<<i)])) for t in range(len(prob)) if not t&(1<<i) and prob[t|(1<<i)]])
rows=0
for n in [1,2,3]:
 for table in range(1<<(1<<n)):
  t=tuple(1 if table&(1<<b) else -1 for b in range(1<<n))
  for i in range(n):
   delta=inf(t,i);B=L.edge(p(t),i);M=down(p(t),i);Cup=add((1,B),(-1,M))
   ck(delta==Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)))
   children=[sl(t,i,s) for s in [1,-1]]
   hchild=add(*[(Q(1,2),H(c)) for c in children]);ichild=sum((I(c)/2 for c in children),Q(0))
   JS=add((1,H(t)),(-1,hchild),(-1,B))
   ck(I(t)-ichild==delta)
   ck(add((1,M),(1,Cup))==B)
   lo,hi=bounds(Cup);ck(lo>=0 or Cup=={});ck(hi<=delta/LN2[0])
   for K in [2,4,5]:
    lhs=add((K*ichild,{2:Q(1)}),(-1,hchild),(-1,B),(-delta,{2:Q(1)}))
    rhs=add((K*I(t)-(K+1)*delta,{2:Q(1)}),(-1,H(t)),(1,JS))
    ck(lhs==rhs)
   rows+=1
point=[]
for d in range(1,8):
 delta=Q(1,1<<d);b=tuple([1]+[-1]*((1<<d)-1));g=tuple(b[y] if s==0 else -1 for y in range(1<<d) for s in range(2))
 Qbank=L.edge(p(g),0);E0=add((-1,L.xlog((1-2*delta)**2)))
 Hformula=add((1,E0),(8*delta*(1-delta)*(d-1),{2:Q(1)}))
 S4=add((4*d*delta,{2:Q(1)}),(-Q(1,2),H(b)))
 Qformula=add((1,L.phi((1-delta)**2,delta**2)),(2*delta*(1-delta),{2:Q(1)}))
 ck(H(b)==Hformula);ck(Qbank==Qformula);ck(I(b)==2*d*delta)
 ck(I(b)==sum((Q(sum(b[x]!=b[x^(1<<i)] for x in range(len(b))),len(b)) for i in range(d)),Q(0)))
 ck(bounds(S4)[0]>=0 or S4=={})
 A0lo=2/LN2[1]-2
 deficit=add((1,Qbank),(-1,S4))
 ck(bounds(deficit)[1]<A0lo*delta)
 point.append({'d':d,'delta':str(delta),'retained_bank_prime_log':{str(k):str(v) for k,v in Qbank.items()},'terminal_surplus_prime_log':{str(k):str(v) for k,v in S4.items()},'certified_Q_minus_S4_lt_A0_delta':True})
 (ROOT/'out/POINT_CHECKPOINT.json').write_text(json.dumps(point,indent=2)+'\n',encoding='utf-8')
symbolic=[]
for d in [2,4,8,16,32,64]:
 delta=Q(1,1<<d)
 Qiv=sum_bounds(phi_bounds((1-delta)**2,delta**2),(2*delta*(1-delta),)*2)
 S4iv=sum_bounds((4*delta+4*(d-1)*delta**2,)*2,scale_bounds(-Q(1,2),eta_bounds((1-2*delta)**2)))
 shortage=(Qiv[0]-S4iv[1],Qiv[1]-S4iv[0])
 ck(shortage[1]<(2/LN2[1]-2)*delta)
 full=(shortage[0]+delta,shortage[1]+delta)
 if d>=8:ck(full[0]>0)
 den=1<<120;a=shortage[0]/delta;b=shortage[1]/delta
 rounded=[Q((a*den).__floor__(),den),Q((b*den).__ceil__(),den)]
 ck(rounded[0]<=a and b<=rounded[1])
 symbolic.append({'d':d,'Q_minus_S4_over_delta_interval':[str(x) for x in rounded],'outward_denominator':'2^120','full_bank_positive_shortage':d>=8})
def erase(t,labels,order):
 if not order:return {}
 i=labels.index(order[0]);remain=labels[:i]+labels[i+1:]
 return add((1,L.edge(p(t),i)),*[(Q(1,2),erase(sl(t,i,s),remain,order[1:])) for s in [1,-1]])
h=tuple(L.majority(3,[]))
for order in itertools.permutations(range(3)):ck(erase(h,(0,1,2),order)=={2:Q(1)})
save=lambda name,obj:(ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
save('SYMBOLIC_BANKS.json',symbolic)
out={'status':'PASS','helper':'A003-retained-point-bank-v1','assertions':assertions,'labelled_seeds':276,'distinguished_rows':rows,'point_spectra':len(point),'symbolic_banks':len(symbolic),'encoder_orders':6,'runtime_seconds':time.perf_counter()-start,'arithmetic':'integer FWHT; Fraction; exact prime-log identities; 40-term rational atanh intervals'}
save('VALIDATION.json',out);print(json.dumps(out))
