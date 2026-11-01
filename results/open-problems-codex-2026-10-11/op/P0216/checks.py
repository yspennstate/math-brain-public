import itertools, fractions, random, math, json, pathlib, time
R=pathlib.Path(__file__).resolve().parent
out={}
# Exhaustive independent cell pairs: all m^4 equally likely outcomes.
m=2;n=3
cells=list(itertools.product(range(m),repeat=2))
outcomes=list(itertools.product(cells,repeat=2))
hist=[0]*(m+1); isolated=0
for seq in itertools.product(outcomes,repeat=n):
 usedr=set();usedc=set();acc=[]
 for i,(p,q) in enumerate(seq):
  if p==q and p[0] not in usedr and p[1] not in usedc:
   usedr.add(p[0]);usedc.add(p[1]);acc.append(i)
 for i,j in itertools.permutations(acc,2):
  p,q=seq[i]; pp,qq=seq[j]
  assert ((p[0]<pp[0]) and (p[1]<pp[1]))==((q[0]<qq[0]) and (q[1]<qq[1]))
 hist[len(acc)]+=1
 for i,(p,q) in enumerate(seq):
  if p==q and all(j==i or a!=b or (a[0]!=p[0] and a[1]!=p[1]) for j,(a,b) in enumerate(seq)):
   isolated+=1
F=fractions.Fraction
dist=[F(1)]+[F(0)]*m
for _ in range(n):
 new=[F(0)]*(m+1)
 for k,p in enumerate(dist):
  hit=F((m-k)**2,m**4)
  new[k]+=p*(1-hit)
  if k<m:new[k+1]+=p*hit
 dist=new
assert [F(x,len(outcomes)**n) for x in hist]==dist
assert F(isolated,len(outcomes)**n)==F(n,m*m)*(1-F(2*m-1,m**4))**(n-1)
out['exhaustive']={'m':m,'n':n,'outcomes':len(outcomes)**n,'histogram':hist,'exact_distribution':[str(x) for x in dist],'isolated_mean':str(F(isolated,len(outcomes)**n))}
# Direct geometric waiting-time simulation, O(m) space/time per repetition.
rng=random.Random(216); data=[]
for m in [20,100,500,2000]:
 n=2*m**3; samples=[]
 for rep in range(300):
  trials=0;k=0
  for r in range(m,0,-1):
   p=r*r/m**4
   g=math.floor(math.log1p(-rng.random())/math.log1p(-p))+1
   trials+=g
   if trials>n:break
   k+=1
  samples.append(k/m)
 mean=sum(samples)/len(samples)
 sd=(sum((x-mean)**2 for x in samples)/(len(samples)-1))**.5
 data.append({'m':m,'n':n,'repetitions':len(samples),'mean_A_over_m':mean,'standard_error':sd/math.sqrt(len(samples)),'prediction':2/3})
out['simulation']=data
out['constants']={'isolated_unoptimized':math.exp(-2),'isolated_optimized':(3*math.e)**(-2/3),'greedy_optimized':2**(2/3)/3}
(R/'checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
