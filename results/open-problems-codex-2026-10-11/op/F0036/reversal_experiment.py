import random,json,pathlib
rng=random.Random(3612)
checks=[]
for trial in range(500):
 L=rng.choice([7,9,11]); U=rng.randrange(4,10); s=rng.randrange(1,U-2)
 edges={}; occ=[set(range(0,L,2))]; pred={}
 for t in range(U):
  nxt=set()
  for x in sorted(occ[-1]):
   k=rng.randrange(3); ys=([x-1] if k==0 else [x+1] if k==1 else [x-1,x+1]); ys=[y for y in ys if 0<=y<L]
   if not ys: ys=[1 if x==0 else L-2]
   edges[t,x]=ys
   for y in ys: nxt.add(y); pred.setdefault((t+1,y),[]).append(x)
  occ.append(nxt)
 A={(x,y) for x in occ[s] for y in occ[s] if x<y}; meetings=set()
 for t in range(s,U-1):
  new=set()
  for x,y in A:
   for p in edges[t,x]:
    for q in edges[t,y]:
     if p==q: meetings.add((p,t+1))
     if p<q: new.add((p,q))
  A=new
 forks=set()
 for t in range(s+1,U):
  for x in occ[t]:
   lo=hi=x; survive=True
   for v in range(t,s,-1):
    lo=min(pred[v,lo]); hi=max(pred[v,hi])
    if lo>=hi: survive=False; break
   if survive: forks.add((x,t))
 assert meetings==forks,(trial,meetings,forks)
 checks.append({'trial':trial,'L':L,'U':U,'s':s,'contacts':len(meetings)})
result={'seed':3612,'trials':500,'mismatches':0,'total_contacts':sum(x['contacts'] for x in checks),'meaning':'Contacts with two histories separated since a positive cut equal surviving forks in the reversed occupied image. This checks geometry, not Brownian-net reversal in law.','checks':checks}
pathlib.Path('reversal_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print({k:v for k,v in result.items() if k!='checks'})
