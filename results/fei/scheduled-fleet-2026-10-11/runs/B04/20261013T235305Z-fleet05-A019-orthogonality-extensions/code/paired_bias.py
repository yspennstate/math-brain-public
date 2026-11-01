import json,math,time,hashlib
from fractions import Fraction as Q
from pathlib import Path
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'A019-paired-bias-v1','family':'independent zero-mean two-point posterior-bias laws; relaxation only, Boolean realization not asserted','domain':'support values +a,-b with a,b in {1,3/5,4/5,5/13,12/13,7/25,24/25,8/17,15/17}; 81 laws, ordered pairs','case_count':6561,'symmetry':'none','arithmetic':'double discovery ranking only; worst/minimum and every negative-margin case followed by exact Fraction log interval','memory_estimate_MB':30,'maximum_runtime_seconds':60}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2))
started=time.monotonic()
values=[(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(4,5),Q(3,5)),(Q(5,13),Q(12,13)),(Q(12,13),Q(5,13)),(Q(7,25),Q(24,25)),(Q(24,25),Q(7,25)),(Q(8,17),Q(15,17)),(Q(15,17),Q(8,17))]
laws=[]
for a,ra in values:
 for b,rb in values:laws.append([(a,ra,b/(a+b)),(-b,rb,a/(a+b))])
def hb(t):
 if t in (0,1):return 0.
 return -t*math.log2(t)-(1-t)*math.log2(1-t)
def ef(r):return hb(float((1+r)/2))
best=(1e10,None);negative=[];cases=0
for i,L in enumerate(laws):
 for j,M in enumerate(laws):
  cases+=1
  v=sum(float(w)*ef(r) for u,r,w in L)+sum(float(w)*ef(r) for u,r,w in M)
  for u,ru,wu in L:
   for z,rz,wz in M:
    a=1+u*z
    if a:v+=float(wu*wz*a)*(math.log2(float(a))-ef(ru*rz/a))
  if v<best[0]:best=(v,(i,j))
  if v< -1e-12:negative.append((i,j))
def lnunit(x):
 z=(x-1)/(x+1);n=60
 s=sum((2*z**(2*k+1)/Q(2*k+1) for k in range(n)),Q(0))
 e=2*z**(2*n+1)/((2*n+1)*(1-z*z));return s,s+e
l2,u2=lnunit(Q(2))
def log(x):
 k=x.numerator.bit_length()-x.denominator.bit_length()
 t=x/(2**k if k>=0 else Q(1,2**(-k)))
 if t<1:k-=1;t*=2
 if t>=2:k+=1;t/=2
 l,u=lnunit(t);return Q(k)+l/u2,Q(k)+u/l2
def exact_expr(i,j):
 terms={}
 def term(w,x):
  if x and w:terms[x]=terms.get(x,Q(0))+w
 def entropy(w,r):
  p=(1+r)/2
  term(-w*p,p);term(-w*(1-p),1-p)
 L,M=laws[i],laws[j]
 for u,r,w in L:entropy(w,r)
 for u,r,w in M:entropy(w,r)
 for u,ru,wu in L:
  for z,rz,wz in M:
   a=1+u*z
   if a:term(wu*wz*a,a);entropy(-wu*wz*a,ru*rz/a)
 return {x:w for x,w in terms.items() if w}
cert=[]
for i,j in sorted(set(negative+[best[1]])):
 terms=exact_expr(i,j);lo=hi=Q(0)
 for x,w in terms.items():
  l,u=log(x);lo+=w*(l if w>=0 else u);hi+=w*(u if w>=0 else l)
 cert.append({'law_ids':[i,j],'laws':[[[str(u),str(r),str(w)] for u,r,w in laws[k]] for k in (i,j)],'gap_interval':[str(lo),str(hi)],'sign':'NEGATIVE' if hi<0 else 'NONNEGATIVE' if lo>=0 else 'INCONCLUSIVE','terms':[[str(x),str(w)] for x,w in terms.items()]})
out={'status':'DISCOVERY_COMPLETED_WITH_SELECTED_EXACT_CERTIFICATES','cases':cases,'minimum_float_evidence':best[0],'negative_float_case_count':len(negative),'certificates':cert,'runtime_seconds':time.monotonic()-started,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'Boolean_realization':'NOT_ASSERTED'}
(R/'out/BIAS_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('status','cases','minimum_float_evidence','negative_float_case_count','runtime_seconds')}));print('Exact selected signs:',[(z['law_ids'],z['sign']) for z in cert])
