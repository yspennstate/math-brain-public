from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,time,math
BASE=Path(__file__).resolve().parent.parent
START=time.monotonic();COUNT=0
def ck(x):
 global COUNT
 COUNT+=1;assert x,COUNT;assert time.monotonic()-START<60
S=1<<160
def iv(x):
 x=F(x)*S;return x.numerator//x.denominator,-((-x.numerator)//x.denominator)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,q):
 q=F(q);x,y=(a[0]*q,a[1]*q) if q>=0 else (a[1]*q,a[0]*q)
 return x.numerator//x.denominator,-((-y.numerator)//y.denominator)
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v)//S,-((-max(v))//S)
def series(q):
 z=iv((q-1)/(q+1));z2=mul(z,z);power=z;out=(0,0)
 for j in range(40):out=add(out,scale(power,F(2,2*j+1)));power=mul(power,z2)
 # Range-reduced z in [0,1/3], tail after j39 <= 2*(1/3)^81/(81*(1-1/9)).
 tail=iv(F(2,3**81)*F(9,81*8))[1]
 return out[0],out[1]+tail
LN2=series(F(2))
@lru_cache(maxsize=None)
def log(q):
 q=F(q);assert q>0;e=0
 if q==1:return 0,0
 while q>=2:q/=2;e+=1
 while q<1:q*=2;e-=1
 a=add(series(q),scale(LN2,e))
 vals=[F(x*S,y) for x in a for y in LN2]
 return min(vals).numerator//min(vals).denominator,-((-max(vals).numerator)//max(vals).denominator)
def sm(items):
 o=(0,0)
 for x in items:o=add(o,x)
 return o
def ent(p):return sm(scale(log(q),-q) for q in p if q)
def kl(p,q):return sm(scale(log(a/b),a) for a,b in zip(p,q) if a)
def encode(a):return [str(F(a[0],S)),str(F(a[1],S))]
def diag(a):return float(F(a[0]+a[1],2*S))
def law(tab):
 a=list(tab);step=1
 while step<len(a):
  for i in range(0,len(a),2*step):
   for j in range(step):u,v=a[i+j],a[i+j+step];a[i+j],a[i+j+step]=u+v,u-v
  step*=2
 return [F(x*x,len(tab)**2) for x in a]
