from pathlib import Path
from itertools import product
import argparse,time,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
start=time.monotonic();checks=0;functions=0;support_sets=0;disconnected_positive=0;forests=0;outside_witnesses=0
def ck(b):
 global checks
 assert b;checks+=1
 assert time.monotonic()-start<55
def components(A,gates):
 parts=[{i} for i in A]
 for gate in gates:
  hit=[p for p in parts if p&gate]
  if hit:
   union=set().union(*hit)
   parts=[p for p in parts if not p&union]+[union]
 return parts
for n in range(1,3 if args.pilot else 4):
 size=1<<n
 faces=[]
 for s in product([-1,0,1],repeat=n):
  points=[z for z in range(size) if all(not a or bool(z>>i&1)==(a==1) for i,a in enumerate(s))]
  faces.append((s,points))
 for table in range(1,(1<<size)-1):
  truth=[1 if table>>z&1 else -1 for z in range(size)]
  prime_tables=[]
  for polarity in [1,-1]:
   implicants={s for s,points in faces if all(truth[z]==polarity for z in points)}
   primes={s for s in implicants if all(tuple(0 if i==j else a for i,a in enumerate(s)) not in implicants for j,a in enumerate(s) if a)}
   prime_tables.append([{i for i,a in enumerate(s) if a} for s in sorted(primes)])
  walsh=[sum(truth[z]*(-1)**((z&mask).bit_count()) for z in range(size)) for mask in range(size)]
  ck(sum(c*c for c in walsh)==size*size)
  for mask in range(1,size):
   if not walsh[mask]:continue
   A={i for i in range(n) if mask>>i&1}
   plus,minus=prime_tables;parts=components(A,plus);other=components(A,minus)
   ck(len(parts)==1 or len(other)==1)
   if len(parts)>1:
    disconnected_positive+=1
    for c in range(len(parts)):
     for d in range(c+1,len(parts)):
      for a in parts[c]:
       for b in parts[d]:ck(any({a,b}<=gate for gate in minus))
    # Exhibit an outside fiber with a nonzero full-A coefficient, independently of graph code.
    outside=set(range(n))-A
    fibers=[]
    for z in range(size):
     if z&mask:continue
     value=sum(truth[z|x]*(-1)**((x&mask).bit_count()) for x in range(size) if not x & ~mask)
     if value:fibers.append(z)
    ck(bool(fibers));outside_witnesses+=1
   gates=plus if len(parts)==1 else minus
   # Greedy construction of an actual ordered ownership tree, with one root.
   first=next(e for e,g in enumerate(gates) if g&A)
   used=[first];owned={first:gates[first]&A};covered=set(owned[first]);parents={}
   while covered!=A:
    e=next(e for e,g in enumerate(gates) if e not in used and g&covered and (g&A)-covered)
    attachment=min(gates[e]&covered)
    parent=next(h for h in used if attachment in owned[h])
    ck(attachment in gates[e] and attachment in owned[parent])
    owned[e]=(gates[e]&A)-covered
    parents[e]=(parent,attachment)
    covered|=owned[e];used.append(e)
   ck(len(used)<=len(A))
   ck(sum(map(len,owned.values()))==len(A))
   ck(set().union(*owned.values())==A)
   ck(all(owned[e] and owned[e]<=gates[e] for e in used))
   # Independent reachability in the FULL ownership graph, not just the chosen parent tree.
   edges={e:{h for h in used if h!=e and owned[e]&gates[h]} for e in used}
   reached={first};pending=[first]
   while pending:
    e=pending.pop()
    for h in edges[e]-reached:reached.add(h);pending.append(h)
   ck(reached==set(used))
   support_sets+=1;forests+=1
  functions+=1
result={'status':'PASS','pilot':args.pilot,'assertions':checks,'functions':functions,
 'nonempty_Fourier_support_sets':support_sets,'positive_disconnected_cases':disconnected_positive,
 'outside_fiber_witnesses':outside_witnesses,'one_root_partition_forests':forests,
 'seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'arithmetic':'integer Walsh; complete signed prime faces; exact ownership and allowed attachment graphs'}
(ROOT/'out'/('connectivity_pilot.json' if args.pilot else 'connectivity.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
