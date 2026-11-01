"""A fixed already-frozen fixture; exact all-k ratio proved in review text."""
import review as r
import json,time
from fractions import Fraction as F
start=time.monotonic()
def credits(kind,k):
 g=r.core(kind,k);v,A,n=r.build(1,1,1,g);P,ds,H,TC,W=r.spectrum(v)
 v0,v1=r.halves(v,0);W0=r.fwht(v0);W1=r.fwht(v1);N=len(v0)
 packet=tuple(P[2*j]+P[2*j+1] for j in range(len(P)//2))
 B=r.add((1,H),(-1,r.ent(packet)));J=r.add((1,r.h(ds[0])),(-1,B));mu=F(0);minor={}
 for a,b,Q in zip(W0,W1,packet):
  m=F((abs(a)-abs(b))**2,4*N*N);mu+=m
  if m:minor=r.add((1,minor),(m,r.lv(Q/m)))
 credit=r.add((1,r.ent_atom(mu)),(-1,minor))
 r.check(r.bounds(J)[0]>0);r.check(r.bounds(credit)[0]>0)
 return {'posterior':J,'minor_KL_credit':credit,'minor_KL_divergence':r.add((1/mu,credit)),'minority_mass':mu,'H':H,'I':sum(ds)}
base=credits('dictator',0)
for k in [2,4]:
 row=credits('bent',k)
 for s in ['posterior','minor_KL_credit','minor_KL_divergence','minority_mass']:r.check(row[s]==base[s])
 r.check(not r.add((1,row['H']),(-1,base['H']),(-F(7*k,16),{2:F(1)})))
 r.check(row['I']==F(3,4)+F(7,16)*(1+F(k,2)))
result={'status':'PASS','checks':r.CHECKS,'runtime_seconds':time.monotonic()-start,'fixture':'L=R=T=1; pi=7/16; g_k=z*b_k even k>=2',
 'minority_mass':str(base['minority_mass']),'posterior':r.packed(base['posterior']),'minor_KL_credit':r.packed(base['minor_KL_credit']),
 'minor_KL_divergence':r.packed(base['minor_KL_divergence']),
 'posterior_over_terminal_entropy_times_k':r.packed(r.add((F(16,7),base['posterior']))),
 'minor_KL_credit_over_terminal_entropy_times_k':r.packed(r.add((F(16,7),base['minor_KL_credit']))),
 'minor_KL_divergence_over_terminal_entropy_times_k':r.packed(r.add((F(16,7),base['minor_KL_divergence']))),
 'root_entropy_constant':r.packed(base['H']),
 'exact_all_k':'H(F_k)=H(F_dictator)+(7/16)k; I(F_k)=3/4+(7/16)(1+k/2). Each listed positive credit is independent of k. Its ratio to retained terminal entropy equals (16/7)*credit/k.',
 'limitation':'Only the named root posterior and complete minority KL terms are covered. No claim that total correlation or arbitrary reference divergence is small.'}
(r.ROOT/'out'/'CREDIT_FIXTURE.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({s:result[s] for s in ['status','checks','runtime_seconds','minority_mass']}))
