from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve

def configs(n,counts):
 for a in combinations(range(n),counts[0]):
  rem=[i for i in range(n) if i not in a]
  for b in combinations(rem,counts[1]):yield tuple(1 if i in a else 2 if i in b else 3 for i in range(n))

def ring_queue(n,k1,k2):
 states=list(configs(n,(k1,k2))); weights={s:0 for s in states}
 for aa in combinations(range(n),k1):
  A=[int(i in aa) for i in range(n)]
  for ss in combinations(range(n),k1+k2):
   S=[int(i in ss) for i in range(n)]
   Q=[max([0]+[sum(A[(i-j)%n]-S[(i-j)%n] for j in range(k)) for k in range(1,n+1)]) for i in range(n)]
   U=[int(S[i] and not A[i] and Q[(i-1)%n]==0) for i in range(n)]
   state=tuple(2 if U[i] else 1 if S[i] else 3 for i in range(n)); weights[state]+=1
 total=sum(weights.values()); pi=[F(weights[s],total) for s in states]
 # Martin orientation: decreasing adjacent pair swaps at rate 1.
 balance=[F(0) for s in states]; ids={s:i for i,s in enumerate(states)}
 for idx,s in enumerate(states):
  for i in range(n):
   j=(i+1)%n
   if s[i]>s[j]:
    t=list(s);t[i],t[j]=t[j],t[i];t=tuple(t)
    balance[idx]-=pi[idx];balance[ids[t]]+=pi[idx]
 assert not any(balance),(n,k1,k2,'stationarity failed')
 cov=[sum(pi[i]*int(s[0]==2)*int(s[d]==2) for i,s in enumerate(states))-F(k2,n)**2 for d in range(n)]
 assert sum(cov)==0
 return {'N':n,'counts':[k1,k2,n-k1-k2],'states':len(states),'stationarity_exact':True,'C22':[str(x) for x in cov], 'nonuniform':len(set(pi))>1}

def infinite(a,b,theta):
 p=a*(1-b); q=(1-a)*b; r=p/q; delta=b-a; K=160
 pi=np.zeros(K);pi[0]=1
 for k in range(1,K):pi[k]=pi[k-1]*r/(1-theta**k)
 pi/=sum(pi)
 P=np.zeros((K,K))
 for k in range(K):
  if k<K-1:P[k,k+1]=p
  if k>0:P[k,k-1]=q*(1-theta**k)
  P[k,k]=1-sum(P[k])
 f=np.array([theta**k for k in range(K)]) # 0**0=1
 assert abs(q*pi@f-delta)<1e-12
 U=np.diag(q*f)
 g=f.copy(); cs=[]; integral_errors=[]
 h=1-p-q;t=math.sqrt(p*q);lo=h-2*t;hi=h+2*t
 for n in range(1,31):
  c=q*q*(pi*f)@g-delta*delta
  direct=pi@U@np.linalg.matrix_power(P,n-1)@U@np.ones(K)-delta**2
  assert abs(c-direct)<1e-12
  if theta==0:
   val=delta/(2*math.pi)*quad(lambda x:x**(n-1)*math.sqrt(max(0,4*p*q-(x-h)**2))/(1-x),lo,hi,epsabs=1e-13)[0]
   integral_errors.append(abs(c-val));assert abs(c-val)<1e-11
  cs.append(c);g=P@g
 L=math.prod(1-theta**j for j in range(1,1000));gap=L*q*(1-math.sqrt(r))**2
 var=pi@(f*f)-(pi@f)**2
 assert all(-1e-13<=c<=q*q*var*(1-gap)**i+1e-12 for i,c in enumerate(cs))
 # Poisson-equation and integrated-covariance checks, independent of quadrature.
 fc=f-pi@f
 Q=np.arange(K,dtype=float)
 solution=solve(np.eye(K)-P+np.outer(np.ones(K),pi),fc)
 integral=q*q*(pi*fc)@solution
 poisson_error=np.max(np.abs((np.eye(K)-P)@(-Q/q)-fc)[:K-1])
 assert abs(integral-p)<1e-11
 assert abs(-q*(pi@(f*Q)-(pi@f)*(pi@Q))-p)<1e-12
 assert poisson_error<1e-12
 return {'a':a,'b':b,'theta':theta,'max_integral_error':max(integral_errors,default=None),'C22_first5':cs[:5],'proved_gap_bound':gap,'integrated_positive_lags':integral,'exact_value_p':p,'poisson_error_below_truncation_boundary':poisson_error}

out={'ring':[ring_queue(n,k1,k2) for n,k1,k2 in [(3,1,1),(4,1,1),(5,2,1),(6,2,2),(7,2,2)]],
     'infinite':[infinite(.3,.6,t) for t in [0,.2,.7]],'scaling':[]}
for delta in [.1,.05,.025,.0125]:
 a=.5;b=a+delta;p=a*(1-b);q=(1-a)*b;h=1-p-q;t=math.sqrt(p*q);lo=h-2*t;hi=h+2*t
 n=round(delta**-2); beta=(1-hi)/delta**2
 # Change variables away from the shrinking spectral edge.
 val=math.sqrt(t)/math.pi*quad(lambda z: math.sqrt(z)*math.sqrt(max(0,1-delta**2*z/(4*t)))/(beta+z)*max(0,hi-delta**2*z)**(n-1),0,min((hi-lo)/delta**2,80),epsabs=1e-10)[0]
 limit=quad(lambda z:math.sqrt(z)/(1+z)*math.exp(-1-z),0,np.inf)[0]/(2*math.pi)
 out['scaling'].append({'delta':delta,'n':n,'C22_over_delta2':val,'limit_s1':limit})
Path('verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
