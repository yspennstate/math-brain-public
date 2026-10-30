from pathlib import Path
from collections import Counter
from functools import lru_cache
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1];E={0,1,2,4};free=[x for x in range(16) if x not in E];EM=sum(1<<(2*x+1) for x in E)
chars=[sum(((x&s).bit_count()%2)<<x for x in range(64)) for s in range(64)]
@lru_cache(None)
def spread(v):return sum((v>>x&1)<<(2*x) for x in range(16))
def full(I,O):return (spread(I)*3^EM)|(spread(O)*3<<32)
def walsh_pop(f):return [64-2*(f^c).bit_count() for c in chars]
def hist(f):
 W=walsh_pop(f);assert all(w%4==0 for w in W)
 assert sum(w*w for w in W)==4096
 return tuple(sorted(Counter((W[j]**2//16,W[j+1]**2//16) for j in range(0,64,2) if W[j] and W[j+1]).items()))
def factors(n):
 v={};p=2
 while p*p<=n:
  while n%p==0:v[p]=v.get(p,0)+1;n//=p
  p+=1
 if n>1:v[n]=v.get(n,0)+1
 return v
cache={}
def ratio(h):
 if h not in cache:
  expo=Counter()
  for (t,u),count in h:
   for n,sign in [(t+u,1),(t,-1),(u,-1)]:
    for p,e in factors(n).items():expo[p]+=sign*count*n*e
  num=den=1
  for p,e in expo.items():
   if e>0:num*=p**e
   if e<0:den*=p**(-e)
  cache[h]=(num,den)
 return cache[h]
start=time.perf_counter();pilot='--pilot' in sys.argv;o=json.loads((R/'out/orbits.json').read_text(encoding='utf-8'));tc=json.loads((R/'out/tetra_certificate.json').read_text(encoding='utf-8'));best=None;cases=0;checks=0;digest=hashlib.sha256()
for orb in o['orbits']:
 O=orb['representative']
 for code in range(16 if pilot else 4096):
  I=sum((code>>j&1)<<x for j,x in enumerate(free));f=full(I,O);h=hist(f);p,q=ratio(h)
  assert p<=q<<128;checks+=1
  assert (f^(sum((f>>(x^1)&1)<<x for x in range(64)))).bit_count()==8;checks+=1
  if best is None or p*best[1]>best[0]*q:best=(p,q,O,code)
  cases+=1;digest.update(f.to_bytes(8,'little'))
if not pilot:
 assert best[0]*int(tc['maximum']['Q'])==int(tc['maximum']['P'])*best[1];checks+=1
# Check actual-parent action for each orbit word and every generator, not just
# the polynomial masks used by the orbit builder. Inside data is nonconstant.
group=0
for wstr in (list(o['lookup'])[:16] if pilot else o['lookup']):
 O=int(wstr);code=(O*37+123)&4095;I=sum((code>>j&1)<<x for j,x in enumerate(free));p,q=ratio(hist(full(I,O)))
 for g in o['generators']:
  perm=g['permutation'];add=g['add_mask'];name=g['name']
  OO=sum(((O>>perm[x]&1)^(add>>x&1))<<x for x in range(16))
  II=I if name.startswith('outside_translate') else sum(((I>>perm[x]&1)^(add>>x&1))<<x for x in range(16))
  if OO&1:OO^=65535
  assert all(not II>>e&1 for e in E);checks+=1
  pp,qq=ratio(hist(full(II,OO)));assert p*qq==pp*q;checks+=1;group+=1
res={'status':'PASS','pilot':pilot,'independent_parent_cases':cases,'actual_parent_generator_checks':group,'assertions':checks,'entropy_histogram_classes':len(cache),'maximum':{'P':str(best[0]),'Q':str(best[1]),'outside_mask':best[2],'inside_code':best[3]},'coverage_sha256':digest.hexdigest(),'elapsed_seconds':time.perf_counter()-start}
(R/'out'/('independent_pilot.json' if pilot else 'independent_certificate.json')).write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in res.items() if k!='maximum'}))
