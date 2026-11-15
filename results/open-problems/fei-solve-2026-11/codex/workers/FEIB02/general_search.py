"""Bounded coordinate/block ascent with exact integer derivative sums."""
from math import comb,log2,log1p,log
import random,json,time,argparse
from pathlib import Path
LN2=log(2)
class Evaluator:
 def __init__(self,n):
  self.n=n
  # <=2,003,001 binomial integers at n=2000, below 1 GiB by construction.
  self.cs=[]
  for m in range(n+1):
   c=[1]
   for t in range(m):c.append(c[-1]*(m-t)//(t+1))
   self.cs.append(c)
  self.estimate_bytes=sum(8+((x.bit_length()+7)//8)+32 for row in self.cs for x in row)
 def __call__(self,f):
  n=self.n;total=1<<n;J=2*n*sum(c for c,x,y in zip(self.cs[n-1],f,f[1:]) if x!=y)
  if not J:return {'A/I':0.,'B/I':0.,'Gamma/I':0.,'I':0.}
  den=total*J
  F0=sum(c*x for c,x in zip(self.cs[n],f))
  m=(total-abs(F0))//2;x=(2*m)/total
  factor=2/LN2 if x<1e-9 else (-2*(1-x)**2*log1p(-x)/(x*LN2) if x<1 else 0.)
  A=0.;B=(2*m)/J*factor;G=B/2;d=list(f)
  for k in range(1,n+1):
   d=[d[t]-d[t+1] for t in range(n-k+1)]
   F=L=Q=0
   for c,v in zip(self.cs[n-k],d):
    F+=c*v;L+=c*abs(v);Q+=c*v*v
   if not F:continue
   wI=(self.cs[n][k]*F*F)/den;lf=log2(abs(F));lq=log2(Q)
   A+=wI*(n+k-lq);B+=wI*(lq+n-k-2*lf);G+=wI*(log2(L)-lf)
  return {'A/I':A,'B/I':B,'Gamma/I':G,'I':(J/total if J/total else None),'I_log2':log2(J)-n,'I_is_positive':True}

def main():
 p=argparse.ArgumentParser();p.add_argument('--dimensions',nargs='+',type=int,default=[24,32,64,128,256,512,1000,1024,2000]);p.add_argument('--moves',type=int,default=32);a=p.parse_args()
 rng=random.Random(20261110)
 for n in a.dimensions:
  out=Path(f'hill_{n:04d}.json')
  if out.exists():continue
  start=time.monotonic();ev=Evaluator(n);records=[]
  for objective in ['B/I','Gamma/I']:
   # Start from thresholds, a Gaussian-scale oscillation, and an extrapolated census extremizer.
   th=json.loads(Path(f'thresholds_{n:04d}.json').read_text()) if Path(f'thresholds_{n:04d}.json').exists() else None
   r=th['maxima'][objective]['threshold'] if th else n//2
   seeds=[[1 if t<r else -1 for t in range(n+1)],
          [1 if int((t-n/2)/max(1,n**.5/2))%2==0 else -1 for t in range(n+1)]]
   cen=json.loads(Path('census_24.json').read_text())
   pattern=[1]+[-1 if cen['maxima'][objective]['mask']>>(t-1)&1 else 1 for t in range(1,25)]
   seeds.append([pattern[min(24,max(0,round(12+(t-n/2)*(24/n)**.5)))] for t in range(n+1)])
   scored=[(ev(f),f) for f in seeds];scored.sort(key=lambda p:p[0][objective],reverse=True)
   score,f=scored[0];initial=score.copy();history=[];evaluations=len(seeds)
   # Single-coordinate flips and short contiguous flips, chosen in the binomial bulk.
   # Finite proposal budget is recorded; no claim of a local or global optimum.
   for step in range(a.moves):
    j=max(0,min(n,int(round(rng.gauss(n/2,max(2,n**.5))))))
    width=1 if step%3 else max(1,int(round(rng.uniform(1,max(2,n**.5/3)))))
    lo=max(0,min(n-width+1,j));hi=min(n+1,lo+width)
    trial=f[:]
    for t in range(lo,hi):trial[t]*=-1
    v=ev(trial);evaluations+=1
    if v[objective]>score[objective]+1e-11:
     f=trial;score=v;history.append({'step':step,'flip':[lo,hi],'score':score[objective]})
   records.append({'objective':objective,'initial':initial,'final':score,'evaluations':evaluations,'accepted_moves':history,'value_vector':''.join('+' if x>0 else '-' for x in f)})
   print(n,objective,score,'evaluations',evaluations,flush=True)
  row={'n':n,'seed':20261110,'proposal_budget_per_objective':a.moves,'binomial_cache_estimate_bytes':ev.estimate_bytes,'wall_seconds':time.monotonic()-start,'searches':records}
  out.write_text(json.dumps(row,indent=2)+'\n')
if __name__=='__main__':main()
