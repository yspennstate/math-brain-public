import itertools,collections,math,json,pathlib
R=pathlib.Path(__file__).resolve().parent
results=[]
for n in range(1,5):
 perms=list(itertools.permutations(range(n))); pairs=list(itertools.combinations(range(n),2));counts=collections.Counter()
 for x in perms:
  for y in perms:
   rel=tuple(1 if x[i]<x[j] and y[i]<y[j] else -1 if x[i]>x[j] and y[i]>y[j] else 0 for i,j in pairs)
   counts[rel]+=1
 hist=[0]*(n+1); cache={}
 def largest(bad,allowed=(1<<n)-1):
  key=(bad,allowed)
  if key in cache:return cache[key]
  best=0
  for s in range(1<<n):
   if s&~allowed:continue
   if s.bit_count()<=best:continue
   if all(not (bad>>k&1) or not (s>>i&1 and s>>j&1) for k,(i,j) in enumerate(pairs)):best=s.bit_count()
  cache[key]=best;return best
 for a,ca in counts.items():
  for b,cb in counts.items():
   bad=sum((u!=v)<<k for k,(u,v) in enumerate(zip(a,b)))
   c=largest(bad);hist[c]+=ca*cb
   ds=[c-largest(bad,((1<<n)-1)^(1<<i)) for i in range(n)]
   assert all(d in [0,1] for d in ds) and sum(ds)<=c
 total=math.factorial(n)**4
 mean=sum(k*h for k,h in enumerate(hist))/total
 var=sum(k*k*h for k,h in enumerate(hist))/total-mean*mean
 assert var<=mean
 results.append({'n':n,'distinct_labeled_posets':len(counts),'total_rank_quadruples':total,'histogram_C':hist,'mean':mean,'variance':var,'collision_probability':sum(c*c for c in counts.values())/total,'deletion_certificate_checked':True})
(R/'exact_posets.json').write_text(json.dumps(results,indent=2),encoding='utf8');print(json.dumps(results,indent=2))
