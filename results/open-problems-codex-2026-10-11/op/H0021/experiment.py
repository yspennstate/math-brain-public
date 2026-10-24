import itertools,math,json,time,random,pathlib
import networkx as nx
started=time.time();out={}
# Exact embedding by permuting vertices; masks avoid reliance on graph-isomorphism heuristics.
n=5;edges=list(itertools.combinations(range(n),2));edgeidx={e:i for i,e in enumerate(edges)}
trees=list(nx.nonisomorphic_trees(n));t3=[t for t in trees if max(dict(t.degree()).values())<=3]
def copy_masks(t):
 masks=set()
 for a in itertools.permutations(range(n)):
  masks.add(sum(1<<edgeidx[tuple(sorted((a[u],a[v])))] for u,v in t.edges()))
 return masks
families=[copy_masks(t) for t in t3];paths=copy_masks(nx.path_graph(n))
counts={'path_by_edges':[0]*11,'universal3_by_edges':[0]*11,'path_not_universal3_by_edges':[0]*11}
for g in range(1<<len(edges)):
 m=g.bit_count();hp=any((g&t)==t for t in paths);u3=all(any((g&t)==t for t in f) for f in families)
 counts['path_by_edges'][m]+=int(hp);counts['universal3_by_edges'][m]+=int(u3);counts['path_not_universal3_by_edges'][m]+=int(hp and not u3)
assert all(counts['universal3_by_edges'][i]<=counts['path_by_edges'][i] for i in range(11))
out['exact_n5']={'graphs':1024,'tree_types_degree3':len(t3),**counts}
# Exhaustively check isolation covariance and fixed-reservoir moments in all n=5 graphs.
p=.23;R={0,1};ex=ex2=ey=ey2=0.
for g in range(1024):
 adj=[set() for _ in range(n)]
 for i,(u,v) in enumerate(edges):
  if g>>i&1:adj[u].add(v);adj[v].add(u)
 w=p**g.bit_count()*(1-p)**(10-g.bit_count());x=sum(not a for a in adj);y=sum(not(adj[v]&R) for v in range(n) if v not in R)
 ex+=w*x;ex2+=w*x*x;ey+=w*y;ey2+=w*y*y
A=(1-p)**(n-1);mu=n*A;var=n*A*(1-A)+n*(n-1)*A*A*p/(1-p)
y_mu=(n-len(R))*(1-p)**len(R);y_var=y_mu*(1-(1-p)**len(R))
assert max(abs(ex-mu),abs(ex2-ex*ex-var),abs(ey-y_mu),abs(ey2-ey*ey-y_var))<1e-10
out['moment_checks']={'p':p,'EX':ex,'VarX':ex2-ex*ex,'EY':ey,'VarY':ey2-ey*ey,'all_formula_errors_under':1e-10}
# Bounded stochastic checks of repair, not tests of an asymptotic threshold.
rng=random.Random(210012);trials=[]
for n in [500,2000,8000]:
 c=1.5;k=2;L=math.log(n);ell=math.log(L);lam=ell+(k+2)*math.log(ell);q=lam/(c*L);p=c*L/n
 for rep in range(3):
  G=nx.fast_gnp_random_graph(n,p,seed=rng.randrange(2**32));R={v for v in G if rng.random()<q};B={v for v in G if v not in R and len(R.intersection(G[v]))<k};md=min(dict(G.degree()).values());S=set(R)
  if md>=k:
   for v in B:S.update(list(G[v])[:k])
   assert len(S)<=len(R)+k*len(B)
   assert all(len(S.intersection(G[v]))>=k for v in G if v not in S)
  trials.append(dict(n=n,c=c,k=k,q=q,p=p,minimum_degree=md,initial_size=len(R),bad_size=len(B),repaired_size=len(S),M=n*ell/(c*L),checked=md>=k))
out['repair_trials']=trials
# Numerical stability of the asymptotic bounds at astronomical sizes, represented via log n.
rows=[]
for L in [100.,1000.,10000.,1e6]:
 ell=math.log(L);k=2;lam=ell+(k+2)*math.log(ell);poissonbad=math.exp(-lam)*sum(lam**j/math.factorial(j) for j in range(k));delta=.2
 rows.append({'log_n':L,'q_over_ell_div_cL':lam/ell,'expected_bad_over_M':1.5*L*poissonbad/ell,'lower_bound_positive_to_negative_scale':ell**2/L**delta})
out['asymptotic_scale_checks']=rows;out['elapsed_seconds']=time.time()-started
pathlib.Path('experiment_results.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
