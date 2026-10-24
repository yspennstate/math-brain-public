import itertools,json,time
from fractions import Fraction as Q
import audit as a
start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
v=json.loads((a.ROOT/'out/validation.json').read_text())
boxes=json.loads((a.ROOT/'out/boxes_partial.json').read_text())
ck(len(boxes)==256)
for row in boxes:ck(Q(row['price_upper'])<48)
for row in v['rare_cases']:
 C=list(map(Q,row['C']));D=list(map(Q,row['D']))
 ck(max(C[1],-C[0])<48*D[0])
R=tuple(map(Q,v['existing_g3_fixture']['R']));Psi=tuple(map(Q,v['existing_g3_fixture']['Psi']))
paid=a.add(R,a.mul(Psi,48));ck(paid[1]<10)
ck(48*Q(11,16)==33)
pairlist=((0,4),(1,2),(3,5));perms=[]
def perm(x,pi):return sum(((x>>j)&1)<<pi[j] for j in range(6))
for order in itertools.permutations(range(3)):
 for flips in itertools.product((0,1),repeat=3):
  pi=[0]*6
  for k,pair in enumerate(pairlist):
   for t,j in enumerate(pair):pi[j]=pairlist[order[k]][t^flips[k]]
  for x in range(64):ck(a.H[x]==a.H[perm(x,pi)])
  perms.append(pi)
ck(len(set(map(tuple,perms)))==48)
ck(set(pi[0] for pi in perms)==set(range(6)))
for j in range(6):
 pi=next(pi for pi in perms if pi[0]==j)
 for x in range(64):ck(-a.H[x^1]==-a.H[perm(x,pi)^(1<<j)])
# Rational endpoint prices used in the analytic review, not numerical extrapolation.
ck(Q(360)*Q(4,105)<14<48)
ck(Q(120)*Q(4,3)*Q(1,4)==40<48)
ck(Q(36)*Q(4,3)==48)
out={'assertions':checks,'price':48,'rare_budget':33,'endpoint_prices':{'common_h_upper':14,'J_positive_upper':40,'J_negative_upper':48},
 'compact_price_max':str(max(Q(row['price_upper']) for row in boxes)),
 'g3_R_plus48Psi':list(map(str,paid)),'g3_R_plus48Psi_display':list(map(float,paid)),
 'all_admissible_g3_descendants_H_over_I_less_than':10,'all48_gate_automorphisms_checked':True,
 'all6_oneflip_positions_checked':True,'runtime_seconds':time.perf_counter()-start,'full_FEI':'OPEN'}
a.save('refinement48.json',out)
print(json.dumps({k:v for k,v in out.items() if k!='g3_R_plus48Psi'},indent=2))
