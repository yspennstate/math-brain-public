from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time
import arithmetic as A
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v;checks+=1
 if time.perf_counter()-start>58:raise RuntimeError('Frozen pilot watchdog')
A.log=lru_cache(None)(A.log)
@lru_cache(None)
def ent(p):return A.entropy(p)
def H(p):return ent(tuple(sorted(x for x in p if x)))
def sub(a,b):return A.add(a,A.mul(-1,b))
def phi(a,b):return sub(H((a,b)),H((a+b,)))
@lru_cache(None)
def spectrum(t):
 a=tuple(A.walsh(t));return a,tuple(x*x for x in a)
def influences(t):return tuple(Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(len(t).bit_length()-1))
def I(t):return sum(influences(t),Q(0))
@lru_cache(None)
def bounds(form):return A.bounds(dict(form))
def interval(form):return bounds(tuple(sorted(form.items()))) if form else (Q(0),Q(0))
def encode(form):return {str(k):str(v) for k,v in form.items()}
lnlo,lnhi=A.ln_interval(Q(2));A0lo=2/lnhi-2;A0hi=2/lnlo-2
results=[];counterexamples=[];hist={};count=0;maximum=None
def pair(b,v,label):
 global count,maximum
 n=len(b).bit_length()-1;delta=Q(1,len(b));ck(b[v]==1)
 c=tuple(-x if j==v else x for j,x in enumerate(b));ab,pb=spectrum(b);ac,pc=spectrum(c)
 Ib=I(b);Ic=I(c);k=sum(b[v]!=b[v^(1<<i)] for i in range(n))
 ck(Ic==Ib+2*delta*(n-2*k))
 signs=tuple((-1)**(s&v).bit_count() for s in range(len(b)))
 ck(all(ac[s]==ab[s]-2*delta*signs[s] for s in range(len(b))))
 g=tuple(b[x>>1] if not x&1 else c[x>>1] for x in range(2*len(b)))
 ag,pg=spectrum(g);ck(influences(g)[0]==delta)
 ck(I(g)==(Ib+Ic)/2+delta)
 Qbank=A.add(*(phi((ab[s]-delta*signs[s])**2,delta**2) for s in range(len(b))))
 direct=A.add(*(phi(pg[s],pg[s|1]) for s in range(len(pg)) if not s&1));ck(Qbank==direct)
 hb=H(pb);hc=H(pc);S4=sub({2:2*(Ib+Ic)},A.mul(Q(1,2),A.add(hb,hc)))
 baseS4=sub({2:4*Ib},hb)
 ck(S4==A.add(baseS4,{2:4*delta*(n-2*k)},A.mul(Q(-1,2),sub(hc,hb))))
 allowance=A.mul(1/delta,sub(Qbank,S4));lo,hi=interval(allowance)
 sb=interval(baseS4);sc=interval(sub({2:4*Ic},hc));childcert=sb[0]>=0 and sc[0]>=0
 if label=='exhaustive':
  count+=1;key='destroyed' if 2*k>n else 'neutral' if 2*k==n else 'created';hist[key]=hist.get(key,0)+1
  if maximum is None or lo>maximum['upper']:
   maximum={'n':n,'mask':sum((1<<x) for x in range(len(b)) if b[x]==1),'vertex':v,'incident_pivots':k,'allowance_log_form':encode(allowance),'lower':lo,'upper':hi,'children_K4_certified':childcert}
  elif hi>maximum['lower'] and allowance!= {int(x):Q(y) for x,y in maximum['allowance_log_form'].items()}:
   raise AssertionError('Maximum not resolved by frozen rigorous intervals')
  if hi>A0lo:
   ck(lo>A0hi);counterexamples.append({'n':n,'vertex':v,'mask':sum((1<<x) for x in range(len(b)) if b[x]==1),'k':k,'allowance_log_form':encode(allowance),'children_K4_certified':childcert})
  ck(childcert)
 rec={'label':label,'n':n,'vertex':v,'incident_pivots':k,'delta':str(delta),'I_b':str(Ib),'I_c':str(Ic),'B_shadow':encode(Qbank),'terminal_S4':encode(S4),'allowance':encode(allowance),'children_K4_certified':childcert,'entropy_change':encode(sub(hc,hb))}
 return rec,Qbank,S4,allowance
for n in (1,2,3):
 for mask in range(1<<(1<<n)):
  b=tuple(1 if mask>>x&1 else -1 for x in range(1<<n))
  for v in range(1<<n):
   if b[v]==1:pair(b,v,'exhaustive')
ck(count==1060)
maxout=dict(maximum);maxout['lower']=str(maxout['lower']);maxout['upper']=str(maxout['upper'])
(R/'out/SMALL_EDIT_CERTIFICATE.json').write_text(json.dumps({'status':'PASS','pairs':count,'edge_regimes':hist,'maximum':maxout,'A003_point_allowance_counterexamples':counterexamples},indent=2)+'\n',encoding='utf-8')
print('SMALL_EDIT_PASS',checks,flush=True)
for d in range(1,11):
 delta=Q(1,1<<d);b=(1,)+(-1,)*((1<<d)-1)
 rec,B,S,allow=pair(b,0,'point')
 ck(B==A.add(phi((1-delta)**2,delta**2),{2:2*delta*(1-delta)}))
 eta=H(((1-2*delta)**2,))
 ck(S==A.add({2:4*delta+4*(d-1)*delta*delta},A.mul(Q(-1,2),eta)))
 # Enclose source's complete quadratic correction, not just the limiting allowance.
 factor=2*delta-3*delta*delta;upper=factor/lnhi-2*delta+(2-2*d)*delta*delta
 ck(interval(sub(B,S))[1]<upper)
 ck(interval(allow)[1]<A0lo)
 # Direct independent physical terminal tensor q=x, H(q)=0,I(q)=1.
 bq=tuple(b[x>>1]*(1 if not x&1 else -1) for x in range(2*len(b)))
 cq=tuple(-1*(1 if not x&1 else -1) for x in range(2*len(b)))
 Aq=(tuple(Q(bq[x]+cq[x],2) for x in range(len(bq))))
 Dq=(tuple(Q(bq[x]-cq[x],2) for x in range(len(bq))))
 aq=A.walsh(Aq);dq=A.walsh(Dq)
 ck(A.add(*(phi(a*a,e*e) for a,e in zip(aq,dq)))==B)
 Snew=sub({2:2*(I(bq)+I(cq))},A.mul(Q(1,2),A.add(H(spectrum(bq)[1]),H(spectrum(cq)[1]))))
 ck(Snew==A.add(S,{2:4}))
 results.append(rec)
 (R/'out/POINT_CHECKPOINT.json').write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8')
for dummy in (1,2,3):
 n=3+dummy;b=tuple(1 if not x&7 else -1 for x in range(1<<n))
 rec,B,S,allow=pair(b,0,'padded_AND3');ck(rec['incident_pivots']==3)
 if dummy==3:ck(rec['I_b']==rec['I_c']);ck(rec['entropy_change'])
 results.append(rec)
(R/'out/ENDPOINTS.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
out={'helper_version':'A004-point-edit-ledger-v1','status':'PASS','assertions':checks,'exhaustive_pairs':count,'point_pairs':10,'tensor_checks':10,'padded_AND3_pairs':3,'counterexamples_to_A0_in_small_domain':len(counterexamples),'runtime_seconds':time.perf_counter()-start}
(R/'out/VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out),flush=True)
