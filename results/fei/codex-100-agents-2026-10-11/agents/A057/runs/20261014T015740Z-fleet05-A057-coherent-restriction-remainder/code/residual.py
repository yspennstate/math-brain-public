from pathlib import Path
from fractions import Fraction as Q
import json
import primitives as z
labels=tuple(1 if (k>>1&1 if k&1==0 else k>>2&1)==0 else 2 for k in range(8))
u=v=(1,-1)
def F(c):return tuple(u[i] if a==1 else v[j] for a in c for j in range(2) for i in range(2))
f=F(labels);w=z.walsh(f);children=[F(labels[b::2]) for b in [0,1]]
assert sorted(abs(a) for a in w if a)==[Q(1,4)]*8+[Q(1,2)]*2
assert z.raw(w)==z.scale(z.log(2),3)
assert all(z.raw(z.walsh(c))==z.scale(z.log(2),2) for c in children)
assert Q(sum(f[k]!=f[k^4] for k in range(len(f))),len(f))==Q(1,4)
q=Q(labels.count(1),len(labels));qs=[Q(labels[b::2].count(1),len(labels)//2) for b in [0,1]]
assert q==Q(1,2) and qs==[q,q]
R=z.add(z.phi(q),z.phi(1-q))
assert R==z.log(2)
B=z.add(*(z.packet(w[k]**2,w[k|4]**2) for k in range(len(w)) if not k&4))
assert B==z.scale(z.log(2),Q(1,2))
out={'status':'PASS','assertions':7,'physical_dimension':5,'source_fixture':'A030 arbitrary-controller two-dictator wrapper, with h a two-address mux','H_parent_bits':'3','H_children_bits':['2','2'],'controller_entropy_decrement_bits':'1','controller_erasure_bits':'1/2','queried_influence':'1/4','R_parent_bits':'1','R_children_bits':['1','1'],'R_release_bits':'0','conclusion':'No release-only payment of controller decrement; inherited controller entropy remains'}
(Path(__file__).resolve().parents[1]/'out'/'RESIDUAL.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
