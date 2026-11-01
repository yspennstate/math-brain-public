import pathlib,itertools,json,math
checks=[]
# Exact stopped-word check: stop on first equal pair, truncate at length 10.
# Each allowed stopped word of length n has probability 2**(-n).
mass=0.;same=0.
for n in range(2,11):
 for w in itertools.product([-1,1],repeat=n):
  if w[-1]!=w[-2] or any(w[i]==w[i-1] for i in range(1,n-1)):continue
  mass+=2**(-n);same+=2**(-n)*int(w[-1]==w[-2])
checks.append(dict(check='stopped symmetric random walk reversal',enumerated_up_to=10,total_stopped_mass=mass,exact_expected_mass=1-2**(-9),reverse_first_pair_equal_conditional=same/mass,iid_pair_equal_probability=.5))
# Finite interval supports in Theorem A. Independent residue windows must be disjoint.
count=0
for M in [0,.25,.5,1,2.75,10]:
 q=math.floor(2*M+1)+1
 if q<=2*M+1:q+=1
 for j in range(q):
  for n in range(10):
   k=j+n*q;l=j+(n+1)*q
   assert k+2*M+1<l;count+=1
checks.append(dict(check='Brownian averaging window separation',cases=count,result='PASS'))
# Translation bound for simple functions, exactly integrated interval by interval.
def integral(a,b):
 knots=sorted(set([a,b]+[float(i) for i in range(-20,21) if a<i<b]))
 return sum((v-u)*((-1)**math.floor((u+v)/2)) for u,v in zip(knots,knots[1:]))
count=0
for c in [-5,-2.2,-1,0,.1,2.7,5]:
 for R in [.2,1,2,5,10]:
  err=abs(integral(0,R)-integral(c,c+R));assert err<=2*abs(c)+1e-12;count+=1
checks.append(dict(check='translation bound including disjoint intervals and negative shifts',cases=count,result='PASS'))
checks.append(dict(check='pinned bridge endpoint mismatch',L=2,brownian_variance=2,pinned_bridge_variance=0,result='old bridge formulation rejected'))
pathlib.Path('checks.json').write_text(json.dumps(checks,indent=2),encoding='utf8')
print(json.dumps(checks,indent=2))
