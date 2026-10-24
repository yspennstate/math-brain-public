from pathlib import Path
from fractions import Fraction as Q
import json
p=Path('second_replica_example.json');d=json.loads(p.read_text());E={(i,j) for i in range(4) for j in range(4,8)};H=(E-{(0,4),(1,5)})|{(0,1),(4,5)};q=Q(8,9)
vals=[]
for edges in [E,H]:
 adj=[sorted(w for a,b in edges for u,w in [(a,b),(b,a)] if u==v) for v in range(8)]
 eh=Q(0);em=Q(0);ehm=Q(0)
 for mask in range(256):
  Z=[(mask>>v)&1 for v in range(8)];M=sum(Z);H1=sum(Z[v] and sum(Z[u] for u in adj[v])>=3 for v in range(8));weight=q**M*(1-q)**(8-M)
  eh+=weight*H1;em+=weight*M;ehm+=weight*H1*M
 cov=ehm-eh*em;deriv=16*q**3-15*q**4
 assert cov==8*q*(1-q)*deriv
 vals.append(str(cov))
d['one_round_count_initial_count_covariances']=vals;d['checked_identity']='Cov(H1,M)=n q(1-q) h1 derivative, exactly on both 8-vertex graphs'
p.write_text(json.dumps(d,indent=2),encoding='utf8');print(d['checked_identity'],vals)