def restrict(tab,i,y):return [tab[(t&((1<<i)-1))|(y<<i)|((t>>i)<<(i+1))] for t in range(len(tab)//2)]
def marg(p):return [sum(v for s,v in enumerate(p) if s>>i&1) for i in range((len(p)-1).bit_length())]
def prodlaw(d):return [math.prod(v if s>>j&1 else 1-v for j,v in enumerate(d)) for s in range(1<<len(d))]
def erase(p,i):return [p[s]+p[s|(1<<i)] for s in range(len(p)) if not s>>i&1]
def info(tab):
 p=law(tab);d=marg(p);H=ent(p);TC=sub(sm(ent([v,1-v]) for v in d),H)
 ck(sum(p)==1)
 for i,v in enumerate(d):ck(v==F(sum(tab[x]!=tab[x^(1<<i)] for x in range(len(tab))),len(tab)))
 return p,d,H,TC,sub(iv(4*sum(d)),H)
def step(tab,Q,coords,i):
 j=coords.index(i);P=law(tab);T=erase(P,j);QT=erase(Q,j)
 tabs=[restrict(tab,j,y) for y in [0,1]];ps=[law(t) for t in tabs]
 ck(T==[(a+b)/2 for a,b in zip(*ps)])
 k=[[ps[y][s]/(2*T[s]) if T[s] else F(1,2) for s in range(len(T))] for y in [0,1]]
 out=[sum(q*ky for q,ky in zip(QT,k[y])) for y in [0,1]]
 refs=[[q*ky/out[y] for q,ky in zip(QT,k[y])] for y in [0,1]]
 ck(sum(out)==1)
 for y in [0,1]:
  ck(sum(refs[y])==1)
  for s in range(len(T)):
   if ps[y][s]:
    # Exact likelihood factorization; no interval overlap used as equality proof.
    ck((ps[y][s]/2)/(QT[s]*k[y][s])==F(1,2)/out[y]*(ps[y][s]/refs[y][s]))
 for s in range(len(P)):
  if P[s]:
   small=(s&((1<<j)-1))|((s>>(j+1))<<j)
   ck(P[s]/Q[s]==T[small]/QT[small]*((P[s]/T[small])/(Q[s]/QT[small])))
 E=sub(kl(P,Q),kl(T,QT));O=kl([F(1,2)]*2,out)
 return [(tabs[y],refs[y],[c for c in coords if c!=i]) for y in [0,1]],E,O,sum(1 for q in T if not q)
core=[1 if 91>>j&1 else -1 for j in range(8)]
tab=[-1 if not(t&1) and t&2 else (core[t>>3] if t&1 and t&4 else 1) for t in range(64)]
P,d,H,TC,surplus=info(tab);v=1-P[0];r=[x/v for x in d]
def polynomial(c):return 1-c-math.prod(1-c*x for x in r)
lo,hi=F(0),F(1)
for _ in range(48):
 mid=(lo+hi)/2
 if polynomial(mid)>0:lo=mid
 else:hi=mid
ck(lo>0 and polynomial(lo)>0 and polynomial(hi)<0)
c=(lo+hi)/2;theta=[c*x for x in r];raw=prodlaw(theta);Z=1-raw[0]
Q=[P[0]]+[v*x/Z for x in raw[1:]];ck(sum(Q)==1)
# Certified canonical-reference approximation, including actual normalization.
eps=F(1,2**36);atom_brackets=[]
for s,q in enumerate(Q):
 if s==0:a=b=q
 else:
  a=b=v
  for j,x in enumerate(r):
   al,bu=(lo*x,hi*x) if s>>j&1 else (1-hi*x,1-lo*x)
   a*=al;b*=bu
  a/=hi;b/=lo
 ck(log(a/q)[0]>-eps*S and log(b/q)[1]<eps*S)
 atom_brackets.append([str(a),str(b)])
A=kl(P,Q)
first,E0,O0,rows=step(tab,Q,list(range(6)),1)
front=[];E=E0;O=O0
for t,q,coords in first:
 children,e,o,rr=step(t,q,coords,4) # original z1
 front+=children;E=add(E,scale(e,F(1,2)));O=add(O,scale(o,F(1,2)));rows+=rr
def account(leaves,E,O):
 fs=[info(t) for t,q,c in leaves];weight=F(1,len(leaves))
 K=sm(scale(kl(f[0],q),weight) for f,(t,q,c) in zip(fs,leaves))
 TCend=sm(scale(f[3],weight) for f in fs);Hend=sm(scale(f[2],weight) for f in fs)
 bank=sm(scale(f[4],weight) for f in fs);Iend=sum(sum(f[1])*weight for f in fs)
 D=sub(add(O,TCend),A);sigma=sub(TCend,K)
 # Analytic identities supported by exact per-atom factorization above.
 ck(sub(sub(sub(A,E),O),K)[0]<=0<=sub(sub(sub(A,E),O),K)[1])
 cond=[];quot=[]
 for f,(t,q,coords) in zip(fs,leaves):
  actual=f[0];R=prodlaw(f[1]);bits=[i for i,c in enumerate(coords) if c in [0,2]]
  def quotient(p):
   out=[F(0)]*(1<<len(bits))
   for s,x in enumerate(p):out[sum(1<<j for j,b in enumerate(bits) if s>>b&1)]+=x
   return out
  qsig=sub(kl(quotient(actual),quotient(R)),kl(quotient(actual),quotient(q)))
  full=sub(f[3],kl(actual,q));quot.append(scale(qsig,weight));cond.append(scale(sub(full,qsig),weight))
 return {'D':encode(D),'D_display':diag(D),'sigma':encode(sigma),'conditional_sigma':encode(sm(cond)),'quotient_sigma':encode(sm(quot)),'E':encode(E),'O':encode(O),'K_terminal':encode(K),'TC_terminal':encode(TCend),'H_terminal':encode(Hend),'I_terminal':str(Iend),'S4_terminal':encode(bank),'terminals':[{'coords':coords,'H':encode(f[2]),'I':str(sum(f[1])),'S4':encode(f[4]),'reference_mass_empty':str(q[0])} for f,(t,q,coords) in zip(fs,leaves)]}
baseline=account(front,E,O)
ck(F(baseline['conditional_sigma'][0])>F(1,4)+4*eps)
ck(F(baseline['D'][1])+2*eps<F(-19,100))
policies=[]
for choices in product([3,5],repeat=4):
 leaves=[];En=E;On=O;nr=rows
 for (t,q,coords),i in zip(front,choices):
  ch,e,o,rr=step(t,q,coords,i);leaves+=ch;En=add(En,scale(e,F(1,4)));On=add(On,scale(o,F(1,4)));nr+=rr
 result=account(leaves,En,On);result['policy']=choices;result['source_zero_rows']=nr
 ck(F(result['D'][1])+2*eps<F(-7,10))
 ck(F(result['conditional_sigma'][1])+4*eps<F(-1,10))
 ck(F(result['quotient_sigma'][0])-4*eps>F(0))
 ck(all(F(t['S4'][0])>=0 for t in result['terminals']))
 ck(F(result['S4_terminal'][0])>F(9,5))
 result['canonical_signs_certified']={'D_below_minus_7_over_10':True,'conditional_sigma_below_minus_1_over_10':True,'quotient_sigma_positive':True,'all_actual_S4_nonnegative':True,'no_terminal_surplus_withdrawal':True}
 policies.append(result)
summary={'status':'PASS','assertions':COUNT,'runtime_seconds':time.monotonic()-START,'core_code':91,'canonical_root_bracket':[str(lo),str(hi)],'rational_reference_c':str(c),'rational_reference_mass':list(map(str,Q)),'canonical_atom_brackets':atom_brackets,'uniform_log_ratio_bound':str(eps),'root_A':encode(A),'baseline':baseline,'policies':policies}
(BASE/'out/CHECK.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','assertions':COUNT,'runtime_seconds':summary['runtime_seconds'],'baseline_D':baseline['D_display'],'third_frontier_D_range':[min(x['D_display'] for x in policies),max(x['D_display'] for x in policies)],'baseline_conditional_sigma':float(sum(map(F,baseline['conditional_sigma']))/2),'third_source_zero_rows':[min(x['source_zero_rows'] for x in policies),max(x['source_zero_rows'] for x in policies)]},indent=2))
