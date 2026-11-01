"""Separate direct characters and physical edges; no Walsh transform for roots."""
from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1];START=time.monotonic();C=0
def ck(z):
 global C
 C+=1;assert z,C
 if time.monotonic()-START>55:raise RuntimeError('55s cap')
def coeff(f):
 N=len(f)
 return [F(sum(v*(-1 if (s&z).bit_count()%2 else 1) for z,v in enumerate(f)),N) for s in range(N)]
records=[]
for d,t in [(2,1),(3,1),(2,2)]:
 g=tuple((-1 if z==0 else 1) if d==3 else (-1)**((z&1)*((z>>1)&1)) for z in range(1<<d))
 ga=coeff(g);k=2;p=F(1,4);mu=F(sum(g),len(g));nu=mu**t
 h=[]
 for z in range(1<<(d*t)):
  a=1
  for j in range(t):a*=g[(z>>(d*j))%len(g)]
  h.append(a)
 ha=coeff(h)
 f=tuple(h[z>>k] if z%4==0 else 1 for z in range(1<<(d*t+k)))
 fa=coeff(f)
 for s,a in enumerate(fa):
  want=p*ha[s>>k] if s>>k else (-p*(1-nu) if s else 1-p*(1-nu))
  ck(a==want)
 physical=[F(sum(v!=f[z^(1<<j)] for z,v in enumerate(f)),len(f)) for j in range(d*t+k)]
 source=[F(sum(v!=g[z^(1<<j)] for z,v in enumerate(g)),len(g)) for j in range(d)]
 ck(sum(physical)==p*(t*sum(source)+k*(1-nu)))
 ck(F(sum((a-1)**2 for a in f),len(f))==2*p*(1-nu))
 # Each fixed finite spectral window consists of control-only labels here.
 for s in range(1,4):ck(fa[s]**2==p*p*(1-nu)**2<=4*p*p)
 for m in range(d*t+k+1):
  means=[F(sum(f[z+(y<<m)] for y in range(1<<(d*t+k-m))),1<<(d*t+k-m)) for z in range(1<<m)]
  rounded=[1 if a>=0 else -1 for a in means]
  e=F(sum(a!=rounded[z%(1<<m)] for z,a in enumerate(f)),len(f))
  delta=1-sum(a*a for a in fa[:1<<m])
  ck(e<=delta/2)
  # Independent conditional-variance representation of spectral tail mass.
  ck(delta==sum(1-a*a for a in means)/(1<<m))
 records.append({'d':d,'t':t,'k':k,'n':d*t+k,'I':str(sum(physical))})
for k in range(2,21):
 p=F(1,1<<k)
 ck(k*p<=F(1,2));ck((10*(k+1)+15)*p/2<(10*k+15)*p)
 for K in [0,1,2,4]:ck(((10+2*K)*(k+1)+15)*p/2<((10+2*K)*k+15)*p)
r={'status':'PASS','assertions':C,'fixtures':records,'runtime_seconds':time.monotonic()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic':'direct character sums, physical edges and exact Fraction; symbolic rate monotonicity guards k2..20','scope':'independent implementation by A051, not independent-agent acceptance'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r))
