from fractions import Fraction as F
from math import comb,log,sqrt
import json
import numpy as np
from scipy.special import gammaln
from scipy.integrate import quad

def d(k):return F(comb(2*k,k),4**k)
def h(k):return 2*k*d(k)
exact_rows=0
for atoms in [{1:F(1)},{7:F(1)},{1:F(1,3),5:F(2,3)},{2:F(1,5),13:F(4,5)}]:
 # atoms specify k*a_k, k=m+1; q_1=0.
 a={m:c/F(m+1) for m,c in atoms.items()}
 Z=1/(1-sum(a.values()))
 pos={m:a[m]*F(m+1,2*m+1)/d(m) for m in a}
 def neg(k):return d(k)/F(2*k-1)*sum(F(m*(2*m+1))*d(m)*pos[m]/F(m+k) for m in a)
 for k in range(1,21):
  integral=Z*sum(F(m+1)*a[m]*(F(1,k)-F(1,k+m)) for m in a)
  independent=F(1,2)/Z*d(k-1)*integral
  assert independent==neg(k)
 for p in range(1,17):
  row=sum(v*h(p+m)/h(p) for m,v in pos.items())+sum(neg(k)*h(p-k)/h(p) for k in range(1,p))
  assert row==1,(atoms,p,row)
  delta=1-sum(pos.values())-sum(neg(k) for k in range(1,p))
  recip=sum(v*(h(p+m)/h(p)-1) for m,v in pos.items())+sum(neg(k)*(h(p-k)/h(p)-1) for k in range(1,p))
  assert delta==recip and delta>0
  exact_rows+=1
for j in range(1,30):assert h(j+1)/h(j)==1+F(1,2*j)
for p in range(8,101):
 for t in range(1,2*p):
  dist=min(t,2*p-t)
  for k in range((p+1)//2,p-1):assert dist<2*k+1

def df(k):
 k=np.asarray(k,dtype=float)
 return np.exp(gammaln(k+.5)-gammaln(k+1)-.5*np.log(np.pi))
rows=[]
for atomlist in [[(1,1.)],[(31,1.)],[(1000000,1.)],[(1,.1),(17,.2),(4096,.3),(1000000,.4)]]:
 ms=np.array([x[0] for x in atomlist],float); coeff=np.array([x[1] for x in atomlist],float)
 pos=coeff/( (2*ms+1)*df(ms))
 w=ms*(2*ms+1)*df(ms)*pos
 for p in [1,2,3,8,16,63,256,1024,4096]:
  ks=np.arange(1,p,dtype=float)
  neg=df(ks)/(2*ks-1)*np.sum(w[None,:]/(ks[:,None]+ms[None,:]),axis=1)
  h0=2*p*df(p); yp=p+ms; yn=p-ks
  kp=pos*(2*yp*df(yp))/h0; kn=neg*(2*yn*df(yn))/h0
  R=np.sum(w/(ms+p))/sqrt(p)
  dp=np.log(2*yp*df(yp)/h0)*(ms<=p/2)
  dn=np.log(2*yn*df(yn)/h0)*(ks<=p/2)
  norm=float(sum(kp)+sum(kn))
  rows.append({'atoms':atomlist,'p':p,'normalization_error':abs(norm-1),'big_over_R':float((sum(kp[ms>p/2])+sum(kn[ks>p/2]))/R),'drift_over_R':float(abs(sum(kp*dp)+sum(kn*dn))/R),'variance_over_R':float((sum(kp*dp**2)+sum(kn*dn**2))/R),'b_over_R':float(.5*sum(kn[ks>=(p+1)//2])/R)})
  assert abs(norm-1)<2e-8
out={'exact_rows':exact_rows,'exact_kernel_checks':80,'numeric_rows':len(rows),'max_normalization_error':max(r['normalization_error'] for r in rows),'max_big_over_R':max(r['big_over_R'] for r in rows),'max_drift_over_R':max(r['drift_over_R'] for r in rows),'max_variance_over_R':max(r['variance_over_R'] for r in rows),'min_b_over_R_p_ge_8':min(r['b_over_R'] for r in rows if r['p']>=8),'rows':rows}
import mpmath as mp
mp.mp.dps=45
C=1/(mp.zeta(3)-1); Z=(mp.zeta(3)-1)/(mp.zeta(3)-mp.zeta(4))
errors=[]
for j in [1,2,7,30]:
 val=Z*C*(-mp.zeta(3)/(j*(j+1))+mp.zeta(2)/j**2-mp.harmonic(j)/j**3)
 numeric=mp.quad(lambda r:r**j*Z*C*(mp.zeta(3)-mp.polylog(3,r)/r),[0,.5,1])
 errors.append(str(abs(val-numeric)))
out['zeta_integral_errors']=errors
open('checks.json','w',encoding='utf8').write(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
