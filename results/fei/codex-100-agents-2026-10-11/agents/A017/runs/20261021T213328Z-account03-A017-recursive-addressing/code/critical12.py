from pathlib import Path
from itertools import product,islice
from collections import Counter
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]
def walsh(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
  h*=2
 return a
def ratio(A):
 p=q=1
 for a in A:
  t=a*a;p*=(t+1)**(t+1)
  if t:q*=t**t
 return p,q
start=time.perf_counter();pilot='--pilot' in sys.argv;checks=cases=0
P=[u for u in range(32) if u>>2&1];E=[u for u in P if u>>3==0];removed=[u for u in P if u not in E]
assert len(E)==4 and len(removed)==12
base=[(-1)**(((x>>0&1)*(x>>3&1)+(x>>1&1)*(x>>2&1))%2) for x in range(64)]
for code in range(32 if pilot else 4096):
 f=base.copy()
 for j,u in enumerate(removed):f[2*u+(code>>j&1)]*=-1
 assert sum(a!=b for a,b in zip(f,base))==12;checks+=1
 assert [u for u in range(32) if f[2*u]!=f[2*u+1]]==E;checks+=1
 W=walsh(f);p=q=1
 for j in range(0,64,2):
  a,b=W[j]//4,W[j+1]//4;t,v=a*a,b*b
  if t+v:p*=(t+v)**(t+v)
  if t:q*=t**t
  if v:q*=v**v
 assert p<=q<<128;checks+=1
 # Child slices in t=x1,x2; z=x3,x4,x5. Exactly four outside P untouched.
 affine=0
 for z in range(8):
  vals=[f[2*(t+4*z)] for t in range(4)];v=walsh(vals)
  affine+=sum(abs(a)==4 for a in v)
  if not z&1:assert vals==[1,1,1,-1];checks+=1
 assert affine<=3;checks+=1;cases+=1
algebra=0
for removed_n in range(17):
 for added_n in range(17):
  for doubled in range(33-removed_n-added_n):
   edits=removed_n+added_n+2*doubled
   if edits<=12 and 16-removed_n+added_n==4:
    assert (removed_n,added_n,doubled,edits)==(12,0,0,12);algebra+=1
assert algebra==1 and 3**5<2**8
out={'status':'PASS','pilot':pilot,'actual_twelve_edit_parents':cases,'assertions':checks,'feasible_critical_paircount_triples':algebra,'affine_intrusions_at_most':3,'terminal_log_sign_slack':2**8-3**5,'elapsed_seconds':time.perf_counter()-start}
(R/'out'/('critical12_pilot.json' if pilot else 'critical12_certificate.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
