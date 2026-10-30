import json,time,sys,math,hashlib
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv
CAP=60 if PILOT else 600
spec={'helper_version':'A079-cubic-row-v2','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'Actual two-address Boolean functions; integer height-two product rows with one primitive magnitude ratio 2,3,4, arbitrary Fourier signs; quadratic-pair inverse support subfamily','domain':'All 256 Boolean signs on 2 address+1 data bits; quadratic row pairs m<=2' if PILOT else 'All 65536 Boolean signs on 2 address+2 data bits; all quadratic branch pairs m=0..3 modulo simultaneous sign; 12 fixed higher-rank/translation endpoints m=4,5,7; A032 actual 64-sign witness plus sharp conditional witness','case_count':256+3*138 if PILOT else 65536+3*8330+12+2,'symmetry':'Global sign removed only for row branch pairs, no reduction of Boolean truth tables','arithmetic':'integer Walsh, gcd, Fraction, prime-log identities; rational 120-term atanh tails rounded outward to denominator2^96','memory_estimate':'below100MB; largest table256 entries; bounded caches','maximum_runtime_seconds':CAP}
(ROOT/'out'/('FROZEN_PILOT_V2.json' if PILOT else 'FROZEN_FULL_V2.json')).write_text(json.dumps(spec,indent=2)+'\n')
START=time.monotonic();ASSERT=0;COUNTS=Counter();FORMS=Counter();ADMITTED=Counter()
def ck(x):
 global ASSERT
 ASSERT+=1;assert x,ASSERT
 if time.monotonic()-START>CAP:raise RuntimeError('Frozen runtime cap exceeded')
def W(v):
 a=list(v);j=1
 while j<len(a):
  for k in range(0,len(a),2*j):
   for i in range(k,k+j):a[i],a[i+j]=a[i]+a[i+j],a[i]-a[i+j]
  j*=2
 return a
@lru_cache(None)
def fac(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return tuple(out.items())
def add(*terms):
 d={}
 for c,e in terms:
  for p,v in e.items():d[p]=d.get(p,Q(0))+c*v
 return {p:v for p,v in d.items() if v}
def logq(q):return add((1,dict(fac(q.numerator))),(-1,dict(fac(q.denominator))))
@lru_cache(None)
def H(weights):
 den=sum(weights)
 return add(*[(-Q(v,den),logq(Q(v,den))) for v in weights if v]) if den else {}
@lru_cache(None)
def logbounds(n):
 def ln(x):
  z=Q(x-1,x+1);s=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(120)),Q(0));tail=2*z**241/(241*(1-z*z));return s,s+tail
 a,b=ln(n);c,d=ln(2);lo=a/d;hi=b/c;D=1<<96
 return Q((lo.numerator*D)//lo.denominator,D),Q(-((-hi.numerator*D)//hi.denominator),D)
@lru_cache(None)
def positive(items):
 lo=Q(0)
 for p,c in items:
  a,b=(Q(1),Q(1)) if p==2 else logbounds(p)
  lo+=c*(a if c>=0 else b)
 return lo>0
def nonnegative(e):ck(not e or positive(tuple(sorted(e.items()))))
HB=H((9,1));KC=add((Q(3,2),{2:Q(1)}),(Q(5,2),HB));KJ={2:Q(10),3:-Q(3)}
def I(weights):return Q(sum(v*s.bit_count() for s,v in enumerate(weights)),sum(weights))
def product_row(h):
 a=W(h);sqs=tuple(x*x for x in a);norm=sum(sqs)
 if not norm:return None
 d=(len(h)).bit_length()-1;qs=[Q(sum(v for s,v in enumerate(sqs) if s>>j&1),norm) for j in range(d)]
 for s,v in enumerate(sqs):
  p=Q(1)
  for j,q in enumerate(qs):p*=q if s>>j&1 else 1-q
  if p!=Q(v,norm):return None
 varying=[j for j,q in enumerate(qs) if q not in (0,1)]
 nonfair=[j for j in varying if qs[j]!=Q(1,2)]
 if not nonfair:return {'kind':'fair','m':len(varying),'sq':sqs,'I':I(sqs),'H':H(sqs),'R':{2:Q(len(varying))}}
 if len(nonfair)!=1:return None
 bit=nonfair[0];small=min(qs[bit],1-qs[bit]);ratios={Q(1,5):2,Q(1,10):3,Q(1,17):4}
 if small not in ratios:return None
 other=[j for j in varying if j!=bit];base=next(s for s,v in enumerate(sqs) if v)&~sum(1<<j for j in varying)
 quadratic=True
 for b in range(2):
  phase=[int(a[base|(b<<bit)|sum(((u>>k)&1)<<j for k,j in enumerate(other))]<0) for u in range(1<<len(other))]
  anf=phase[:]
  for j in range(len(other)):
   for u in range(len(anf)):
    if u>>j&1:anf[u]^=anf[u^(1<<j)]
  if any(v and u.bit_count()>2 for u,v in enumerate(anf)):quadratic=False
 l1=sum(abs(x) for x in a)
 s=min(abs(x) for x in a if x);ck(s&(s-1)==0)
 return {'kind':str(ratios[small]),'m':len(other),'sq':sqs,'I':I(sqs),'H':H(sqs),'R':logq(Q(l1*l1,norm)),'quadratic_branches':quadratic}
def boolean_case(f,group):
 N=len(f)//4;h=[[sum(f[4*y+x]*(-1)**((x&j).bit_count()) for x in range(4))//2 for y in range(N)] for j in range(4)]
 mixed=[y for y in range(N) if all(abs(h[j][y])==1 for j in range(4))]
 for y in range(N):ck(y in mixed or sorted(abs(h[j][y]) for j in range(4))==[0,0,0,2])
 norms=[sum(v*v for v in r) for r in h];weights=[Q(n,4*N) for n in norms];ck(sum(weights)==1)
 ia=sum(w*j.bit_count() for j,w in enumerate(weights));delta=Q(len(mixed),N);ck(ia>=delta)
 cond={};iy=Q(0);wr={};mixedonly=Q(0);classes=[]
 for j,row in enumerate(h):
  if not norms[j]:continue
  a=W(row);sq=tuple(v*v for v in a);norm=sum(sq);ck(norm==N*norms[j])
  l1=sum(abs(v) for v in a);maximum=max(abs(v) for v in row)
  ck(Q(l1*l1,4*N*N)>=Q(maximum*maximum,4))
  # w*exp2(H_1/2)=L1(raw)^2/(4N^2); proves each entropy bound exactly.
  if maximum==1:ck(weights[j]==delta/4);mixedonly+=weights[j]
  cond=add((1,cond),(weights[j],H(sq)));iy+=weights[j]*I(sq)
  wr=add((1,wr),(weights[j],logq(Q(l1*l1,norm))))
  classes.append(product_row(row))
 ck(mixedonly<=delta)
 fullsq=tuple(v*v for v in W(f));ck(I(fullsq)==ia+iy)
 rootH=H(fullsq);addressH=H(tuple(norms));ck(rootH==add((1,addressH),(1,cond)))
 # Per-row exact rational bounds plus mixedonly<=I_A certify H(w)<=E R+2 I_A.
 if all(c is not None for c in classes):
  for c in classes:
   if c['kind']=='2':ck(c['m']>=1)
   if c['kind']=='4':ck(c['m']>=3)
  for j,row in enumerate(h):
   if not norms[j]:continue
   c=product_row(row)
   if c['kind'] in ('2','3'):ck(weights[j]<=Q(5,8))
   if c['kind']=='4':ck(weights[j]<=Q(17,32))
  nonnegative(add((iy,KC),(-1,cond)))
  nonnegative(add((ia+iy,KJ),(-1,rootH)))
  COUNTS[group+'_admitted']+=1
 COUNTS[group]+=1
@lru_cache(None)
def phase(mask,m):
 pairs=[(i,j) for i in range(m) for j in range(i+1,m)]
 return [(-1)**((mask&1)^sum(((mask>>(1+i))&1)*((x>>i)&1) for i in range(m))^sum(((mask>>(1+m+k))&1)*((x>>i)&1)*((x>>j)&1) for k,(i,j) in enumerate(pairs))) for x in range(1<<m)]
def row_pair(m,q0,q1,ratio,group):
 a,b=W(phase(q0,m)),W(phase(q1,m));raw=[ratio*x+y for x,y in zip(a,b)]+[ratio*x-y for x,y in zip(a,b)]
 g=math.gcd(*raw);primitive=[v//g for v in raw];height=max(abs(v) for v in primitive)
 COUNTS[group]+=1
 if height>2:return
 S0={i for i,v in enumerate(a) if v};S1={i for i,v in enumerate(b) if v}
 r0=(len(S0)).bit_length()-1;r1=(len(S1)).bit_length()-1
 A=Q(ratio*max(abs(x) for x in a),g);B=Q(max(abs(x) for x in b),g)
 if S0==S1:
  ck(ratio==3 and sorted([A,B])==[Q(1,2),Q(3,2)]);form='same'
 elif S0&S1:
  ck(A==B==1 and ratio in (2,4));ck(r0-r1==2*(ratio.bit_length()-1));form='overlap'
 else:
  ck(A in (1,2) and B in (1,2) and ratio in (2,4));ck(Q(ratio)==A/B*Q(2)**Q(r0-r1,2));form='disjoint'
 if ratio==2:ck(m>=1)
 if ratio==4:ck(m>=3)
 for t in range(1,2//height+1):
  h=[t*v for v in primitive];c=product_row(h);ck(c is not None and c['kind']==str(ratio))
  w=Q(sum(v*v for v in h),4*len(h));
  if ratio==4:ck(w<=Q(17,32))
  FORMS[str((ratio,form,A*t,B*t,r0,r1))]+=1;ADMITTED[str((m,ratio))]+=1
def receipt(final=False):
 v={'status':'PASS','final':final,'cases':dict(COUNTS),'assertions':ASSERT,'row_forms':dict(FORMS),'admitted_rows':dict(ADMITTED),'seconds':time.monotonic()-START,'independent_review':False}
 (ROOT/'out'/('pilot_validation.json' if PILOT else 'validation.json')).write_text(json.dumps(v,indent=2)+'\n');return v
d=1 if PILOT else 2;L=1<<(d+2)
for mask in range(1<<L):boolean_case([1 if mask>>i&1 else -1 for i in range(L)],'Boolean_data'+str(d))
receipt()
for m in range(3 if PILOT else 4):
 bits=1+m+m*(m-1)//2
 for q0 in range(0,1<<bits,2):
  for q1 in range(1<<bits):
   for r in [2,3,4]:row_pair(m,q0,q1,r,'quadratic_pairs_m'+str(m))
 receipt()
if not PILOT:
 for m in [4,5,7]:
  quad=sum(1<<(1+m+k) for k,(i,j) in enumerate([(i,j) for i in range(m) for j in range(i+1,m)]) if (i,j) in [(0,1),(2,3)] + ([(4,5)] if m==7 else []))
  for lin in [0,1<<(1+m-1)]:
   for r in [2,4]:row_pair(m,quad,lin,r,'fixed_endpoints')
 source=Path(r'~\brain_workers\FEI100_20261011\agents\A032\runs\20261013T221334Z-fleet05-A032-boolean-phase-realizability\out\witness.json')
 witness=json.loads(source.read_text());(ROOT/'out'/'A032_WITNESS_SOURCE.json').write_text(json.dumps({'path':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_keys':list(witness)},indent=2)+'\n')
 rows=witness['slices_h'];f=[]
 for y in range(16):
  for x in range(4):
   value=sum(rows[j][y]*(-1)**((j&x).bit_count()) for j in range(4));ck(value in (-2,2));f.append(value//2)
 boolean_case(f,'A032_witness');ck(COUNTS['A032_witness_admitted']==1)
 (ROOT/'out'/'actual_witness.json').write_text(json.dumps({'truth_table':f,'rows':rows,'class': [product_row(h)['kind'] for h in rows]},indent=2)+'\n')
 # Sharp conditional equality: actual 3-bit point defect.
 f=[1]*8;f[-1]=-1;boolean_case(f,'sharp_conditional_witness')
 hs=[[sum(f[4*y+x]*(-1)**((x&j).bit_count()) for x in range(4))//2 for y in range(2)] for j in range(4)]
 sq=[tuple(v*v for v in W(h)) for h in hs];cond=add(*[(Q(sum(v*v for v in h),8),H(s)) for h,s in zip(hs,sq)])
 iy=sum(Q(sum(v*v for v in h),8)*I(s) for h,s in zip(hs,sq));ck(iy==Q(1,4));ck(cond==add((iy,KC)))
ck(3**5<2**8);ck(3**12>2**19);ck(5**3<2**7);ck(5**10>2**23);ck(17**4<2**17)
print(json.dumps(receipt(True),indent=2))
