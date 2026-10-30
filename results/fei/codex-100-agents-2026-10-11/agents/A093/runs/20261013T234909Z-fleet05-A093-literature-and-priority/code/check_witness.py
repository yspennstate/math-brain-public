from fractions import Fraction as Q
from pathlib import Path
import json, time, hashlib
R=Path(__file__).resolve().parents[1]
start=time.perf_counter()
assert json.loads((R/'out/FROZEN_SPEC.json').read_text())['case_count']==1
checks=0
def check(x):
    global checks
    assert x
    checks+=1
def spectrum(values):
    m=len(values)
    return [Q(sum(v*(-1)**(s.bit_count()-(s&x).bit_count()) for x,v in enumerate(values)),m) for s in range(m)]
def log2(q):
    q=Q(q)
    check(q>0 and q.numerator&(q.numerator-1)==0 and q.denominator&(q.denominator-1)==0)
    return q.numerator.bit_length()-q.denominator.bit_length()
def entropy(probs):
    return sum((-p*log2(p) for p in probs if p),Q(0))
def h(t):return entropy([t,1-t])
f=[-1,-1,-1,1]
parent=spectrum(f)
# x index is bit 0: minus child x0=0, plus child x0=1.
b=spectrum([f[0],f[2]])
a=spectrum([f[1],f[3]])
check(parent==[Q(-1,2),Q(1,2),Q(1,2),Q(1,2)])
check(a==[0,1] and b==[-1,0])
Hp=entropy([c*c for c in parent]); Ha=entropy([c*c for c in a]); Hb=entropy([c*c for c in b])
delta=Hp-(Ha+Hb)/2
surrogate=Q(0); refund=Q(0); influence=Q(0)
for c,d in zip(a,b):
    z=c*c+d*d
    if z:
        surrogate+=z/2*h((c-d)**2/(2*z))
        refund+=z/2*(1-h(c*c/z))
    influence+=(c-d)**2/4
check(Hp==2 and Ha==0 and Hb==0)
check(delta==surrogate+refund)
check(delta==2 and surrogate==1 and refund==1 and influence==Q(1,2))
K=Q(2)
check(surrogate<=K*influence and delta>K*influence)
check(h(Q(1,2))==1)
# The square-root right side in printed (20) is exactly 1/2.
check(Q(1,2)**2==Q(1,2)*(1-Q(1,2)))
check(h(Q(1,2))>Q(1,2))
out={'status':'PASS','exact_assertions':checks,'seconds':time.perf_counter()-start,'truth_table':f,
     'parent_coefficients':list(map(str,parent)),'plus_coefficients':list(map(str,a)),
     'minus_coefficients':list(map(str,b)), 'H_parent':str(Hp),'H_children':[str(Ha),str(Hb)],
     'Delta_bits':str(delta),'surrogate_bits':str(surrogate),'refund_bits':str(refund),
     'query_influence':str(influence),'K':str(K),'same_K_equivalence':'REFUTED',
     'printed_binary_entropy_bound_at_half':'REFUTED','full_FEI':'NOT_REFUTED',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out/EXACT_WITNESS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out,indent=2))
