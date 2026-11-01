from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
from itertools import product
import json,time,hashlib
from math import lcm
R=Path(__file__).resolve().parents[1];T=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v,checks;checks+=1
 assert time.perf_counter()-T<50
def sign(x,m):return (-1)**((x&m).bit_count()%2)
def spectrum(v):
 n=len(v);return [F(sum(v[x]*sign(x,m) for x in range(n))**2,n*n) for m in range(n)]
def influence(p):return sum((x*m.bit_count() for m,x in enumerate(p)),F(0))
@lru_cache(None)
def log2(q):
 q=F(q)
 if q==1:return F(0),F(0)
 N=4096;n=q.numerator**N;d=q.denominator**N;k=n.bit_length()-d.bit_length()
 def ge(a):return n>=(d<<a) if a>=0 else (n<<(-a))>=d
 if not ge(k):k-=1
 ck(ge(k) and not ge(k+1))
 return F(k,N),F(k+1,N)
def ce(p,q):
 lo=hi=F(0)
 for x,y in zip(p,q):
  if x:
   ck(y>0);l,h=log2(1/y);lo+=x*l;hi+=x*h
 return lo,hi
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def mean(v):return sum(x[0] for x in v)/len(v),sum(x[1] for x in v)/len(v)
def kl(p,q):return sub(ce(p,q),ce(p,p))
def ln2():
 z=F(1,3);N=20;l=sum((2*z**(2*j+1)/F(2*j+1) for j in range(N)),F(0));return l,l+2*z**(2*N+1)/F(2*N+1)/(1-z*z)
ell=ln2();K=(4+2/ell[1],4+2/ell[0]);booking=(F(5,4)/ell[1],F(5,4)/ell[0])
def margin(i,c):return K[0]*i-c[1]-booking[1],K[1]*i-c[0]-booking[0]
truth=[]
for x in range(64):
 s=x&7;u=(x>>3)&1;v=(x>>4)&1;z=x>>5;c=-1 if s==0 else 1
 g=c*(-1 if s==0 and u==0 else 1);h=c*(-1 if s==1 and v==0 else 1)
 truth.append(g if z==0 else h)
src=R.parent/'20261023T053904Z-fleet03-A012-sparse-activation-accounting/out/NEXT_TARGET.json'
target=json.loads(src.read_text(encoding='utf-8'));ck(truth==target['F']);Q=list(map(F,target['root_Q']));ck(spectrum(truth)==Q)
author=json.loads((R/'out/PARTIAL.json').read_text(encoding='utf-8'));states={};fullcontrol=[]
for state in product((-1,0,1),repeat=3):
 fixed={j:b for j,b in enumerate(state) if b!=-1};free=[j for j in range(6) if j not in fixed]
 members=[x for x in range(64) if all(((x>>j)&1)==b for j,b in fixed.items())]
 child=[truth[x] for x in members];p=spectrum(child);q=[F(0)]*len(child)
 for t,x in enumerate(Q):
  index=sum(((t>>j)&1)<<k for k,j in enumerate(free));q[index]+=x
 r0=(p[0]+q[0])/2;r=[r0]+[(1-r0)*x/(1-q[0]) for x in q[1:]]
 ck(sum(r)==1);a=author['states'][str(state)]
 ck(p==list(map(F,a['P'])));ck(q==list(map(F,a['Q_original_marginal'])));ck(r==list(map(F,a['R_profile'])))
 for j in range(1,len(q)):ck(r[j]*(1-q[0])==q[j]*(1-r0));ck((r[j]>0)==(q[j]>0))
 i=influence(p);ck(i==F(a['I']))
 old=ce(p,q);new=ce(p,r);charge=kl(r,q);net=sub(sub(old,new),charge)
 pp=[p[0],1-p[0]];qq=[q[0],1-q[0]];rr=[r0,1-r0]
 J=plus(kl(rr,qq),kl(qq,rr));ck(not(net[1]<J[0] or J[1]<net[0]))
 # Independent exact replay of the author's entire prime-log net-rebate vector:
 # exponentiate after clearing rational exponents, without factorizing any rational.
 vector={int(k):F(v) for k,v in a['net_rebate'].items()};coef=r0-q[0]
 den=lcm(coef.denominator,*[v.denominator for v in vector.values()]);lhs=F(1)
 for prime,v in vector.items():lhs*=F(prime)**int(den*v)
 odds=r0*(1-q[0])/(q[0]*(1-r0));ck(lhs==odds**int(den*coef))
 # Whole-category full calibration is a REAL negative arm, not an absent operation.
 full=[p[0]]+[(1-p[0])*x/(1-q[0]) for x in q[1:]]
 fullnet=sub(sub(old,ce(p,full)),kl(full,q));ck(fullnet[0]<=0<=fullnet[1]);fullcontrol.append(fullnet)
 conditional=F(0),F(0)
 if p[0]<1:
  conditional=kl([x/(1-p[0]) for x in p[1:]],[x/(1-q[0]) for x in q[1:]])
 states[state]={'I':i,'old':old,'new':new,'charge':charge,'net':net,'P0':p[0],'Q0':q[0],'R0':r0,'conditional_KL':conditional,'full_KL':kl(p,r)}
