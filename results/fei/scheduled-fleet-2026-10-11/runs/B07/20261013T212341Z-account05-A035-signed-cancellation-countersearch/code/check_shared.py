from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import sys,json,time
ROOT=Path(__file__).resolve().parents[1];(ROOT/'out').mkdir(exist_ok=True)
PILOT='--pilot' in sys.argv;START=time.perf_counter();CAP=50 if PILOT else 240
def clock():
 if time.perf_counter()-START>CAP:raise RuntimeError('frozen runtime cap reached; no domain escalation')
def fwht(v):
 v=list(v);s=1
 while s<len(v):
  clock()
  for base in range(0,len(v),2*s):
   for j in range(base,base+s):a,b=v[j],v[j+s];v[j],v[j+s]=a+b,a-b
  s*=2
 return v
def unitln(q):
 z=(q-1)/(q+1);term=z;lo=Q(0)
 for j in range(28):lo+=2*term/Q(2*j+1);term*=z*z
 return lo,lo+2*term/Q(57)/(1-z*z)
LN2=unitln(Q(2))
@lru_cache(None)
def logint(k):
 if k==1:return Q(0),Q(0)
 shift=k.bit_length()-1;l,u=unitln(Q(k,1<<shift))
 return shift+l/LN2[1],shift+u/LN2[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,k):return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
