from pathlib import Path
from collections import deque
import itertools,json,time,hashlib
R=Path(__file__).resolve().parents[1]
FULL=(1<<16)-1;E={0,1,2,4}
def mask(vals):return sum(int(v)<<i for i,v in enumerate(vals))
linear=[mask((x&s).bit_count()%2 for x in range(16)) for s in range(1,16)]
mon=[mask((x>>i&1)*(x>>j&1) for x in range(16)) for i in range(4) for j in range(i+1,4)]
basis=[linear[(1<<i)-1] for i in range(4)]+mon
words=[]
for code in range(1024):
 w=0
 for j,v in enumerate(basis):
  if code>>j&1:w^=v
 words.append(w)
assert len(set(words))==1024 and all(not w&1 for w in words)
gens=[]
for i in range(4):gens.append(('outside_translate_'+str(i),[x^(1<<i) for x in range(16)],0))
# Affine permutation of the tetrahedron's four vertices.
gens.append(('swap_t1_t2',[((x&1)<<1)|((x&2)>>1)|(x&12) for x in range(16)],0))
gens.append(('swap_t2_t3',[(x&9)|((x&2)<<1)|((x&4)>>1) for x in range(16)],0))
gens.append(('swap_origin_t1',[(x&14)|((1+(x&7).bit_count())%2) for x in range(16)],0))
for i in range(3):gens.append(('v_shear_t'+str(i),[x^((1<<i) if x&8 else 0) for x in range(16)],0))
gens.append(('common_v_character',list(range(16)),linear[7]))
for name,perm,add in gens:
 assert len(set(perm))==16
 if name.startswith('swap') or name.startswith('v_shear'):assert {perm[e] for e in E}==E
 if name=='common_v_character':assert all(not add>>e&1 for e in E)
def act(w,g):
 name,p,add=g;out=mask((w>>p[x]&1) for x in range(16))^add
 return out^(FULL if out&1 else 0)
start=time.perf_counter();remaining=set(words);orbits=[];lookup={};checks=0
while remaining:
 rep=min(remaining);todo=deque([rep]);seen={rep};parent={str(rep):None}
 while todo:
  w=todo.popleft()
  for j,g in enumerate(gens):
   v=act(w,g);assert v in remaining or v in seen;checks+=1
   if v not in seen:seen.add(v);todo.append(v);parent[str(v)]=[w,j]
 for w in seen:lookup[str(w)]=rep
 remaining-=seen;orbits.append({'representative':rep,'size':len(seen),'parents':parent})
assert sum(o['size'] for o in orbits)==1024
out={'status':'PASS','helper':'A017-tetrahedron-normalization-v1','outside_words':1024,'generators':[{'name':n,'permutation':p,'add_mask':a} for n,p,a in gens],'orbits':orbits,'lookup':lookup,'generator_checks':checks,'elapsed_seconds':time.perf_counter()-start}
(R/'out/orbits.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['orbits','lookup','generators']}));print('ORBITS',[(o['representative'],o['size']) for o in orbits])
