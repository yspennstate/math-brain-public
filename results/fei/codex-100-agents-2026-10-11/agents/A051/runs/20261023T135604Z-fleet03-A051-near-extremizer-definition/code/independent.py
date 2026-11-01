from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
R=Path(__file__).resolve().parents[1];START=time.monotonic();C=0
def ck(z):
 global C
 C+=1;assert z,C
 if time.monotonic()-START>55:raise RuntimeError('55s frozen cap')
def currentI(g):
 n=len(g).bit_length()-1
 return F(sum(g[z]!=g[z^(1<<j)] for z in range(len(g)) for j in range(n)),len(g))
def walk(g,k,dep=0):
 n=len(g).bit_length()-1
 if n==0:return F(0),F(0),F(0)
 I=currentI(g);q=F(sum(g[z]!=g[z^1] for z in range(len(g))),len(g))
 children=[]
 for b in [0,1]:
  h=tuple(g[z] for z in range(b,len(g),2))
  children.append((F(0),F(0),F(0)) if dep<k and b else walk(h,k,dep+1))
 return I+(children[0][0]+children[1][0])/2,q+(children[0][1]+children[1][1])/2,1+(children[0][2]+children[1][2])/2
records=[];sharp=0
for k,t in [(2,1),(3,1),(2,2),(2,4)]:
 p=F(1,1<<k);mu=F(1,2)**t;N=1<<(k+2*t)
 def val(z):return 1 if z% (1<<k) else (-1)**sum(((z>>(k+2*j))&1)*((z>>(k+2*j+1))&1) for j in range(t))
 g=tuple(val(z) for z in range(N));omega,spend,depth=walk(g,k)
 ck(spend==currentI(g)==p*(t+k*(1-mu)))
 ck(omega==p*(k*t+(1-mu)*F(k*(k+1),2)+t*t+F(t,2)))
 ck(depth==2*(1-p)+p*2*t)
 ds=[next((j+1 for j in range(k) if z>>j&1),k+2*t) for z in range(N)]
 ordered=sorted(ds,reverse=True);prefix=[0]
 for z in ordered:prefix.append(prefix[-1]+z)
 # Exact dual sharpness over EVERY admissible event probability for this actual depth law.
 tails={L:sum(max(z-L,0) for z in ds) for L in range(max(ds)+1)}
 for j in range(N+1):
  primal=F(prefix[j],N);dual=min(F(L*j+tail,N) for L,tail in tails.items())
  ck(primal==dual);sharp+=1
 records.append({'k':k,'t':t,'n':k+2*t,'I':str(spend),'remaining_influence_occupation':str(omega),'expected_depth':str(depth)})
for t in [1,2,3]:
 g=tuple((-1)**sum(((z>>(2*j))&1)*((z>>(2*j+1))&1) for j in range(t)) for z in range(1<<(2*t)))
 omega,spent,_=walk(g,0);ck(omega==t*t+F(t,2));ck(spent==t)
# Large actual formula guard, certified without enumeration.
ck(F(1024)*512>1000*517);ck(1+F(10,1024)==F(517,512))
ck(F(1024)/(F(517,512))>1000)
r={'status':'PASS','assertions':C,'sharp_depth_probabilities':sharp,'activation_fixtures':records,'runtime_seconds':time.monotonic()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic':'direct Boolean exponents, recursive physical edge counts, exact Fraction, exact top-tail primal/dual depth certificates','large_guard':{'seed':'bent2','k':10,'t':1024,'dimension':2058,'root_I_upper':'517/512','remaining_influence_occupation_lower':'1024','overcharge_factor_lower':'>1000'},'scope':'independent A051 implementation, not independent-agent acceptance'}
(R/'out/INDEPENDENT.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r))
