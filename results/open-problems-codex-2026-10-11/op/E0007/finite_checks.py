import itertools,json,time
from fractions import Fraction as Q
from pathlib import Path
start=time.time();L=3;n=4;V=9
nb=[[(y*L+(x+1)%L),(y*L+(x-1)%L),(((y+1)%L)*L+x),(((y-1)%L)*L+x)] for y in range(L) for x in range(L)]
def pairs(s):return sum(sum(s[j]==2 for j in nb[i]) for i in range(V) if s[i]==2)
count=transitions=0
for state in itertools.product(range(3),repeat=V):
 s=list(state);C=pairs(s);N=sum(z==2 for z in s)
 birth_sum=vac_square=0
 for i in range(V):
  m=sum(s[j]==2 for j in nb[i])
  if s[i]==0:
   birth_sum+=m;vac_square+=m*m
   if m:
    s[i]=2;assert pairs(s)-C==2*m;s[i]=0;transitions+=1
  elif s[i]==2:
   s[i]=0;assert pairs(s)-C==-2*m;s[i]=2;transitions+=1
 assert birth_sum<=n*N-C
 assert vac_square>=birth_sum
 count+=1
# coefficients checked in exact rational arithmetic across a parameter grid
algebra=0
for degree in [2,4,6,8]:
 for delta in [Q(1,3),Q(1),Q(3)]:
  for f in [Q(1,10),Q(1,2),Q(9,10),Q(999,1000)]:
   beta=f*degree*delta/(degree-1)
   a=degree*beta/(2*(degree*delta+beta));k=1-2*a/degree
   gamma=delta*(degree*delta-(degree-1)*beta)/(degree*delta+beta)
   assert 0<a<Q(1,2) and k>0 and gamma>0
   assert 2*a*delta-k*beta==0 and k*beta-delta==-gamma
   algebra+=1
stripe=[1,1,1,0,2,0]
rho={i:Q(stripe.count(i),6) for i in [1,2]}
qs={}
for typ in [1,2]:
 incid=sum((stripe[(x-1)%6]==0)+(stripe[(x+1)%6]==0) for x in range(6) if stripe[x]==typ)
 qs[typ]=Q(incid,4*stripe.count(typ))
assert qs[1]==Q(1,6) and qs[2]==Q(1,2)
result={'states_exhaustively_checked':count,'pair_transitions_checked':transitions,'rational_coefficient_cases':algebra,'stripe_rho':{str(i):str(v) for i,v in rho.items()},'stripe_q':{str(i):str(v) for i,v in qs.items()},'two_vertex_last_type1_probability':str(Q(1,5)),'elapsed_seconds':time.time()-start,'scope':'finite generator and algebra verification; no infinite-volume conclusion from computation'}
Path('checks.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(result)
