"""Seeded cubic-graph evidence. Single process, one numerical thread.

All fixed local rules use IID labels and bounded numbers of rounds. The
nonlocal heuristic comparator is explicitly separate. Graph sampling is
uniform configuration pairing conditioned on simplicity, without repair.
"""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
    os.environ[key]='1'
import itertools
import json
import math
import random
import resource
import statistics
import time
from functools import lru_cache
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix
import warnings

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'/'final'
SEED=15120261113

def graph(n,seed):
    rng=random.Random(seed); attempts=0
    while True:
        attempts+=1; stubs=list(range(n))*3; rng.shuffle(stubs)
        adj=[set() for _ in range(n)]; edges=[]
        for u,v in zip(stubs[::2],stubs[1::2]):
            if u==v or v in adj[u]:break
            adj[u].add(v);adj[v].add(u);edges.append((min(u,v),max(u,v)))
        else:
            assert all(len(a)==3 for a in adj)
            return [sorted(a) for a in adj],sorted(edges),attempts

def valid(adj,S):
    assert all(not (set(adj[u])&S) for u in S)

def parallel_greedy(adj,rng,rounds=16):
    active=set(range(len(adj))); S=set()
    for _ in range(rounds):
        keys={v:rng.random() for v in active}
        chosen={v for v in active if all(keys[v]<keys[w] for w in adj[v] if w in active)}
        S|=chosen
        active-=chosen|{w for v in chosen for w in adj[v]}
    return S

def gaussian(adj,rng,radius):
    n=len(adj); neigh=np.array(adj)
    radial=np.zeros((radius+1,radius+1))
    for k in range(radius):
        radial[k,k+1]=radial[k+1,k]=math.sqrt(3 if k==0 else 2)
    _,vec=np.linalg.eigh(radial)
    coeff=vec[:,0]/np.sqrt([1]+[3*2**(k-1) for k in range(1,radius+1)])
    z=rng.standard_normal(n); previous=z; out=coeff[0]*z
    if radius:
        current=z[neigh].sum(axis=1);out=out+coeff[1]*current
    for k in range(2,radius+1):
        new=current[neigh].sum(axis=1)-(3 if k==2 else 2)*previous
        out+=coeff[k]*new;previous,current=current,new
    # A local polynomial kills the trivial eigenvalue d. Without this step,
    # large-radius polynomials amplify the graph-wide constant component.
    out=out[neigh].sum(axis=1)-3*out
    return {v for v in range(n) if all(out[v]>out[w] for w in adj[v])}

def local_improve(adj,S,rng,rounds=2):
    """Parallel 1->2 swaps with IID conflict resolution, then local filling.

    One proposal per occupied centre. Keep proposals whose fresh IID key is
    smaller than every proposal with overlapping or adjacent added vertices.
    Conflict tests are local: proposed vertices are adjacent to their centre.
    """
    S=set(S);n=len(adj)
    for _ in range(rounds):
        occ=[set(a)&S for a in adj]; proposals={}
        pair_keys=[rng.random() for _ in adj]
        for v in S:
            eligible=[u for u in adj[v] if occ[u]=={v}]
            pairs=[(a,b) for a,b in itertools.combinations(eligible,2) if b not in adj[a]]
            if pairs:proposals[v]=min(pairs,key=lambda pair:pair_keys[pair[0]]+pair_keys[pair[1]])
        keys={v:rng.random() for v in proposals}
        owners={}
        for v,pair in proposals.items():
            for u in pair: owners.setdefault(u,set()).add(v)
        accept=[]
        for v,pair in proposals.items():
            conflicts=set()
            for u in pair:
                for w in [u]+adj[u]:conflicts.update(owners.get(w,()))
            if all(keys[v]<keys[w] for w in conflicts if w!=v):accept.append(v)
        for v in accept:S.remove(v)
        for v in accept:S.update(proposals[v])
        free={v for v in range(n) if v not in S and not set(adj[v])&S}
        keys={v:rng.random() for v in free}
        S|={v for v in free if all(keys[v]<keys[w] for w in adj[v] if w in free)}
        valid(adj,S)
    return S

def min_degree(adj,rng):
    active=set(range(len(adj)));S=set()
    while active:
        degrees={v:len(set(adj[v])&active) for v in active}
        degree=min(degrees.values());v=rng.choice([v for v in active if degrees[v]==degree])
        S.add(v);active.discard(v);active.difference_update(adj[v])
    return S

def heuristic(adj,seed,restarts=24):
    rng=random.Random(seed);best=set()
    for _ in range(restarts):
        S=local_improve(adj,min_degree(adj,rng),rng,8)
        if len(S)>len(best):best=S
    # Global annealing comparator. No claim that best-of-run selection is FIID.
    for run in range(4):
        S=set(best)
        for step in range(100*len(adj)):
            v=rng.randrange(len(adj));T=.3*(.025/.3)**(step/(100*len(adj)))
            if v in S:
                if rng.random()<math.exp(-1/T):S.remove(v)
            else:
                blocked=set(adj[v])&S;delta=1-len(blocked)
                if delta>=0 or rng.random()<math.exp(delta/T):
                    S.difference_update(blocked);S.add(v)
                    if len(S)>len(best):best=set(S)
        valid(adj,S)
    best=local_improve(adj,best,rng,8)
    return best

