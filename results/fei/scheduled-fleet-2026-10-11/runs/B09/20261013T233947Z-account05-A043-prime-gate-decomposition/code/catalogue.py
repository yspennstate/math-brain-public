from pathlib import Path
import itertools,json,time
OUT=Path(__file__).resolve().parents[1]/'out';start=time.perf_counter();checks=0
def ck(q):
 global checks
 assert q;checks+=1
def table(m):return tuple(2*((m>>x)&1)-1 for x in range(8))
def prime(t):
 if not all(any(t[x]!=t[x^(1<<i)] for x in range(8)) for i in range(3)):return False
 for B in itertools.combinations(range(3),2):
  d=next(i for i in range(3) if i not in B)
  rows={tuple(t[((a&1)<<B[0])|(((a>>1)&1)<<B[1])|(b<<d)] for b in range(2)) for a in range(4)}
  if len(rows)<=2:return False
 return True
def orbit(m):
 t=table(m);result=set()
 for perm in itertools.permutations(range(3)):
  for flip in range(8):
   a=sum(int(t[sum((((x^flip)>>i)&1)<<perm[i] for i in range(3))]==1)<<x for x in range(8))
   result.update([a,a^255])
 return result
primes={m for m in range(256) if prime(table(m))};ck(len(primes)==104)
classes=[];remaining=primes.copy()
while remaining:
 m=min(remaining);o=orbit(m);ck(o<=primes);ck(not(o & (primes-remaining)));remaining-=o
 t=table(m)
 walsh=[sum(t[x]*(-1 if (x&S).bit_count()%2 else 1) for x in range(8)) for S in range(8)]
 mobius=[sum((-1)**((S^U).bit_count())*t[U] for U in range(8) if U&S==U) for S in range(8)]
 classes.append({'representative':m,'orbit_size':len(o),'orbit':sorted(o),'positive_assignments':[x for x in range(8) if t[x]==1],'uniform_walsh_numerators_den8':walsh,'bit_mobius_coefficients':mobius})
 for v in o:ck(orbit(v)==o)
ck(sum(c['orbit_size'] for c in classes)==104)
result={'helper':'A043-ternary-prime-catalogue-v1','prime_count':104,'classes':classes,'majority_class':min(orbit(232)),'mux_class':min(orbit(sum(int((((x>>1)&1) if x&1 else ((x>>2)&1)))<<x for x in range(8)))),'previous_n3_grid_winner_class':min(orbit(142)),'assertions':checks,'runtime_seconds':time.perf_counter()-start}
(OUT/'catalogue.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
