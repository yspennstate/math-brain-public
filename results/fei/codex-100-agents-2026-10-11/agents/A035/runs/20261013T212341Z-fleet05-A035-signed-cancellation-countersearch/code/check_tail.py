from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,time
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();count=0;minimum=Q(1);records=[]
kernel={'__file__':str(ROOT/'code'/'check_shared.py')}
exec((ROOT/'code'/'check_shared.py').read_text(encoding='utf-8').split('# Exact five-variable local module:')[0],kernel)
def value(x,flip):
 s=(-1)**(((x&3)==3)+(((x>>2)&3)==3))
 return -s if flip and x==0 else s
for flip in [False,True]:
 for assignment in product([-1,0,1],repeat=4):
  free=[i for i in range(4) if assignment[i]==-1]
  fixed=sum(a<<i for i,a in enumerate(assignment) if a!=-1)
  t=[value(fixed|sum(((y>>j)&1)<<i for j,i in enumerate(free)),flip) for y in range(1<<len(free))]
  for j,i in enumerate(free):
   d=Q(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t))
   assert not d or d>=Q(1,4)
   phase=kernel['split'](t,j);assert phase['d']==d
   if d:assert phase['B'][1]<=4*d
   if d:minimum=min(minimum,d)
   records.append(dict(flip=flip,assignment=list(assignment),query=i,d=str(d),B=kernel['emit'](phase['B']) if d else ['0','0'],B_bound='0 if d=0; otherwise B<=h2(d)<=1<=4d'))
   count+=1
assert count==216 and time.perf_counter()-start<50
out=dict(helper_version='A035-tail-completion-v1',split_count=count,min_positive_d=str(minimum),all_nodes_K4_good=True,runtime_seconds=time.perf_counter()-start,records=records)
(ROOT/'out'/'tail_completion.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
