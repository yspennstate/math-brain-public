from pathlib import Path
from fractions import Fraction as Q
import itertools,json,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x
events=[];table=[]
for x in range(16):
 y1,y2,y3,z=[bool(x>>j&1) for j in range(4)]
 a=y1 and y2 and z;b=(not y1) and y3 and z;c=(not y2) and (not y3)
 ck(int(a)+int(b)+int(c)<=1)
 events.append([a,b,c]);table.append(1 if a or b or c else -1)
mask=sum(int(t==1)<<x for x,t in enumerate(table));ck(mask==56067)
ck(all(any(table[x]!=table[x^(1<<j)] for x in range(16)) for j in range(4)))
blocks=[]
for size in (2,3):
 for B in itertools.combinations(range(4),size):
  C=[j for j in range(4) if j not in B]
  rows={tuple(table[sum(((a>>j)&1)<<B[j] for j in range(size))+sum(((z>>j)&1)<<C[j] for j in range(len(C)))] for z in range(1<<len(C))) for a in range(1<<size)}
  ck(len(rows)>2);blocks.append({'block':[j+1 for j in B],'rows':len(rows)})
def delta(t):
 w=[sum(t[x]*(-1)**((s&x).bit_count()) for x in range(16)) for s in range(16)]
 p=[Q(a*a,256) for a in w]
 ck(sum(p)==1)
 I=sum((s.bit_count()*p[s] for s in range(16)),Q(0))
 return I,1-p[0],I-(1-p[0])
components=[delta([1 if e[j] else -1 for e in events]) for j in range(3)]
actual=delta(table)
ck([x[2] for x in components]==[Q(5,16),Q(5,16),Q(1,4)])
ck(actual==(Q(7,4),Q(1),Q(3,4)))
ck(actual[2]-sum(x[2] for x in components)==Q(-1,8))
out={'mask':mask,'prime':True,'proper_blocks':blocks,'uniform_components_I_Var_delta':[[str(y) for y in x] for x in components],
     'uniform_actual_I_Var_delta':[str(x) for x in actual],
     'deficit_loss':'1/8','general_exact_loss':'delta(F)-sum delta(components)=-2*v1*p2*p3*p4*(1-p4)',
     'general_identity_status':'analytic derivation in NEXT_FIXTURE.md; uniform case checked here',
     'assertions':checks,'all_passed':True,'runtime_seconds':time.perf_counter()-start}
(ROOT/'out/next_fixture.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='proper_blocks'}))
