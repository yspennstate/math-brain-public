from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x
spec={'helper_version':'standalone literal character/physical-edge reconstruction1; no producer imports','family':'three-negative-point selector pair','domain':{'r':[4,5],'m_rational_endpoints':[4,5,6,7,8,9,10,11,12,13,14,15,16]},'case_count':15,'symmetry':'none','arithmetic':'integers and Fraction only; no logarithmic sign tests','memory_estimate_MB':25,'max_runtime_seconds':30}
(R/'REPRODUCTION_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
rows=[]
for r in [4,5]:
 d=F(1,1<<r);truth=[-1 if (x>>1) in ({0,3,5} if x&1 else {0,1,3}) else 1 for x in range(1<<(r+1))]
 def walsh(t):return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t))]
 W=walsh(truth);ck(W[-1]==2*d);ck(W[0]==1-6*d)
 I=F(sum(truth[x]!=truth[x^(1<<j)] for x in range(len(truth)) for j in range(r+1)),len(truth));ck(I==(6*r-2)*d)
 neg=[x for x,v in enumerate(truth) if v<0];ck(len(neg)==6);ck(sum((x^y).bit_count()==1 for i,x in enumerate(neg) for y in neg[i+1:])==4)
 for b in [0,1]:
  t=truth[b::2];w=walsh(t);ck(all(w));ck(w[-1]==(-2*d if b==0 else -6*d));ck(w[0]==1-6*d)
  for v in w:ck(v!=0)
 a=F(1,6);ck(a*F(1,5)/(1-a+a*F(1,5))==F(1,26));ck(a*F(9,5)/(1-a+a*F(9,5))==F(9,34))
 rows.append({'r':r,'I':str(I),'full':str(W[-1]),'all_child_frequencies_nonzero':True})
for m in spec['domain']['m_rational_endpoints']:
 I=F(24*m-2,1<<m);lower=F(8*(1<<m),25);ck(F(12,1<<m)<=1)
 if m>=6:ck(lower>8*I)
 if m==6:ck(lower-8*I==F(273,100));ck((4*m+1)*(1<<(3*m))==6553600)
result={'status':'PASS','cases':15,'assertions':checks,'runtime_seconds':time.perf_counter()-start,'rows':rows,'all_dimensional_bridge':'proved Bernoulli/convexity/telescoping in PROOF.md, not extrapolation of these endpoints'}
(R/'out/REPRODUCTION.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
