import pathlib,json,math
import numpy as np
from scipy.optimize import linprog
P=pathlib.Path(__file__).resolve().parent
ns={'__file__':str(P/'finite_search.py')}
exec((P/'finite_search.py').read_text().split('records=[];')[0],ns)
records=[]
for n in [2,3,5,7,8]:
 A=ns['setup'](n)
 for a,c in [(0,.7),(.7,0),(.2,1),(1,.2),(0,1),(1,0),(.35,.8),(.8,.35)]:
  Q=a*np.eye(n)+(c-a)*np.ones((n,n))/n
  for side,M,x,y in [('lower',Q,a,c),('complement_lower',np.eye(n)-Q,1-a,1-c)]:
   p=(x**(n-1)*y)**(1/n)
   mu=ns['law'](M)
   nu=np.array([p**s.bit_count()*(1-p)**(n-s.bit_count()) for s in range(1<<n)])
   z=linprog(mu-nu,A_ub=A,b_ub=np.zeros(A.shape[0]),bounds=(0,1),method='highs')
   assert z.success and z.fun>=-1e-8
   records.append({'n':n,'a':a,'c':c,'side':side,'density':p,'gap':float(z.fun)})
P.joinpath('boundary_results.json').write_text(json.dumps(records,indent=2))
print('EXCHANGEABLE_ENDPOINT_CHECK_PASS',len(records),'all-event comparisons')
rng=np.random.default_rng(3636);gaps=[]
for n in [2,3,6,12,20]:
 for trial in range(60):
  lam=rng.uniform(.0001,.9999,n)
  if trial%4==0:lam[0]=0
  if trial%4==1:lam[-1]=1
  for vals in [lam,1-lam]:
   p=float(np.prod(vals)**(1/n));pmf=np.array([1.])
   for v in vals:pmf=np.convolve(pmf,[1-v,v])
   binpmf=np.array([math.comb(n,k)*p**k*(1-p)**(n-k) for k in range(n+1)])
   gap=np.cumsum(pmf[::-1])-np.cumsum(binpmf[::-1])
   assert gap.min()>=-1e-11;gaps.append(float(gap.min()))
P.joinpath('count_boundary_results.json').write_text(json.dumps({'comparisons':len(gaps),'min_gap':min(gaps),'seed':3636},indent=2))
print('COUNT_ENDPOINT_CHECK_PASS',len(gaps),'count-law comparisons','worst gap',min(gaps))
