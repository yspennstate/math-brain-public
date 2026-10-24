"""Small checks of partial results; no test-bank material is used."""
import os
for option in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[option] = '1'
import collections
from fractions import Fraction
import itertools
import json
import math
import pathlib
import numpy as np
from scipy.optimize import brentq, root

here = pathlib.Path(__file__).resolve().parent
output = here / 'special_case_measurements.jsonl'
records = []
def save(record):
    records.append(record)
    with output.open('a', encoding='utf-8') as file:
        file.write(json.dumps(record) + '\n')
output.write_text('', encoding='utf-8')

t = [Fraction(j) for j in (1,2,3)]
u = [Fraction(j) for j in (1,0,1)]
mean_u = sum(u)/3
ratio = sum(a*b for a,b in zip(t,u))/sum(t)
assert mean_u == ratio == Fraction(2,3)
assert Fraction(0) != Fraction(1,3) * Fraction(2,3)
save({'problem_id':'C0004','mean_of_normalized_mass':str(mean_u),'normalized_mean_mass':str(ratio),'independent':False,'joint_T2_U1':'0','product_of_marginals':'2/9','label':'exact rational counterexample'})

values = np.array([0.,2.])
probabilities = np.array([.75,.25])
mean = float(probabilities @ values)
central = values - mean
mu2, mu3, mu5 = [float(probabilities @ central**k) for k in (2,3,5)]
for variance in (50.,100.,200.,400.,800.):
    classical = brentq(lambda x: float(probabilities @ ((values-x) * np.exp(-(values-x)**2/(2*variance)))), values.min(), values.max(), xtol=1e-14)
    def free_equations(z):
        q, scaled_w = z
        denominator = scaled_w + (q-values)**2/variance
        return [float(probabilities @ (1/denominator))-1, float(probabilities @ ((q-values)/denominator**2))]
    result = root(free_equations, [mean-2*mu3/variance,1-mu2/variance], tol=1e-11)
    assert result.success and np.max(np.abs(free_equations(result.x))) < 1e-10
    q, scaled_w = result.x
    free = q + float(probabilities @ ((q-values)/(scaled_w+(q-values)**2/variance)))
    classical_second = (classical-mean+mu3/(2*variance))*variance**2
    free_second = (free-mean+3*mu3/variance)*variance**2
    save({'problem_id':'P0177','t':variance,'mean':mean,'mu2':mu2,'mu3':mu3,'mu5':mu5,'classical_mode':classical,'free_mode':free,'t_classical_shift':variance*(classical-mean),'t_free_shift':variance*(free-mean),'classical_scaled_second_error':classical_second,'free_scaled_second_error':free_second,'predicted_classical_second':(mu5-6*mu2*mu3)/8,'predicted_free_second':5*mu5-22*mu2*mu3,'label':'numerical check of asymptotic coefficients'})

for degree in (3,4,8):
    offspring = degree-1
    critical = 1/offspring
    expected_slope = 2*degree*(degree-1)/(degree-2)
    for epsilon in (1e-3,1e-4,1e-5):
        p = critical+epsilon
        extinction_complement = brentq(lambda x: -math.expm1(offspring*math.log1p(-p*x))/x-1, 1e-12, 1., xtol=1e-14)
        theta = -math.expm1(degree*math.log1p(-p*extinction_complement))
        save({'problem_id':'C0063','tree_degree':degree,'epsilon':epsilon,'theta_over_epsilon':theta/epsilon,'predicted_slope':expected_slope,'label':'tree special case only'})

def tree_and_components(n, weighted_edges, threshold=None):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    tree = []
    for a,b,weight in sorted(weighted_edges,key=lambda edge:edge[2]):
        if threshold is not None and weight>threshold:
            continue
        x,y = find(a),find(b)
        if x!=y:
            parent[x]=y
            tree.append((a,b,weight))
    return tree, [find(j) for j in range(n)]
def intrinsic_diameters(n, edges):
    adjacency = [[] for _ in range(n)]
    for a,b,*_ in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    max_distance = 0
    for start in range(n):
        distances = {start:0}
        queue = collections.deque([start])
        while queue:
            a=queue.popleft()
            for b in adjacency[a]:
                if b not in distances:
                    distances[b]=distances[a]+1
                    queue.append(b)
        max_distance=max(max_distance,max(distances.values()))
    return max_distance
