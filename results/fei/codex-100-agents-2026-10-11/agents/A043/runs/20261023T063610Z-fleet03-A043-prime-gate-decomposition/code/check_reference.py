"""Frozen finite certificates for a complete paid-sector reference; v1."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'out';OUT.mkdir(exist_ok=True)
spec={'helper':'A043-paid-sector-complete-reference-v1.2','family':'Boolean signs plus three genuine disjoint compositions and one explicitly excluded non-Boolean control',
 'domain':'all n=0,1,2 signs at p in {1/4,1/2,3/4}; all 256 ternary signs at fair law; five ternary prime reps on {1/4,3/4}^3; prime56067 on {1/4,1/2,3/4}^4; bent tensors n=2,4; three fixed compositions of dimensions 5,4,6',
 'case_count':540,'nonboolean_controls':1,'duplicate_strict_improvement_control':1,'symmetry':'none; ternary representatives are additional sourced fixtures, not an exhaustive orbit claim',
 'arithmetic':'Fraction spectra, full reference masses and likelihood ratios; outward 24-term atanh logarithms; exact dyadic cell assignment',
 'memory_estimate_mb':80,'max_runtime_seconds':55,'automatic_dimension_escalation':False}
(OUT/'frozen_spec.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.perf_counter();checks=0;profiles=0
def ck(b):
 global checks
 checks+=1
 if not b:raise AssertionError(checks)
def mul(xs):
 a=Q(1)
 for x in xs:a*=x
 return a
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def scale(a,x):return (a[0]*x,a[1]*x) if x>=0 else (a[1]*x,a[0]*x)
zero=(Q(0),Q(0))
def basiclog(t):
 z=(t-1)/(t+1);ck(0<=z<=Q(1,3))
 l=sum((Q(2,2*j+1)*z**(2*j+1) for j in range(24)),Q(0))
 return l,l+2*z**49/(49*(1-z*z))
L2=basiclog(Q(2));L4=scale(L2,2)
@lru_cache(maxsize=4096)
def ln(x):
 ck(x>0)
 if x==1:return zero
 if x<1:return scale(ln(1/x),-1)
 k=0
 while x>=2:x/=2;k+=1
 return add(basiclog(x),scale(L2,k))
def isum(xs):
 a=zero
 for x in xs:a=add(a,x)
 return a
def overlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
def compact(a):
 D=2**80
 return [str(Q((a[0]*D).__floor__(),D)),str(Q((a[1]*D).__ceil__(),D))]
def KL(p,q):
 ck(sum(p)==sum(q)==1)
 if p==q:return zero
 for a,b in zip(p,q):ck(a==0 or b>0)
 a=isum(scale(ln(x/y),x) for x,y in zip(p,q) if x)
 ck(a[0]>=0);return a
def signs(n,mask):return [Q(1) if mask>>i&1 else Q(-1) for i in range(1<<n)]
def analyze(values,p,boolean=True):
 global profiles
 profiles+=1;ck(time.perf_counter()-start<55)
 n=len(p);v=[4*t*(1-t) for t in p]
 wt=[mul(p[j] if b>>j&1 else 1-p[j] for j in range(n)) for b in range(1<<n)]
 P=[];c=[];W=[];jscale=[]
 for s in range(1<<n):
  m=sum((wt[b]*values[b]*mul(Q((b>>j)&1)-p[j] for j in range(n) if s>>j&1) for b in range(1<<n)),Q(0))
  den=mul(p[j]*(1-p[j]) for j in range(n) if s>>j&1)
  c.append(m/(2**s.bit_count()*den));P.append(m*m/den)
  if s==0 or m==0:W.append(Q(0));jscale.append(0);continue
  u=abs(c[-1]);ck(0<u<=1);j=0
  while u<=Q(1,2):u*=2;j+=1
  ck(Q(1,2)<u<=1);jscale.append(j)
  W.append(mul(v[k] for k in range(n) if s>>k&1)/4**j)
  ck(P[-1]<=W[-1]<4*P[-1])
 ck(sum(P)==1)
 w=1-P[0];M=sum((P[s] for s in range(1,1<<n) if s.bit_count()>=2),Q(0));A=w-M
 Delta=sum(((s.bit_count()-1)*P[s] for s in range(1,1<<n)),Q(0))
 R=sum(((s.bit_count()-2)*P[s] for s in range(1,1<<n) if s.bit_count()>=3),Q(0));ck(M==Delta-R)
 Zh=sum((W[s] for s in range(1,1<<n) if s.bit_count()>=2),Q(0));Z=sum(W);Z1=Z-Zh
 Qstar=[P[s] if s.bit_count()<2 else (M*W[s]/Zh if M else Q(0)) for s in range(1<<n)]
 Qflat=[P[0]]+[w*W[s]/Z if w else Q(0) for s in range(1,1<<n)]
 ck(sum(Qstar)==sum(Qflat)==1)
 Kstar=KL(P,Qstar);Kflat=KL(P,Qflat)
 E1=isum(scale(ln(1/c[s]**2),P[s]) for s in range(1,1<<n) if s.bit_count()==1 and P[s])
 Ehi=isum(scale(ln(1/c[s]**2),P[s]) for s in range(1,1<<n) if s.bit_count()>=2 and P[s]);E=add(E1,Ehi)
 Jhi=scale(L4,sum((P[s]*jscale[s] for s in range(1,1<<n) if s.bit_count()>=2),Q(0)))
 Jall=scale(L4,sum((P[s]*jscale[s] for s in range(1,1<<n)),Q(0)))
 nhi=scale(ln(Zh/M),M) if M else zero;nflat=scale(ln(Z/w),w) if w else zero
 ck(nhi[0]>=0);ck(nhi[1]<=scale(L4,M)[1]);ck(Kstar[0]>=0);ck(Kstar[0]<=nhi[1])
 Cstar=add(add(E1,Jhi),nhi);Cflat=add(Jall,nflat)
 overlap(E,sub(Cstar,Kstar));overlap(E,sub(Cflat,Kflat))
 transfer=zero
 if A:
  ps=[P[s]/A for s in range(1,1<<n) if s.bit_count()==1]
  qs=[W[s]/Z1 for s in range(1,1<<n) if s.bit_count()==1]
  transfer=scale(KL(ps,qs),A)
 if A and M:transfer=add(transfer,scale(KL([A/w,M/w],[Z1/Z,Zh/Z]),w))
 overlap(sub(Kflat,Kstar),transfer);overlap(sub(Cflat,Cstar),transfer)
 S=sub((4*Delta-2*R,)*2,E1)
 U=isum(scale(ln(4*(2**jscale[s]*abs(c[s]))**2),P[s]) for s in range(1,1<<n) if s.bit_count()>=2 and P[s])
 rhs=add(Jhi,scale(L4,Delta-R));rhs=add(rhs,(4*Delta-2*R,)*2)
 overlap(E,sub(sub(rhs,S),U))
 if boolean:
  ck(set(values)<={Q(-1),Q(1)});ck(S[0]>=0);ck(U[0]>=0);ck(sub(rhs,E)[1]>=0)
 return {'P':P,'Qstar':Qstar,'Kstar':Kstar,'Kflat':Kflat,'Cstar':Cstar,'E':E,'Ehi':Ehi,'Delta':Delta,'R':R,'M':M,'nhi':nhi,'Jhi':Jhi,'S':S,'U':U,'mean':c[0]}
count=0
for n in range(3):
 for mask in range(1<<(1<<n)):
  for p in product((Q(1,4),Q(1,2),Q(3,4)),repeat=n):analyze(signs(n,mask),p);count+=1
for mask in range(256):analyze(signs(3,mask),(Q(1,2),)*3);count+=1
for mask in (22,23,24,25,27):
 for p in product((Q(1,4),Q(3,4)),repeat=3):analyze(signs(3,mask),p);count+=1
prime=[Q(1) if 56067>>(i^6)&1 else Q(-1) for i in range(16)]
for p in product((Q(1,4),Q(1,2),Q(3,4)),repeat=4):analyze(prime,p);count+=1
bent=[]
for r in (1,2):
 vals=[Q(-1)**sum(((b>>(2*j))&1)*((b>>(2*j+1))&1) for j in range(r)) for b in range(1<<(2*r))]
 a=analyze(vals,(Q(1,2),)*(2*r));count+=1
 ck(a['Qstar']==a['P']);ck(a['nhi']==a['Kstar']==zero);overlap(a['Ehi'],a['Jhi'])
 bent.append({'r':r,'normalizer':str(a['nhi']),'KL':str(a['Kstar'])})
def compose(outer_mask,blocks,p):
 m=len(blocks);sizes=[(len(b)-1).bit_length() for b in blocks];ck(sum(sizes)==len(p))
 children=[];offset=0
 for b,k in zip(blocks,sizes):children.append(analyze(b,p[offset:offset+k]));offset+=k
 gp=[(1+x['mean'])/2 for x in children];g=analyze(signs(m,outer_mask),gp)
 vals=[]
 for x in range(1<<len(p)):
  off=0;label=0
  for i,(b,k) in enumerate(zip(blocks,sizes)):
   label|=int(b[(x>>off)&((1<<k)-1)]==1)<<i;off+=k
  vals.append(Q(1) if outer_mask>>label&1 else Q(-1))
 F=analyze(vals,p);tree=[]
 for s in range(1<<len(p)):
  off=0;A=0;fac=Q(1);pfac=Q(1)
  for i,(ch,k) in enumerate(zip(children,sizes)):
   t=(s>>off)&((1<<k)-1);off+=k
   if t:
    A|=1<<i;wi=1-ch['P'][0];fac*=ch['Qstar'][t]/wi;pfac*=ch['P'][t]/wi
  tree.append(g['Qstar'][A]*fac);ck(F['P'][s]==g['P'][A]*pfac)
 ktree=KL(F['P'],tree);weights=[]
 for i,ch in enumerate(children):weights.append(sum((g['P'][s] for s in range(1,1<<m) if s>>i&1),Q(0))/(1-ch['P'][0]))
 expected=add(g['Kstar'],isum(scale(ch['Kstar'],a) for ch,a in zip(children,weights)))
 overlap(ktree,expected)
 ctree=add(g['Cstar'],isum(scale(ch['Cstar'],a) for ch,a in zip(children,weights)))
 overlap(F['E'],sub(ctree,ktree));ck(F['Delta']==g['Delta']+sum((a*ch['Delta'] for ch,a in zip(children,weights)),Q(0)))
 return {'dimension':len(p),'outer_mask':outer_mask,'empty_mass_preserved':tree[0]==F['P'][0],'KL_interval_outward_80bit':compact(ktree)}
compositions=[]
compositions.append(compose(22,[signs(2,8),signs(2,14),signs(1,2)],tuple(map(Q,('1/4','1/3','2/3','3/4','2/5')))));count+=1
compositions.append(compose(8,[signs(3,25),signs(1,2)],tuple(map(Q,('1/5','2/3','3/7','4/5')))));count+=1
compositions.append(compose(22,[signs(3,25),signs(2,8),signs(1,2)],tuple(map(Q,('1/5','2/3','3/7','4/5','2/5','3/5')))));count+=1
strict=analyze(signs(2,8),(Q(3,4),Q(3,4)));ck(strict['Qstar']==strict['P']);ck(strict['Kflat'][0]>0)
excluded=analyze([Q(1,5),Q(7,5)],(Q(1,2),),boolean=False)
ck(excluded['Delta']==excluded['M']==0);ck(excluded['E'][0]>0);ck(excluded['S'][1]<0)
ck(count==spec['case_count']);ck(time.perf_counter()-start<55)
result={'status':'PASS','boolean_cases':count,'extra_strict_improvement_control':1,'excluded_nonboolean_controls':1,'profiles_reconstructed':profiles,'assertions':checks,'runtime_seconds':time.perf_counter()-start,'bent_controls':bent,'compositions':compositions,'strict_improvement_KL_flat_outward_80bit':compact(strict['Kflat']),'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'exact rational spectra/reference distributions and rigorous log intervals on frozen domain; displayed intervals rounded outward to rational 80-bit dyadics; analytic continuum/composition proof in PROOF.md, not a formal or independent review of new refinement'}
(OUT/'checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('status','boolean_cases','profiles_reconstructed','assertions','runtime_seconds')}))
