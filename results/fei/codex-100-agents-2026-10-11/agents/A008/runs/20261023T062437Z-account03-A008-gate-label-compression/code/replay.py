from fractions import Fraction as Q
from pathlib import Path
import itertools,math,json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def check(v):
 global checks
 assert v
 checks+=1
 if checks%500==0 and time.monotonic()-start>55:raise RuntimeError('frozen limit')
# Derive rather than assume the offspring tail constant.
t=Q(17,20);head=sum((Q(1,c+1)-Q(1,c+2))*t**c for c in range(17))
tail=1-sum(Q(1,c+1)-Q(1,c+2) for c in range(17));check(tail==Q(1,18));check(head+tail*t**17<Q(4,5))
transition_cases=0
for w in [1,2]:
 r=2**w;block=(1<<w)-1;dim=r*w
 gates=[sum(1<<(c*w+j) for c,j in enumerate(xs))|(block<<(dim+D*w)) for xs in itertools.product(range(w),repeat=r) for D in range(r)]
 for C,D in itertools.product(range(r),repeat=2):
  xblock=block<<(C*w);yblock=block<<(dim+D*w);target=xblock|yblock
  for parent,child in itertools.product(gates,repeat=2):
   # Every allowed edge changing its X_C coordinate must enter a marked D-gate.
   changes=(parent&xblock)!=(child&xblock)
   attaches=bool(parent&child&target)
   check(not(changes and attaches) or child&yblock==yblock);transition_cases+=1
root_cases=targets=0
for gates in [[1,2,4],[3,6],[7,1,6],[3,12,5],[15,1,2,4,8]]:
 N=len(gates);lam=Q(1,N+1);xs=[lam/Q(2**g.bit_count()) for g in gates]
 rootps=[x/(1+x) for x in xs];normalizer=1-math.prod(1-v for v in rootps);D=math.prod(1+x for x in xs)-1
 n=max(gates).bit_length()
 for target in range(1,1<<n):
  if any(not any(g>>i&1 for g in gates) for i in range(n) if target>>i&1):continue
  targets+=1
  # Components reconstructed by union closure on coordinate bitmasks.
  comps=[];todo=target
  while todo:
   c=todo&-todo
   while True:
    nc=c
    for g in gates:
     if g&c:nc|=g&target
    if nc==c:break
    c=nc
   comps.append(c);todo&=~c
  groups=[[i for i,g in enumerate(gates) if g&c] for c in comps]
  factor=math.prod(math.prod(1+xs[i] for i in G)-1 for G in groups)/D
  mass=Q(0)
  for roots in range(1,1<<N):
   p=math.prod(rootps[i] if roots>>i&1 else 1-rootps[i] for i in range(N))/normalizer
   check(p==math.prod(xs[i] for i in range(N) if roots>>i&1)/D);root_cases+=1
   # Reachable gate types via attachments inside target, starting at actual roots.
   active={i for i in range(N) if roots>>i&1}
   if any(not(gates[i]&target) for i in active):continue
   while True:
    grow=active|{j for i in active for j in range(N) if gates[i]&gates[j]&target}
    if grow==active:break
    active=grow
   reach=0
   for i in active:reach|=gates[i]&target
   if reach==target:mass+=p
  check(mass==factor)
  Sc=[sum(xs[i] for i in G) for G in groups];pi=max(Sc)
  if pi<=Q(1,2):check(factor<=pi**(len(comps)-1)/(len(comps)*(1-pi)**len(comps)))
for w in range(32,97):
 r=2**w;check((48*w)**2<=r)
 # Verify the polynomial inequalities that turn actual sector mass into the bound.
 check(Q(w*w,8)*Q(1,162)/(2*w)==Q(w,2592))
 check((r//2)*(r//2)*(r-1)*r*Q(4,r**4)>=Q(1,2))
result={'status':'PASS','checks':checks,'attachment_transition_cases':transition_cases,'root_target_cases':targets,'root_set_cases':root_cases,'elapsed_seconds':time.monotonic()-start,'pgf_upper':str(head+tail*t**17)}
(R/'out/replay.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
