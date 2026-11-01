from fractions import Fraction as F
import json, pathlib, random, math, time
out={}
graphs={'cycle4':[(i,(i+1)%4) for i in range(4)],'cube3':[(i,i^(1<<k)) for i in range(8) for k in range(3) if i<(i^(1<<k))]}
for name,edges in graphs.items():
 n=max(max(e) for e in edges)+1; degree=sum(0 in e for e in edges); arrows=[(x,y) for e in edges for x,y in [e,e[::-1]]]
 for b in [F(1,7),F(1),F(3)]:
  p=b/(1+b); weights=[p**s.bit_count()*(1-p)**(n-s.bit_count()) for s in range(1<<n)]
  for model in ['CBRW','Ising']:
   rows=[{} for _ in weights]
   for s in range(1<<n):
    for x,y in arrows:
     if not (s>>x)&1:continue
     if model=='CBRW':
      t=(s&~(1<<x))|(1<<y); rows[s][t]=rows[s].get(t,F(0))+F(1,degree)
      if not (s>>y)&1:
       t=s|(1<<y);rows[s][t]=rows[s].get(t,F(0))+b/degree
     else:
      t=s^(1<<y); rate=1-p if (s>>y)&1 else p;rows[s][t]=rows[s].get(t,F(0))+rate
   checked=0
   for s,row in enumerate(rows):
    for t,rate in row.items():
     if t==s:continue
     assert weights[s]*rate==weights[t]*rows[t].get(s,F(0)),(name,b,model,s,t)
     checked+=1
   out[f'{name}/{model}/beta={b}']={'exact_detailed_balance_pairs':checked,'passed':True}
try:
 import scipy.integrate as si
 import scipy.special as ss
 g,err=si.quad(lambda t:float(ss.i0e(t/3))**3,0,math.inf,epsabs=1e-9)
 out['green3_quadrature']={'G':g,'q':1/g,'quadrature_error_estimate':err,'rigorous':False}
 q=1/g
except ImportError:q=0.659462670
rng=random.Random(21220261011)
def pair_trial(L):
 pos=[1,0,0];t=0.
 while True:
  t+=rng.expovariate(2)
  if t>L:return L,True
  axis=rng.randrange(3);pos[axis]+=1 if rng.randrange(2) else -1
  if pos==[0,0,0]:return t,False
for beta in [.1,.03,.01,.003]:
 L=beta**(-2/3);N=3000;times=[];attempts=0;successes=0
 for _ in range(N):
  t=0.
  while True:
   t+=rng.expovariate(beta);u,ok=pair_trial(L);attempts+=1
   if ok:successes+=1;times.append(beta*q*t);break
   t+=u
 out[f'renewal/beta={beta}']={'L':L,'N':N,'qL_estimate':successes/attempts,'scaled_mean':sum(times)/N,'cdf_at_1':sum(t<=1 for t in times)/N,'Exp1_cdf_at_1':1-math.exp(-1),'is_actual_stationary_model':False}
pathlib.Path('checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
