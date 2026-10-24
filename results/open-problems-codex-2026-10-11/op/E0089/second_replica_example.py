from fractions import Fraction as Q
from pathlib import Path
import json
E={(i,j) for i in range(4) for j in range(4,8)};H=(E-{(0,4),(1,5)})|{(0,1),(4,5)}
means=[];success=[]
for edges in [E,H]:
 adj=[sorted(w for a,b in edges for u,w in [(a,b),(b,a)] if u==v) for v in range(8)];q=Q(8,9);p=Q(1,4);mean=Q(0);af=Q(0)
 for mask in range(256):
  Z=[(mask>>v)&1 for v in range(8)];s=sum(Z)
  V1=[Z[v] and sum(Z[u] for u in adj[v])>=3 for v in range(8)]
  mean+=sum(V1)*q**s*(1-q)**(8-s)
  V=Z.copy()
  for _ in range(8):V=[V[v] and sum(V[u] for u in adj[v])>=3 for v in range(8)]
  if not any(V):af+=(1-p)**s*p**(8-s)
 means.append(mean);success.append(af)
h1=Q(16384,19683);assert means[0]==means[1]==8*h1
diff=success[1]-success[0];assert diff==10*p*p*(1-p)**6==Q(3645,32768)
var=diff*diff/4
Path('second_replica_example.json').write_text(json.dumps(dict(one_round_expected_counts=[str(x) for x in means],fixed_occupied_p=str(p),final_success_probabilities=[str(x) for x in success],difference=str(diff),annealed_independent_replica_final_covariance=str(var),note='Two graphs mixed equally; fixed deterministic p, not graph-specific median. Not an asymptotic counterexample.'),indent=2),encoding='utf8')
print('one-step means:',means,'final success difference:',diff,'replica covariance:',var,float(var))
