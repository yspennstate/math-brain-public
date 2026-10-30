from pathlib import Path
from fractions import Fraction as R
import math,time,json
RUN=Path(__file__).resolve().parents[1];(RUN/'out').mkdir(exist_ok=True)
start=time.monotonic()
def fw(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):
    x,y=a[i],a[i+h];a[i],a[i+h]=x+y,x-y
  h*=2
 return a
def maj(v):return 1 if sum(v)>0 else -1
a=[maj([maj([2*((x>>i)&1)-1 for i in range(j,j+3)]) for j in (0,3,6)]) for x in range(512)]
b=a.copy();b[0]*=-1
lengths=[1+3*((s!=0)+sum(bool(s&(7<<j)) for j in (0,3,6))) for s in range(512)]
weights=[R(1,1<<l) for l in lengths];Z=sum(weights);ref=[q/Z for q in weights]
stats={};rows=[]
for depth in range(10):
 ry=[sum(ref[s] for s in range(512) if s>>depth==t) for t in range(1<<(9-depth))]
 for prefix in range(1<<depth):
  aa=[a[prefix|(y<<depth)] for y in range(1<<(9-depth))];bb=[b[prefix|(y<<depth)] for y in range(1<<(9-depth))]
  N=len(aa);ps=[[R(z*z,N*N) for z in fw(v)] for v in (aa,bb)]
  A=sum(p*t.bit_count()/2 for P in ps for t,p in enumerate(P))
  B=sum(float(p)/2*math.log2(1/float(ry[t])) for P in ps for t,p in enumerate(P) if p)
  d=R(sum(x!=y for x,y in zip(aa,bb)),N)
  h=lambda q: -sum(float(t)*math.log2(float(t)) for t in [q,1-q] if t)
  rho=R(1,2);I=A+1+(2-2*d)*rho
  C=B+h(d*rho*rho)+2+2*(1-2*d)*rho+2*float(rho*(1-rho))*math.log2(float((1-rho)/rho*R(20,7)))
  stats[depth,prefix]={'A':A,'B':B,'d':d,'I':I,'C':C,'source_surplus':4*float(A)-B,'surplus':4*float(I)-C}
  assert time.monotonic()-start<55
for (depth,prefix),p in stats.items():
 if depth==9:continue
 cs=[stats[depth+1,prefix|(v<<depth)] for v in (0,1)]
 inf=p['A']-(cs[0]['A']+cs[1]['A'])/2
 e=p['B']-(cs[0]['B']+cs[1]['B'])/2-4*float(inf)
 price=p['C']-(cs[0]['C']+cs[1]['C'])/2-4*float(inf)
 rows.append({'depth':depth,'prefix':prefix,'probability':str(R(1,1<<depth)),'Inf':str(inf),'core_excess':e,'complete_excess':price,'parent_surplus':p['surplus'],'child_surpluses':[c['surplus'] for c in cs],'child_core_influences':[str(c['A']) for c in cs]})
P=sum(2**(-r['depth'])*max(0,r['core_excess']) for r in rows)
out={'status':'DISCOVERY_ONLY','nodes':len(stats),'queries':len(rows),'elapsed_seconds':time.monotonic()-start,'root':{k:str(v) if isinstance(v,R) else v for k,v in stats[0,0].items()},'positive_core_excess_total':P,'minimum_child_surplus':min(p['surplus'] for p in stats.values()),'positive_relevant_rows':[r for r in rows if r['complete_excess']>1e-8 and r['Inf']!='0'],'rows':rows,'reference_normalizer':str(Z)}
(RUN/'out/PILOT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','positive_relevant_rows']}));print('relevant_bad_count',len(out['positive_relevant_rows']));print('first_bad',out['positive_relevant_rows'][:2])
