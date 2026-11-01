import mpmath as m,json,math
from pathlib import Path
m.mp.dps=25
out={'ground_state':[],'N2_variance':[],'convex_example':[]}
def g(s,x):return m.zeta(s,x)+m.zeta(s,1-x)
for s in [.2,.5,.8]:
 for n in [2,3,5,10]:
  direct=n**(1-s)*sum(g(s,m.mpf(k)/n) for k in range(1,n))
  formula=2*m.zeta(s)*(n-n**(1-s))
  out['ground_state'].append(dict(s=s,N=n,direct=float(direct),formula=float(formula),error=float(abs(direct-formula))))
 for beta in [.25,1,4]:
  def h(x):return 2*2**(-s)*g(s,x)
  emin=h(m.mpf('.5'))
  vals=[m.quad(lambda x,k=k:(h(x)-emin)**k*m.exp(-beta*(h(x)-emin)),[0,.05,.2,.5,.8,.95,1]) for k in range(3)]
  var=vals[2]/vals[0]-(vals[1]/vals[0])**2
  out['N2_variance'].append(dict(s=s,beta=beta,variance=float(var),bound=1/beta**2,ratio=float(beta**2*var)))
for n in [10,50,200]:
 for beta in [.3,.5,.7]:
  # Radial integral normalized by volume of the ball of radius sqrt(n).
  inner=m.exp(-beta*n)
  outer=(m.mpf(n)/2)*(beta*n)**(-m.mpf(n)/2)*m.gammainc(m.mpf(n)/2,beta*n,m.inf)
  p=m.log(inner+outer)/n
  lim=-(1+m.log(2*beta))/2 if beta<.5 else -beta
  out['convex_example'].append(dict(N=n,beta=beta,pressure=float(p),limit=float(lim),error=float(p-lim)))
Path('numerics.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('Maximum ground-state formula error:',max(x['error'] for x in out['ground_state']))
print('N=2 beta^2 variance range:',min(x['ratio'] for x in out['N2_variance']),max(x['ratio'] for x in out['N2_variance']))
for x in out['convex_example']:print(x)
