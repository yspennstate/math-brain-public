import numpy as np,math,json,pathlib
from scipy.special import gammaln
ks=np.arange(2,100001,dtype=float)
def h(x):return 2*x*np.exp(gammaln(2*x+1)-2*gammaln(x+1)-x*math.log(4))
nu=1/(4*(ks-1)**2-1)
rows=[]
for ell in [1,5,100]:
 b=nu*h(ell+ks-1)/h(float(ell))
 A=1/(2*math.sqrt(math.pi)*h(float(ell)))
 rows.append({'ell':ell,'coefficient':A,'tail_coefficient_at_100000':float(b[-1]*ks[-1]**1.5),'degree_first_moment_truncated_100000':float(np.sum(2*ks*b)),'first_moment_divided_by_sqrt_cutoff':float(np.sum(2*ks*b)/math.sqrt(100000)),'asymptotic_first_moment_coefficient':4*A})
result={'scope':'source type-2 new-face law conditional on perimeter; not SRW simulation','rows':rows}
pathlib.Path('discovery_tail_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
