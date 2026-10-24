"""Check the remaining quantitative bound in adverse pair-mean directions."""
import json,time
from pathlib import Path
import numpy as np
from explore_fourier_compensation import channel
C,bits=channel()

def counts(ps):
 p=np.array([1.])
 for q in ps:p=np.convolve(p,[1-q,q])
 return p

def evaluate(lam,velocity):
 c,d,u,v=velocity;slopes=np.array([c+u,d+v,c-u,d-v])
 inputp=np.prod(np.where(bits,lam,1-lam),axis=1);score=(bits-lam)/(lam*(1-lam))
 first=score@slopes;second=first**2-score**2@(slopes**2)
 p=C@inputp;dp=C@(inputp*first);ddp=C@(inputp*second)
 f=counts(lam);g=np.zeros(4);h=np.zeros(3)
 for i in range(4):
  g+=slopes[i]*counts(np.delete(lam,i))
  for j in range(4):
   if i!=j:h+=slopes[i]*slopes[j]*counts([lam[k] for k in range(4) if k not in [i,j]])
 P=p[3];O=p[5];ratio=np.log(O/P)
 al=np.log([p[1]**2/(p[0]*P),P*O/(p[1]*p[7]),p[7]**2/(p[15]*P)])
 be=np.log([16*P/f[2],f[2]**2/(16*P*O),16*P/f[2]])
 excess=8*(O*dp[3]-P*dp[5])**2/(P*O*f[2])
 boundary=g[0]**2/f[1]+g[3]**2/f[3]
 lower=excess+boundary+np.maximum(h,0)@be+np.maximum(-h,0)@al+4*c*d*ratio
 full=np.sum(dp*dp/p+ddp*np.log(p))
 return lower,full,4*c*d*ratio,dict(excess=excess,boundary=boundary,h=h.tolist(),alpha=al.tolist(),beta=be.tolist())

def main():
 rng=np.random.default_rng(9172);start=time.time();best=None;adverse=0;count=10000
 for k in range(count):
  lam=1/(1+np.exp(rng.uniform(-7,7,4)));velocity=rng.normal(size=4);velocity/=np.linalg.norm(velocity)
  lower,full,term,parts=evaluate(lam,velocity)
  if term>=0:continue
  adverse+=1
  if best is None or lower<best['bound']:
   best=dict(bound=lower,full_curvature=full,adverse_term=term,lambda_values=lam.tolist(),velocity=velocity.tolist(),components=parts)
 out=dict(status='numerical exploration only',generated=count,adverse_directions=adverse,worst=best,elapsed=time.time()-start)
 Path(__file__).with_name('fourier_adverse_exploration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