edge_pairs = list(itertools.combinations(range(4),2))
rng = np.random.default_rng(344)
graphs, cutoff_checks = 0,0
for mask in range(1,2**len(edge_pairs)):
    pairs=[edge_pairs[j] for j in range(6) if mask>>j&1]
    weights=rng.permutation(len(pairs))+1
    edges=[(*pair,int(w)) for pair,w in zip(pairs,weights)]
    mst,components=tree_and_components(4,edges)
    if len(set(components))>1:
        continue
    graphs+=1
    for threshold in range(len(edges)+1):
        subgraph=[edge for edge in edges if edge[2]<=threshold]
        assert intrinsic_diameters(4,subgraph)<=intrinsic_diameters(4,mst)
        cutoff_checks+=1
save({'problem_id':'C0087','connected_four_vertex_graphs':graphs,'cutoff_checks':cutoff_checks,'label':'finite check of deterministic lower-bound transfer'})
for n in (4,8,16):
    edges=[(a,b,(a+1 if b==a+1 else n+a*n+b)) for a,b in itertools.combinations(range(n),2)]
    mst,_=tree_and_components(n,edges)
    assert intrinsic_diameters(n,mst)==n-1 and intrinsic_diameters(n,edges)==1
    save({'problem_id':'C0087','complete_graph_vertices':n,'sublevel_intrinsic_diameter':1,'mst_diameter':n-1,'label':'exact counterexample to reversing the diameter comparison'})

for degree in (3,4,8):
    cheeger=degree-2
    assert Fraction(1,cheeger+1)==Fraction(1,degree-1)
    save({'problem_id':'C0139','regular_tree_degree':degree,'edge_cheeger_constant':cheeger,'pc_bound':str(Fraction(1,cheeger+1)),'actual_pc':str(Fraction(1,degree-1)),'label':'sharp nonamenable tree boundary case'})

for n in (64,128,256):
    norms=[]
    for _ in range(48):
        edge_variables=rng.choice(np.array([-1,1],dtype=np.int8),size=(n,n))
        upper=np.triu(edge_variables,1)
        degrees=(upper+upper.T).sum(axis=1)
        norms.append(int(np.abs(degrees).max()))
    expected=float(np.mean(norms))
    baseline=math.sqrt(n*(n-1))
    save({'problem_id':'P0018','n':n,'samples':48,'sample_mean_norm':expected,'old_frobenius_upper_bound':baseline,'baseline_to_observed_ratio':baseline/expected,'mean_over_sqrt_n_log_n':expected/math.sqrt(n*math.log(n)),'label':'numerical shape example, not a general graph-matrix asymptotic'})

rate=math.pi**2/2
for elapsed in (1.,2.,3.):
    survival=sum(4/math.pi * (-1)**k/(2*k+1)*math.cos((2*k+1)*math.pi/4)*math.exp(-(2*k+1)**2*rate*elapsed) for k in range(8))
    save({'problem_id':'P0023','interval_length':1,'x':.25,'t':elapsed,'generator':'Delta/2','spectral_rate':rate,'scaled_survival':survival*math.exp(rate*elapsed),'predicted_limit':4/math.pi*math.cos(math.pi/4),'label':'one-dimensional reflection-coupling control'})

for n in (4,8,16):
    edges=[(j,j+1,1) for j in range(n-1)]
    _,whole=tree_and_components(n,edges)
    _,cut=tree_and_components(n,[edge for edge in edges if edge[:2]!=(0,1)])
    assert len(set(whole))==1 and len(set(cut))==2
save({'problem_id':'P0047','finite_edge_change_checks':3,'counts_before_after':[1,2],'label':'count is not generically invariant under finite changes; no claim that this toy law is FUSF'})
print(json.dumps({'records':len(records),'problem_ids':sorted({r['problem_id'] for r in records}),'free_mode_last_record':[r for r in records if r['problem_id']=='P0177'][-1],'shape_records':[r for r in records if r['problem_id']=='P0018']}))
