from pathlib import Path
import math,json
extra=[]
cases={'singleton':[0],'two_point':[0,3],'flat_interval':[0]*100,'one_sided_linear':[0.03*k for k in range(1000)],'asymmetric_linear':[3*(-k) if k<0 else .1*k for k in range(-50,500)]}
for name,w in cases.items():
 z=sum(math.exp(-t) for t in w);ratio=sum(math.exp(-t/2) for t in w)/z;e=sum(t*math.exp(-t) for t in w)/z
 assert ratio<=3+1e-12 and e<=2*math.log(3)+1e-12
 extra.append({'case':name,'ratio':ratio,'expected_excess':e})
domain=list(range(-30,13))
def V(k):return k*k if k<0 else math.exp(k)
tilt=[]
for lam in [-10,-1,0,1,10,100]:
 energies={k:V(k)-lam*k for k in domain};mn=min(energies.values());w={k:math.exp(-(energies[k]-mn)) for k in domain};z=sum(w.values());p={k:w[k]/z for k in domain}
 error=0
 for S in [-10,-3,0,3,10]:
  splits=[k for k in domain if S-k in p];u=[p[k]*p[S-k] for k in splits];zu=sum(u)
  g=[V(k)+V(S-k) for k in splits];mg=min(g);q=[math.exp(-(t-mg)) for t in g];zq=sum(q)
  if zu>1e-290:error=max(error,max(abs(a/zu-b/zq) for a,b in zip(u,q)))
 assert error<1e-12
 tilt.append({'lambda':lam,'finite_domain_mean':sum(k*p[k] for k in domain),'finite_domain_expected_V':sum(V(k)*p[k] for k in domain),'max_bridge_probability_difference':error})
p=Path('heatbath_experiment_results.json');j=json.loads(p.read_text());j['explicit_boundary_cases']=extra;j['asymmetric_tilt_checks']=tilt;p.write_text(json.dumps(j,indent=2),encoding='utf-8')
print('Extra boundary and asymmetric-tilt checks passed.');print(json.dumps(extra+tilt,indent=2))
