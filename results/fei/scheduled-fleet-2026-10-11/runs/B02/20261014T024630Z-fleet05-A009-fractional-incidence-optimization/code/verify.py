from fractions import Fraction as F
from pathlib import Path
import json, math, time, sys
ROOT=Path(__file__).resolve().parents[1]; checks=0
sys.set_int_max_str_digits(0)
DYAD=2**80
def down(x): return F((x*DYAD).__floor__(),DYAD)
def up(x): return F((x*DYAD).__ceil__(),DYAD)
def ck(x):
 global checks
 assert x
 checks+=1
def logunit(x):
 z=(x-1)/(x+1); t=z; total=F(0)
 for j in range(24): total+=t/(2*j+1); t*=z*z
 return 2*total,2*total+2*t/(49*(1-z*z))
l2,h2=logunit(F(2))
def logbound(x):
 # Use integer bit lengths to select scaling independently of proposal helper.
 k=x.numerator.bit_length()-x.denominator.bit_length()
 scaled=x/F(2)**k
 if scaled<1: scaled*=2; k-=1
 if scaled>=2: scaled/=2; k+=1
 lo,hi=logunit(scaled)
 return F(k)+lo/h2,F(k)+hi/l2
start=time.perf_counter(); rows=[]
data=json.loads((ROOT/'out/CHECK.json').read_text())
for c in data['certificates']:
 n=c['n']; edges=[tuple(e) for e in c['edges']]; N=len(edges)
 lam=list(map(F,c['lambda'])); base=list(map(F,c['base_lambda'])); y=list(map(F,c['coordinate_prices'])); usage=list(map(F,c['c'])); v=F(c['v']); I=F(c['I'])
 P={int(b):F(x) for b,x in c['P'].items()}; W={int(b):F(x) for b,x in c['W_base'].items()}; polys={int(b):{int(k):F(x) for k,x in p.items()} for b,p in c['occupation_coefficients'].items()}
 vals=[1 if any((x>>u&1) and (x>>w&1) for u,w in edges) else -1 for x in range(1<<n)]
 direct={b:F(sum(vals[x]*(-1 if (b&x).bit_count()%2 else 1) for x in range(1<<n))**2,4**n) for b in range(1,1<<n)}
 ck({b:x for b,x in direct.items() if x}==P); ck(sum(P.values())==v); ck(sum(p*b.bit_count() for b,p in P.items())==I)
 recomputed=[F(0)]*N; costlo=F(0); costhi=F(0)
 D=math.prod(1+x/4 for x in lam)-1; ck(D==F(c['D']))
 for b in P:
  terms={mask:k*math.prod(base[e] for e in range(N) if mask>>e&1) for mask,k in polys[b].items()}
  ck(sum(terms.values())==W[b])
  lo,hi=logbound(D/W[b]); costlo=down(costlo+P[b]*lo); costhi=up(costhi+P[b]*hi)
  for mask,mass in terms.items():
   for e in range(N):
    if mask>>e&1: recomputed[e]+=P[b]*mass/W[b]
   ratio=math.prod(base[e]/lam[e] for e in range(N) if mask>>e&1)
   lo,hi=logbound(ratio); costlo=down(costlo+P[b]*mass/W[b]*lo); costhi=up(costhi+P[b]*mass/W[b]*hi)
 ck(recomputed==usage)
 ck(all(x>0 for x in usage))
 if N>=2: ck(sum(usage)>v)
 root={}
 for mask in range(1,1<<N): root[mask]=math.prod(lam[e]/4 for e in range(N) if mask>>e&1)/D
 ck(sum(root.values())==1)
 marg=[sum(p for mask,p in root.items() if mask>>e&1) for e in range(N)]
 ck(marg==list(map(F,c['root_marginals'])))
 C=sum(usage); delta=F(c['mixture_delta']); sigma={1<<e:usage[e]/C for e in range(N)}
 nu={mask:(1-delta)*p+delta*sigma.get(mask,F(0)) for mask,p in root.items()}
 ck(sum(nu.values())==1); ck(all(p>=0 for p in nu.values()))
 r=[sum(p for mask,p in nu.items() if mask>>e&1) for e in range(N)]; b=[usage[e]-v*r[e] for e in range(N)]
 ck(b==list(map(F,c['b']))); ck(all(x>=0 for x in b))
 chi=sum((sigma.get(mask,F(0))-p)**2/p for mask,p in root.items()); ck(chi==F(c['root_chi_square']))
 exact_mix_chi=sum((nu[mask]-p)**2/p for mask,p in root.items()); ck(exact_mix_chi==delta**2*chi)
 slack=F(0)
 for j in range(n):
  row=sum(lam[e] for e,E in enumerate(edges) if j in E); ck(row<=1); ck(y[j]>=0); slack+=y[j]*(1-row)
 gapnat=v*exact_mix_chi+slack
 for e,(u,w) in enumerate(edges):
  z=lam[e]*(y[u]+y[w]); ck(z>0); gapnat+=(b[e]-z)**2/z
 gap=2*gapnat; ck(gap==F(c['bit_gap_upper'])); ck(gap<=I/10**7)
 oldlo,oldhi=map(F,c['frozen_cost_interval']); ck(costlo<=oldhi and oldlo<=costhi)
 ck(costhi<F(9,2)*I)
 rows.append({'name':c['name'],'gap_over_I_upper':str(gap/I),'complete_cost_over_I_upper':str(costhi/I),'strict_9I_over_2_margin':str(F(9,2)*I-costhi)})
for a in range(13):
 for b in range(13):
  c=a+b; exact=F(math.factorial(a)*math.factorial(b),(c+1)**2*(c+2))
  moments=F(1,c+1)*F(2,(c+1)*(c+2))*math.factorial(a)*math.factorial(b)
  ck(moments/2==exact)
  ck(exact>=F(2**max(c-1,0),2*6**c))
result={'functions':len(rows),'checks':checks,'elapsed_seconds':time.perf_counter()-start,'all_verified':True,'all_gap_bounds_I_over_10million':True,'all_complete_frozen_costs_below_9I_over_2':True,'local_occupation_credit_cases':169,'certificates':rows}
(ROOT/'out/VERIFY.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='certificates'}))
