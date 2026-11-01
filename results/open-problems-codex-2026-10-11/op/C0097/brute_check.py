import json
from pathlib import Path
from memory_check import states, canonical, valid
d=4; tau=4; n=6
ws=states(tau); counts={w:0 for w in ws}
for w in ws:
 k=max(map(abs,w)); falling=1
 for j in range(k):falling*=d-j
 counts[w]=2**k*falling
for step in range(tau,n):
 nxt={w:0 for w in ws}
 for w,count in counts.items():
  k=max(map(abs,w));z=canonical((w+(k+1,))[-tau:]);nxt[z]+=count*2*(d-k)
  for a in list(range(1,k+1))+list(range(-k,0)):
   z=(w+(a,))[-tau:]
   if valid(z):nxt[canonical(z)]+=count
 counts=nxt
orbit=sum(counts.values())
# Independent concrete lattice enumeration: uses visited positions, not word validity.
paths=[[(0,)*d]]
for step in range(n):
 nxt=[]
 for path in paths:
  for axis in range(d):
   for sign in [-1,1]:
    endpoint=list(path[-1]);endpoint[axis]+=sign;endpoint=tuple(endpoint)
    if endpoint not in path[-tau:]:nxt.append((path+[endpoint])[-tau:])
 paths=nxt
brute=len(paths)
assert orbit==brute
result={'dimension':d,'memory':tau,'length':n,'orbit_count':orbit,'independent_concrete_count':brute,'equal':True}
Path('brute_result.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(result)