front=[states[(a,b,-1)] for a,b in product((0,1),repeat=2)];i=sum(s['I'] for s in front)/4;ck(i==F(1,2))
ck([s['P0'] for s in front]==[F(1,16),F(1),F(9,16),F(1)]);ck(all(s['Q0']==F(21,32) for s in front))
new=mean([s['new'] for s in front]);charge=mean([s['charge'] for s in front]);old=mean([s['old'] for s in front]);paid=margin(i,plus(new,charge));ck(paid[0]>F(1,128))
ck(margin(i,old)[1]<-F(15,64))
ck(front[0]['conditional_KL'][0]>0 and front[2]['conditional_KL'][0]>0)
# Constants retain positive CE and reference-only nonempty category.
ck(front[1]['new'][0]>0 and front[3]['new'][0]>0)
endpoints=[]
for t in (F(1,2),F(5,8)):
 costs=[]
 for a,b in product((0,1),repeat=2):
  s=author['states'][str((a,b,-1))];p=list(map(F,s['P']));q=list(map(F,s['Q_original_marginal']))
  r0=(1-t)*q[0]+t*p[0];r=[r0]+[(1-r0)*x/(1-q[0]) for x in q[1:]]
  ck(sum(r)==1);costs.append(plus(ce(p,r),kl(r,q)))
 m=margin(i,mean(costs));ck(m[0]>F(1,256));endpoints.append({'t':t,'margin_bits':m})
allthree=[states[x] for x in product((0,1),repeat=3)];ii=sum(x['I'] for x in allthree)/8;ck(ii==F(1,4));floor=margin(ii,(F(0),F(0)));ck(floor[1]<-F(1,16))
# Independently validate the A013 designated first-query child bank and untouched selector allowance.
G=[target['G'][j] for j in range(16)];H=[target['H'][j] for j in range(16)]
HG=ce(spectrum(G),spectrum(G));HH=ce(spectrum(H),spectrum(H));HF=ce(Q,Q)
reserve=(3-(HG[1]+HH[1])/2,3-(HG[0]+HH[0])/2)
c0=mean([states[(a,-1,-1)]['old'] for a in (0,1)]);tau=sub((K[0]/8,K[1]/8),sub(HF,c0));left=sub(reserve,tau);ck(left[0]>F(1,4))
delta=sub(HF,mean([HG,HH]));allowance=plus(sub((K[0]/8,K[1]/8),delta),(F(1,4)/ell[1],F(1,4)/ell[0]));ck(allowance[0]>F(1,2))
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
out={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-T,'paid_margin_bits':paid,'old_margin_bits':margin(i,old),'mean_conversion_bits':charge,'mean_net_rebate_bits':mean([s['net'] for s in front]),'frontier':front,'third_query_any_reference_margin_upper_bound_bits':floor,'A013_first_query_remaining_original_child_reserve_bits':left,'A013_untouched_selector_allowance_bits':allowance,'full_calibration_control_intervals':fullcontrol,'continuum_endpoints':endpoints}
(R/'out/REPLAY.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','assertions':checks,'seconds':out['seconds'],'paid_margin_bits':list(map(float,paid)),'conversion_bits':list(map(float,charge)),'third_query_floor_bits':list(map(float,floor)),'same_child_left_bits':list(map(float,left))}))