def ratlog(q):return sub(logint(q.numerator),logint(q.denominator))
def ent(q):return mul(ratlog(q),-q) if q else (Q(0),Q(0))
def h2(q):return add(ent(q),ent(1-q))
def phi(a,b):return sub(add(ent(a),ent(b)),ent(a+b))
def emit(a):
 scale=10**12
 return [str(Q(a[0].numerator*scale//a[0].denominator,scale)),str(Q(-((-a[1].numerator*scale)//a[1].denominator),scale))]
LOGE=(1/LN2[1],1/LN2[0])
def bent(x,n):return -1 if sum(((x>>(2*j))&3)==3 for j in range(n//2))%2 else 1
def table(m,L):
 n=m+5*L;vals=[]
 for a in range(1<<n):
  y=a&((1<<m)-1);p=y.bit_count()%2;s=bent(y,m)
  for j in range(L):
   x=(a>>(m+5*j))&15;z=(a>>(m+5*j+4))&1
   s*=bent(x,4)
   if p and x==0 and z:s=-s
  vals.append(s)
 return vals
def influence(t):
 N=len(t);n=N.bit_length()-1
 return Q(sum(t[x]!=t[x^(1<<j)] for j in range(n) for x in range(N)),N)
def spectrumI(t):
 N=len(t);a=fwht(t)
 return a,Q(sum(s.bit_count()*v*v for s,v in enumerate(a)),N*N)
def restrict(t,i,value):
 n=len(t).bit_length()-1;lo=(1<<i)-1
 return [t[(x&lo)|((x&~lo)<<1)|(value<<i)] for x in range(1<<(n-1))]
def entropy_table(t):
 N=len(t);hist=Counter(v*v for v in fwht(t) if v);H=(Q(0),Q(0))
 for v,c in hist.items():H=add(H,mul(ent(Q(v,N*N)),c))
 return H
checks=0
def split(t,i):
 global checks
 N=len(t)//2;g,h=restrict(t,i,0),restrict(t,i,1)
 A=[(x+y)//2 for x,y in zip(g,h)];V=[(x-y)//2 for x,y in zip(g,h)]
 assert all(a*a+v*v==1 and a*v==0 for a,v in zip(A,V));checks+=1
 u,v=fwht(A),fwht(V);d=Q(sum(x*x for x in v),N*N)
 assert d==Q(sum(x!=y for x,y in zip(g,h)),N);checks+=1
 # Full mixed signed convolutions: transform back to physical A,V,
 # multiply there, transform again. No absolute values precede cancellation.
 aa,vv=fwht(u),fwht(v);mixed=fwht([a*b for a,b in zip(aa,vv)])
 assert mixed==[0]*N;checks+=1
 signedvv=fwht([a*a for a in vv]);G=[a*b for a,b in zip(g,h)];gh=fwht(G)
 assert all((N**3 if s==0 else 0)-2*signedvv[s]==N*N*gh[s] for s in range(N));checks+=1
 W=Q(sum(s.bit_count()*a*a for s,a in enumerate(gh)),2*N*N)
 assert W==influence(G)/2;checks+=1
 B=(Q(0),Q(0));pairs=Counter(zip((a*a for a in u),(a*a for a in v)))
 for (a,b),count in pairs.items():B=add(B,mul(phi(Q(a,N*N),Q(b,N*N)),count))
 M=sub(h2(d),B);R=sub((W,W),ent(d));sigma=sub(mul(LOGE,d),ent(1-d))
 reconstruction=sub(sub(sub(add((W,W),mul(LOGE,d)),R),M),sigma)
 assert reconstruction[0]<=B[1] and reconstruction[1]>=B[0];checks+=1
 assert R[1]>=0 and M[1]>=0 and sigma[1]>=0;checks+=3
 return dict(d=d,W=W,B=B,M=M,R=R,sigma=sigma)
# Exact five-variable local module: b_4(x)(-1)^(A_4(x)z).
module=[bent(a&15,4)*(-1 if (a&15)==0 and (a>>4)&1 else 1) for a in range(32)]
mod=split(module,4);beta=mod['B'];Hmod=entropy_table(module)
assert mod['d']==Q(1,16) and mod['W']==Q(1,4) and beta[0]>Q(1,4);checks+=3
closed_beta=add(add((Q(1),Q(1)),mul(logint(13),Q(39,64))),add(mul(logint(3),Q(-45,64)),mul(logint(5),Q(-25,32))))
assert beta[0]<=closed_beta[1] and beta[1]>=closed_beta[0];checks+=1
closed_H=add((Q(8),Q(8)),add(mul(logint(3),Q(-45,64)),mul(logint(5),Q(-75,64))))
assert Hmod[0]<=closed_H[1] and Hmod[1]>=closed_H[0];assert Hmod[1]<Q(37,8);checks+=2
point=[bent(x,4)*(-1 if x==0 else 1) for x in range(16)]
Hpoint=entropy_table(point);assert influence(point)==Q(5,2);checks+=1
cases=[(2,1),(4,1)] if PILOT else [(2,1),(4,1),(8,1),(4,2),(6,2)]
records=[]
for m,L in cases:
 clock();t=table(m,L);n=m+5*L;a,I=spectrumI(t);assert I==influence(t)==Q(m,2)+Q(69*L,32);checks+=2
 H=entropy_table(t);expected=add((Q(m),Q(m)),mul(add((Q(4),Q(4)),Hmod),Q(L,2)))
 assert H[0]<=expected[1] and H[1]>=expected[0];checks+=1
 contexts=[]
 for j in range(L):
  for history in range(1<<j):
   fixed={m+5*k+4:(history>>k)&1 for k in range(j)}
   child=t;labels=list(range(n))
   for label,value in sorted(fixed.items(),reverse=True):child=restrict(child,labels.index(label),value);labels.remove(label)
   q=split(child,labels.index(m+5*j+4))
   assert q['d']==Q(1,32) and q['W']==Q(m+4,32);checks+=2
   expected_beta=mul(beta,Q(1,2));assert q['B'][0]<=expected_beta[1] and q['B'][1]>=expected_beta[0] and q['B'][0]>4*q['d'];checks+=2
   assert q['R'][0]<=Q(m-1,32)<=q['R'][1];checks+=1
   contexts.append(dict(j=j,history=history,d=str(q['d']),W=str(q['W']),B=emit(q['B']),M=emit(q['M']),R=emit(q['R']),D4=emit(sub(q['B'],(4*q['d'],4*q['d'])))))
 records.append(dict(m=m,L=L,n=n,I=str(I),H=emit(H),prefix_contexts=contexts))
 with (ROOT/'out'/('pilot_direct.jsonl' if PILOT else 'direct.jsonl')).open('a',encoding='utf-8') as fp:fp.write(json.dumps(records[-1])+'\n')
# Frozen analytic cases; proof in DERIVATION.md supplies the all-m bridge.
analytic=[]
for m in [8,16,32,64,128,256,1024]:
 L=m;I=Q(85*m,32);d=Q(1,32);B=mul(beta,Q(1,2));W=Q(m+4,32);R=Q(m-1,32)
 D4=sub(B,(Q(1,8),Q(1,8)));M=sub(h2(d),B);sigma=sub(mul(LOGE,d),ent(1-d))
 raw=Q(m*(m+4),32);good=Q(m,8);joint=mul(D4,m);r_dropped=add(joint,(m*R,m*R))
 assert D4[0]>0 and joint[1]<I and Q(m+4,85)==raw/I;checks+=3
 assert Q(15,16)**m<Q(3,5);checks+=1
 leafI=Q(17*m,8);leafH=mul(add((Q(3),Q(3)),mul(Hpoint,Q(1,4))),m)
 assert I-leafI==Q(m,2)+Q(m,32) and leafH[1]<=2*leafI;checks+=2
 analytic.append(dict(m=m,L=L,n=6*m,I=str(I),bad_prefix_raw_W=str(raw),bad_prefix_raw_W_over_I=str(raw/I),good_order_raw_W=str(good),good_order_raw_W_over_I=str(good/I),joint_prefix=emit(joint),joint_prefix_over_I=emit(mul(joint,1/I)),physical_R_prefix=str(m*R),R_dropped_prefix_over_I=emit(mul(r_dropped,1/I)),terminal_I=str(leafI),terminal_H=emit(leafH)))
# No floating arithmetic participates in a sign decision.
assert 5**5<2**12 and Q(15,16)**8<Q(3,5);checks+=2
nonB=h2(Q(9,25));assert nonB[0]>mul(LOGE,Q(9,25))[1];checks+=1
out=dict(helper_version='A035-shared-parity-v1',pilot=PILOT,runtime_seconds=time.perf_counter()-START,counted_exact_checks=checks,direct_case_count=len(records),prefix_context_count=sum(len(x['prefix_contexts']) for x in records),beta=emit(beta),beta_over_q=emit(mul(beta,16)),module_H=emit(Hmod),point_H=emit(Hpoint),direct=records,analytic=analytic,non_Boolean_discriminator=dict(coefficients=['4/5','3/5'],d='9/25',B=emit(nonB),W='0',claimed_upper=emit(mul(LOGE,Q(9,25))),status='violation of Boolean-only phase bound'),limitations='Exact fixed-domain checks plus analytic proof; independent reviewer acceptance pending; every-tree strengthening refuted, existential tree bridge not refuted.')
(ROOT/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['direct','analytic']},indent=2))
print('First and last analytic cases:',analytic[0],analytic[-1])
