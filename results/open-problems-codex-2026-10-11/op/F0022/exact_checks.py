from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
rows=[]
for p in [F(0),F(1,4),F(49,100),F(1,2),F(51,100),F(3,4),F(1)]:
 total=F(0); singleton=F(0); count=0
 for bits in product([0,1],repeat=7):
  n=sum(bits);w=p**n*(1-p)**(7-n);total+=w
  if bits[0]==1 and all(b==0 for b in bits[1:]):singleton+=w;count+=1
 assert total==1 and count==1 and singleton==p*(1-p)**6
 if F(1,4)<=p<=F(3,4):assert singleton>=F(1,16384)
 rows.append({'p':str(p),'singleton_probability':str(singleton),'decimal':float(singleton)})
assert rows[3]['singleton_probability']=='1/128'
steps=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
def nbr(v):return {(v[0]+a,v[1]+b) for a,b in steps}
sets={frozenset({(0,0)})}; trunc=F(0);animals=[]
for n in range(1,6):
 assert all(len(s)==n for s in sets)
 t=F(0); hist={}
 for s in sets:
  b=set().union(*(nbr(v) for v in s))-set(s);k=len(b);hist[k]=hist.get(k,0)+1;t+=F(1,n)*F(1,2)**(n+k)
 trunc+=t;animals.append({'size':n,'rooted_animals':len(sets),'boundary_histogram':hist,'contribution_at_half':str(t),'partial_kappa':str(trunc)})
 sets={s|{v} for s in sets for v in set().union(*(nbr(w) for w in s))-set(s)}
assert animals[0]['contribution_at_half']=='1/128'
assert animals[1]['rooted_animals']==6 and animals[1]['contribution_at_half']=='3/1024'
Path('exact_checks.json').write_text(json.dumps({'local_128_configuration_checks':rows,'finite_cluster_enumeration':animals},indent=2),encoding='utf-8')
print(json.dumps(animals,indent=2));print('All exact assertions passed')
