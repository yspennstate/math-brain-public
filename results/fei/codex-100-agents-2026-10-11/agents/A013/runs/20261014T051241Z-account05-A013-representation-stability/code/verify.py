from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;Q=1<<80
def check(b):
 global checks
 checks+=1
 assert b,checks
 if time.perf_counter()-start>50:raise RuntimeError('50s verifier cutoff')
def ceildiv(a,b):return -((-a)//b)
# Independent fixed-point interval powers. No import of author log helper.
def ln_bounds(x):
 u=(x-1)/(x+1);ul=(u.numerator*Q)//u.denominator;uh=ceildiv(u.numerator*Q,u.denominator)
 u2l=ul*ul//Q;u2h=ceildiv(uh*uh,Q);pl,ph=ul,uh;lo=hi=0
 for j in range(32):
  lo+=2*pl//(2*j+1);hi+=ceildiv(2*ph,2*j+1)
  pl=pl*u2l//Q;ph=ceildiv(ph*u2h,Q)
 tail=F(2,65)*F(1,3)**65/F(8,9)
 return lo,hi+ceildiv(tail.numerator*Q,tail.denominator)
l2,h2=ln_bounds(F(2));check(F(l2,Q)>F(2,3))
@lru_cache(None)
def log_bounds(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=ln_bounds(x)
 return F(k)+F(lo,h2),F(k)+F(hi,l2)
@lru_cache(None)
def ell(x):
 if not x:return F(0),F(0)
 lo,hi=log_bounds(1/x);return x*lo,x*hi
def phi_hi(a,b):
 if not a or not b:return F(0)
 return ell(a)[1]+ell(b)[1]-ell(a+b)[0]
def fw(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
  h*=2
 return a
def pattern(mask):
 t=[1 if mask>>x&1 else -1 for x in range(8)];w=fw(t)
 return tuple(tuple(sorted(F(w[T]*t[0],8) for T in range(8) if T&1==g)) for g in [0,1])+(t[0]*t[1],)
profiles=json.loads((R/'out/PILOT_RESULTS.json').read_text())['profiles']
known={tuple(tuple(F(a) for a in g) for g in p['groups'])+(p['relative_sign'],) for p in profiles}
actual={pattern(mask) for mask in range(256)}
# A common character with odd first-coordinate frequency swaps the two
# parity groups and flips c(0)c(1). It preserves the erasure expression.
mirrored={(p[1],p[0],-p[2]) for p in known}
check(actual==known|mirrored);check(len(known)==8)
boxes=visited=0;minimum=None;profile_receipts=[]
for idx,p in enumerate(profiles):
 doc=json.loads((R/f'out/CONTINUUM_{idx}.json').read_text());check(doc['status']=='PASS')
 check(doc['code_sha256']==hashlib.sha256((R/'code/continuum.py').read_bytes()).hexdigest())
 leaves={tuple(F(v) for interval in [c['p'],c['q']] for v in interval):c for c in doc['certificates']};used=set()
 groups=[[F(a) for a in g] for g in p['groups']]
 def walk(lp,hp,lq,hq,depth):
  global boxes,visited,minimum
  visited+=1;check(depth<=4)
  if (hp+hq)/8<=F(1,32) or (lp+lq)/8>=F(1,6):return
  key=(lp,hp,lq,hq)
  if key in leaves:
   cert=leaves[key];check(cert['depth']==depth);check(key not in used);used.add(key)
   bound=(lp+lq+lp*lp+lq*lq)/4
   for g in [0,1]:
    sg=p['relative_sign']*(-1 if g else 1)
    kl=(lp+(lq if sg==1 else -hq))/8;kh=(hp+(hq if sg==1 else -lq))/8
    for a in groups[g]:bound-=phi_hi(max((a-kl)**2,(a-kh)**2),max(kl*kl,kh*kh))
   check(bound>=F(cert['gap_lower'])>0);boxes+=1
   low=F(cert['gap_lower']);minimum=low if minimum is None else min(minimum,low);return
  check(depth<4)
  mp=(lp+hp)/2;mq=(lq+hq)/2
  for pl,ph in [(lp,mp),(mp,hp)]:
   for ql,qh in [(lq,mq),(mq,hq)]:walk(pl,ph,ql,qh,depth+1)
 for i in range(16):
  for j in range(16):walk(F(i,16),F(i+1,16),F(j,16),F(j+1,16),0)
 check(used==set(leaves));profile_receipts.append({'index':idx,'certificates':len(leaves)})
 print('independent profile',idx,'PASS',flush=True)
res={'status':'PASS','method':'Independent 80-bit integer interval powers/32-term atanh; exact Fraction endpoint arithmetic; reconstructed box coverage tree; all256 phases classified with explicit character parity-group swap','classification_phases':256,'raw_grouped_profiles':len(actual),'canonical_grouped_profiles':8,'certified_boxes':boxes,'visited_boxes':visited,'minimum_gap':str(minimum),'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'profiles':profile_receipts}
(R/'out/VERIFY_RESULTS.json').write_text(json.dumps(res,indent=2),encoding='utf-8');print(json.dumps(res))
