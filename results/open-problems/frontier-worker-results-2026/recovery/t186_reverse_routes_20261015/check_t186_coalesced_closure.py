from pathlib import Path
from itertools import product
from datetime import datetime
import random,json,hashlib
H=Path(__file__).resolve().parent
def update(table,inputs,m):return table[inputs[0]*m+inputs[1]]
def trajectory(tables,s,forced,m,deps=None):
 n=len(s);deps=deps or [((i+1)%n,(i+2)%n) for i in range(n)]
 x=[0 if i in forced else s[i] for i in range(n)];history=[tuple(x)]
 for _ in range(m*n+1):
  y=[0 if i in forced else update(tables[i],[x[j] for j in deps[i]],m) for i in range(n)]
  assert all(a<=b for a,b in zip(y,x))
  if y==x:return y,history
  x=y;history.append(tuple(x))
 raise AssertionError('Trajectory did not stop')
def closure(tables,s,forced,m,rng,broken=False,deps=None):
 n=len(s);deps=deps or [((i+1)%n,(i+2)%n) for i in range(n)]
 low=[0 if i in forced else s[i] for i in range(n)];flag=set();seen=set()
 for _ in range(m*n+2):
  before=low[:];order=list(range(n));rng.shuffle(order)
  for i in order:
   if i in forced:continue
   changed=sorted({j for j in deps[i] if low[j]<s[j]})
   if len(changed)>=2:flag.add(i);value=0
   elif len(changed)==1:
    if broken and i in seen:continue
    seen.add(i);value=update(tables[i],[low[j] if j==changed[0] else s[j] for j in deps[i]],m)
   else:continue
   low[i]=min(low[i],value)
  if low==before:return low,flag
 raise AssertionError('Closure did not stop')
def monotone_tables(m):
 for t in product(range(m),repeat=m*m):
  if all(t[i*m+j]<=t[(i+1)*m+j] for i in range(m-1) for j in range(m)) and all(t[i*m+j]<=t[i*m+j+1] for i in range(m) for j in range(m-1)):yield t
rng=random.Random(362186)
counts={'boolean_networks':0,'boolean_fixed_baselines':0,'boolean_forcings':0,'ternary_networks':0,'ternary_forcings':0,'strict_actual_drops':0,'closures_below_actual':0}
broken_witness=None
def verify(tables,s,forced,m):
 global broken_witness
 x,hist=trajectory(tables,s,forced,m)
 low,flag=closure(tables,s,forced,m,rng)
 assert all(l<=a for state in hist for l,a in zip(low,state)),(tables,s,forced,x,low)
 deps=[((i+1)%len(s),(i+2)%len(s)) for i in range(len(s))]
 image=[0 if i in forced else update(tables[i],[low[j] for j in deps[i]],m) for i in range(len(s))]
 assert all(a<=b for a,b in zip(low,image))
 counts['strict_actual_drops']+=sum(a<b for a,b in zip(x,s))
 counts['closures_below_actual']+=int(low!=x)
 if m==3 and broken_witness is None:
  bad,_=closure(tables,s,forced,m,rng,broken=True)
  if any(l>a for l,a in zip(bad,x)):broken_witness={'tables':tables,'baseline':s,'forced':sorted(forced),'actual':x,'broken':bad,'correct':low}
bools=list(monotone_tables(2));assert len(bools)==6
for tables in product(bools,repeat=3):
 counts['boolean_networks']+=1
 for s in product(range(2),repeat=3):
  if not all(update(tables[i],[s[(i+1)%3],s[(i+2)%3]],2)==s[i] for i in range(3)):continue
  counts['boolean_fixed_baselines']+=1
  for mask in range(8):verify(tables,s,{i for i in range(3) if mask>>i&1},2);counts['boolean_forcings']+=1
ternary=list(monotone_tables(3))
for trial in range(2500):
 tables=[rng.choice(ternary) for _ in range(3)]
 s=[2]*3
 for _ in range(8):
  v=[update(tables[i],[s[(i+1)%3],s[(i+2)%3]],3) for i in range(3)]
  if v==s:break
  s=v
 else:raise AssertionError('Baseline did not settle')
 counts['ternary_networks']+=1
 for mask in range(8):verify(tables,s,{i for i in range(3) if mask>>i&1},3);counts['ternary_forcings']+=1
if broken_witness is None:
 # A feedback coordinate first lowers to1, then to0. Its downstream
 # recipient must process both values on this SAME input coordinate.
 tables=[(2,)*9,tuple((a+b)//2 for a in range(3) for b in range(3)),tuple(a for a in range(3) for b in range(3)),(2,)*9]
 deps=[(3,3),(0,1),(1,3),(3,3)];s=[2]*4;forced={0}
 actual,_=trajectory(tables,s,forced,3,deps)
 for seed in range(100):
  bad,_=closure(tables,s,forced,3,random.Random(seed),broken=True,deps=deps)
  good,_=closure(tables,s,forced,3,random.Random(seed),deps=deps)
  assert all(l<=a for l,a in zip(good,actual))
  if any(l>a for l,a in zip(bad,actual)):
   broken_witness={'fixture':'four-coordinate feedback and downstream copy','seed':seed,'tables':tables,'deps':deps,'baseline':s,'forced':[0],'actual':actual,'broken':bad,'correct':good};break
assert broken_witness is not None,'Need a positive failure control for skipped reevaluation'
# Independent constant-update chain control: first common site is forced by
# two changed boundary inputs; every later site receives one changed input.
constant_controls=[]
from collections import deque
def constant_chain(n,coalesce):
 seen=[set() for _ in range(n)];flags=set();queue=deque([(0,'boundary0',0),(0,'boundary1',0)])
 while queue:
  site,coord,b=queue.popleft();key=coord if coalesce else (coord,b)
  if key in seen[site]:continue
  seen[site].add(key)
  # Single-input constant response is2, so sends no strict token.
  if len(seen[site])>=2 and site not in flags:
   flags.add(site)
   if site+1<n:
    for value in [0,1]:queue.append((site+1,'previous_site',value))
 return len(flags)
for n in [10,100,1000]:
 old_flags=constant_chain(n,False);new_flags=constant_chain(n,True)
 assert old_flags==n and new_flags==1
 constant_controls.append({'sites':n,'old_second_token_flags':old_flags,'coalesced_distinct_coordinate_flags':new_flags})
out={'at':datetime.now().astimezone().isoformat(),'status':'PASS finite adversarial controls; general lemma still requires analytic review','counts':counts,'ternary_monotone_table_count':len(ternary),'broken_skip_reevaluation_rejected':broken_witness,'constant_controls':constant_controls,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exhaustive Boolean 3-site two-input monotone networks at all fixed baselines/forcing sets; 2500 seeded ternary networks at greatest fixed baseline/all forcing sets. These controls do not establish stochastic sparsity or finite WP transfer.'}
(H/'T186_COALESCED_CLOSURE_CHECK_RECEIPT.json').write_bytes((json.dumps(out,indent=2)+'\n').encode())
print(json.dumps(out))