def exact(adj):
    """Include/exclude recursion with safe leaf reductions and components."""
    masks=[sum(1<<w for w in a) for a in adj]
    nodes=0
    @lru_cache(maxsize=150000)
    def solve(mask):
        nonlocal nodes
        nodes+=1
        if not mask:return 0
        vertices=[v for v in range(len(adj)) if mask>>v&1]
        for v in vertices:
            if (masks[v]&mask).bit_count()<=1:
                return (1<<v)|solve(mask&~((1<<v)|masks[v]))
        component=0;front=mask&-mask
        while front:
            bit=front&-front;front-=bit;v=bit.bit_length()-1
            component|=bit;front|=(masks[v]&mask&~component)
        if component!=mask:return solve(component)|solve(mask&~component)
        v=max(vertices,key=lambda w:(masks[w]&mask).bit_count())
        yes=(1<<v)|solve(mask&~((1<<v)|masks[v]));no=solve(mask&~(1<<v))
        return yes if yes.bit_count()>=no.bit_count() else no
    answer=solve((1<<len(adj))-1)
    return {v for v in range(len(adj)) if answer>>v&1},nodes

def milp_check(adj,edges):
    n=len(adj);A=lil_matrix((len(edges),n))
    for i,(u,v) in enumerate(edges):A[i,u]=A[i,v]=1
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore',message='Unrecognized options detected')
        result=milp(-np.ones(n),integrality=np.ones(n),bounds=Bounds(0,1),
                    constraints=LinearConstraint(A.tocsr(),-np.inf,1),
                    options={'threads':1,'time_limit':30,'mip_rel_gap':0})
    assert result.status==0,str(result.message)
    S={v for v in range(n) if result.x[v]>.5};valid(adj,S)
    return len(S)

def run_local(adj,seed,radius,improvements):
    return local_improve(adj,gaussian(adj,np.random.default_rng(seed),radius),
                         random.Random(seed+11),improvements)

def main():
    start=time.monotonic();DATA.mkdir(parents=True,exist_ok=True)
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    # Select fixed parameters on separate training graphs; never best-of-seed
    # selection on test graphs for the claimed local algorithm.
    grid=list(itertools.product([9,17,25],[0,2,5]))
    scores={str(x):[] for x in grid}
    for trial in range(6):
        adj,_,_=graph(2000,SEED+100000+trial)
        for radius,improvements in grid:
            for rep in range(3):
                S=run_local(adj,SEED+200000+100*trial+rep,radius,improvements)
                valid(adj,S);scores[str((radius,improvements))].append(len(S)/len(adj))
    chosen=max(grid,key=lambda p:statistics.mean(scores[str(p)]))
    training={'seed':SEED,'grid_mean':{k:statistics.mean(v) for k,v in scores.items()},
              'chosen_radius_and_improvement_rounds':chosen,'graphs':6,'n':2000,'labels_per_graph':3}
    (DATA/'training.json').write_text(json.dumps(training,indent=2)+'\n')
    print('training',json.dumps(training),flush=True)
    summaries=[]
    for n,trials in [(20,10),(40,10),(60,10),(200,8),(500,8),(2000,6)]:
        rows=[]
        for trial in range(trials):
            seed=SEED+n*100+trial
            adj,edges,attempts=graph(n,seed)
            row={'n':n,'trial':trial,'graph_seed':seed,'configuration_attempts':attempts,
                 'edges':edges,'local_sizes':[],'parallel_greedy_sizes':[],
                 'gaussian_only_sizes':[],'local_sets':[]}
            for rep in range(12):
                label_seed=seed+500000+rep
                S=run_local(adj,label_seed,*chosen)
                P=parallel_greedy(adj,random.Random(label_seed),16)
                Q=gaussian(adj,np.random.default_rng(label_seed),chosen[0])
                for candidate in [S,P,Q]:valid(adj,candidate)
                row['local_sizes'].append(len(S));row['parallel_greedy_sizes'].append(len(P))
                row['gaussian_only_sizes'].append(len(Q));row['local_sets'].append(sorted(S))
            H=heuristic(adj,seed+700000);valid(adj,H)
            row.update(heuristic_size=len(H),heuristic_set=sorted(H))
            if n<=60:
                E,nodes=exact(adj);valid(adj,E)
                row.update(exact_size=len(E),exact_set=sorted(E),exact_recursion_states=nodes)
                assert len(E)>=len(H)
                if trial<3:
                    row['independent_milp_size']=milp_check(adj,edges)
                    assert row['independent_milp_size']==len(E)
            rows.append(row)
            with (DATA/'samples.jsonl').open('a') as out:out.write(json.dumps(row)+'\n')
        summary={'n':n,'graphs':trials}
        for key in ['local_sizes','parallel_greedy_sizes','gaussian_only_sizes']:
            # Graphs are independent statistical units; labels are nested.
            means=[statistics.mean(row[key])/n for row in rows]
            summary[key.replace('_sizes','')+'_mean']=statistics.mean(means)
            summary[key.replace('_sizes','')+'_graph_SE']=statistics.stdev(means)/math.sqrt(trials)
        summary['heuristic_mean']=statistics.mean(row['heuristic_size']/n for row in rows)
        summary['heuristic_min']=min(row['heuristic_size']/n for row in rows)
        summary['heuristic_max']=max(row['heuristic_size']/n for row in rows)
        if n<=60:summary['exact_mean']=statistics.mean(row['exact_size']/n for row in rows)
        summaries.append(summary)
        (DATA/'summary.json').write_text(json.dumps(summaries,indent=2)+'\n')
        print('test',json.dumps(summary),flush=True)
    meta={'wall_seconds':time.monotonic()-start,'peak_RSS_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'nice':os.getpriority(os.PRIO_PROCESS,0),'numerical_threads':1,
          'python':os.sys.version,'numpy':np.__version__}
    assert meta['peak_RSS_bytes']<4*1024**3
    (DATA/'experiment_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps(meta),flush=True)

if __name__=='__main__':
    assert not (DATA/'samples.jsonl').exists(), 'Keep existing data; choose a fresh output directory to rerun.'
    main()
