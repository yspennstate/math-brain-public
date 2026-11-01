import itertools,math,json,pathlib
r=.75;t=.05;a=.105;b=.755
P=[[1-(1-r)*t,(1-r)*t],[(1-r)*(1-t),r+(1-r)*t]]
# Enumerate the 4-vertex star's hidden spins and noisy observed spins.
edges=[(0,1),(0,2),(0,3)];n=4
prob={x:0. for x in itertools.product([0,1],repeat=n)}
for s in itertools.product([0,1],repeat=n):
 weight=(t if s[0] else 1-t)*math.prod(P[s[u]][s[v]] for u,v in edges)
 for x in prob:
  prob[x]+=weight*math.prod((b if s[i] else a) if x[i] else 1-(b if s[i] else a) for i in range(n))
assert abs(sum(prob.values())-1)<1e-12
worst=1.;pairs=0
for x,y in itertools.product(prob,repeat=2):
 meet=tuple(min(xx,yy) for xx,yy in zip(x,y));join=tuple(max(xx,yy) for xx,yy in zip(x,y))
 lhs=prob[meet]*prob[join];rhs=prob[x]*prob[y]
 assert lhs+1e-14>=rhs
 worst=min(worst,lhs/rhs if rhs else 1);pairs+=1
out={'finite_hidden_star_probability_sum':sum(prob.values()),'log_supermodularity_pairs':pairs,'minimum_lhs_rhs_ratio':worst,'passed':True,'scope':'sanity check only; association proof is analytic'}
pathlib.Path('second_fkg_checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
