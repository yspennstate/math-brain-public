from pathlib import Path
from fractions import Fraction as Q
import json,time
import primitives as z
start=time.monotonic()
labels=tuple(1 if (x&1)==0 and (x>>1&1)==0 else 2 if (x&1)==0 and (x>>2&1)==0 else 0 for x in range(8))
u=(1,1,1,-1);v=(1,)
q=Q(1,4);m=beta=Q(1,2)
aa=tuple(m if h==1 else 1 for h in labels);cc=tuple(int(h==1) for h in labels)
aw,cw=z.walsh(aa),z.walsh(cc)
mix=tuple(a*a+beta*beta*c*c for a,c in zip(aw,cw))
plus=tuple((a+beta*c)**2 for a,c in zip(aw,cw));minus=tuple((a-beta*c)**2 for a,c in zip(aw,cw))
M,mp,mm=sum(mix),sum(plus),sum(minus);rp,rm=mp/(2*M),mm/(2*M)
assert (M,mp,mm,rp,rm)==(Q(7,8),Q(1),Q(3,4),Q(4,7),Q(3,7))
def ent(a):return z.add(*(z.phi(x) for x in a))
J=z.add(ent(mix),z.scale(z.add(ent(plus),ent(minus)),Q(-1,2)))
JS=z.add(ent(tuple(x/M for x in mix)),z.scale(ent(tuple(x/mp for x in plus)),-rp),z.scale(ent(tuple(x/mm for x in minus)),-rm))
correction=z.add(z.scale(z.log(2),M),z.scale(z.packet(rp,rm),-M))
assert J==z.add(z.scale(JS,M),correction)
assert correction==z.add(z.scale(z.log(2),Q(15,8)),z.scale(z.log(3),Q(3,8)),z.scale(z.log(7),Q(-7,8)))
assert z.le({},correction) and z.interval(correction)[0]>0
def F(c,a,b):return tuple(1 if h==0 else a[i] if h==1 else b[j] for h in c for j in range(len(b)) for i in range(len(a)))
datafirst=z.scale(z.add(*(z.raw(z.walsh(F(labels,(a,),(b,)))) for a in u for b in u)),Q(1,16))
controlfirst=z.scale(z.raw(z.walsh(u)),Q(3,8))
expected=z.add(z.scale(z.log(2),Q(11,8)),z.scale(z.log(3),Q(-9,32)))
assert datafirst==expected and controlfirst==z.scale(z.log(2),Q(3,4))
assert z.interval(z.add(datafirst,z.scale(controlfirst,-1)))[0]>0
result={'status':'PASS','exact_assertions':8,'elapsed_seconds':time.monotonic()-start,'projected_mass_fixture':{'M':'7/8','M_plus':'1','M_minus':'3/4','rho_plus':'4/7','rho_minus':'3/7','physical_weights':['1/2','1/2'],'mass_correction_prime_log':{str(p):str(c) for p,c in correction.items()}},'frontier_fixture':{'data_first_bits':'11/8-(9/32)log2(3)','control_first_bits':'3/4','difference_positive':True},'scope':'Independent reconstruction of A087 projected mass/frontier fixtures; no source repair'}
(Path(__file__).resolve().parents[1]/'out'/'REVIEW_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
