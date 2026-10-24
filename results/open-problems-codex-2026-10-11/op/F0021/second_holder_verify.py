from pathlib import Path
import numpy as np, itertools,math,json,time
from scipy.special import logsumexp
p=Path('~/brain_workers/TRIO_1011/op/F0021');start=time.monotonic();rng=np.random.default_rng(21014)
n=8;paths=np.array(list(itertools.product([-1,1],repeat=n)));pos=np.cumsum(paths,axis=1);errs=[];cases=0
for rep in range(50):
 omega=rng.normal(0,1,(n,2*n+1));u=1.2;c=np.minimum(omega,u);delta=np.maximum(omega-u,0);eta=np.where(omega>u,omega,0)
 hs=[a[np.arange(n)[None,:],pos+n].sum(axis=1) for a in [omega,c,delta,eta]]
 def F(h,t):return float(logsumexp(t*h)-n*math.log(2))
 beta=1.3;fo=F(hs[0],beta);fc=F(hs[1],beta)
 for pp in [1.001,1.05,1.5,2.]:
  hh=pp/(pp-1);temp=F(hs[1],pp*beta)/pp-fc;bound=n*math.log(2)*(1-1/pp)
  assert -1e-10<=temp<=bound+1e-10
  holder=F(hs[1],pp*beta)/pp+F(hs[2],hh*beta)/hh
  assert fo<=holder+1e-10
  assert 0<=fo-fc<=bound+F(hs[3],hh*beta)/hh+1e-10
  cases+=1
 for t in [.2,1.,3.]:
  logmu=t*hs[1]-float(logsumexp(t*hs[1]));mu=np.exp(logmu)
  D=float(np.dot(mu,logmu+n*math.log(2)));ident=t*float(np.dot(mu,hs[1]))-F(hs[1],t)
  errs.append(abs(D-ident));assert 0<=D<=n*math.log(2)+1e-10
z={'seed':21014,'finite_holder_and_temperature_cases_passed':cases,'relative_entropy_identity_max_error':max(errs),'elapsed_seconds':time.monotonic()-start}
alpha=5.5;r=2.5;m=.5*(alpha/(alpha-1)-r/(r-1));s2=.5*(alpha/(alpha-2)+r/(r-2))-m*m;s=math.sqrt(s2)
z['admissible_mixture']={'right_alpha':alpha,'negative_exponent':r,'mean_before_standardizing':m,'variance_before_standardizing':s2,'right_tail_ratio_at_t_10000':((2*s*10000+m)/(s*10000+m))**(-alpha),'limiting_right_tail_ratio':2**(-alpha),'negative_third_moment_truncated_at_1e8':r*((1e8)**(3-r)-1)/(3-r)}
p.joinpath('SECOND_HOLDER_CHECKS.json').write_text(json.dumps(z,indent=2),encoding='utf-8');print(json.dumps(z,indent=2))
