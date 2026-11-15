"""Full GP_2 two-point comparisons, using explicit finitely deep side branches.

This imports only our independent audit code. The ancestor cap is at P^180(w).
Finite side branches have six generations below their root. Their exact effect
is independently integrated by the partition solver; the ancestor error uses (5).
"""
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import time
from independent_checks import (edges_from_parents, finite_r, infinite_r,
                                partition_reliability, sample_explicit)
ROOT = Path(__file__).resolve().parents[1]

def geometry(n, branch_depth):
    w = (0,)*n
    s,t = w+(0,),w+(1,)
    core = {w[:i] for i in range(n+1)} | {s,t}
    vertices = set(core)
    parents = {v:v[:-1] for v in core if v}
    branches = []
    for x in sorted(core,key=repr):
        xp = parents.get(x)
        if xp not in core: continue  # branches with only one attachment do nothing
        for j in range(2):
            z = x+(j,)
            if z in core: continue
            branches.append((x,xp,z))
            vertices.add(z); parents[z] = x
            layer = [z]
            for _ in range(branch_depth):
                following = []
                for v in layer:
                    for k in range(2):
                        child = v+(k,)
                        vertices.add(child); parents[child] = v
                        following.append(child)
                layer = following
    return vertices,parents,core,branches,s,t

def main():
    begin = time.monotonic()
    assert os.getpriority(os.PRIO_PROCESS,0) >= 10
    n,depth,samples = 180,6,2000
    vertices,parents,core,branches,s,t = geometry(n,depth)
    original_core = edges_from_parents(core,parents)
    explicit_edges = edges_from_parents(vertices,parents)
    rows = []
    for i,p in enumerate([.22,.32,.42]):
        def evaluate(r):
            edges = [(u,v,p) for u,v in original_core]
            edges += [(x,xp,p*r) for x,xp,z in branches]
            return partition_reliability(core,edges,s,t)
        infinite_cone = evaluate(infinite_r(2,p))
        finite_truncation = evaluate(finite_r(2,depth,p))
        ancestor_bound = (1-(1-p)**4)**(n//3+1)
        bottom_bias = infinite_cone-finite_truncation
        assert bottom_bias >= -1e-12
        wins = sample_explicit(vertices,explicit_edges,[(s,t)],p,samples,159100+i)[0]
        observed = wins/samples
        se = math.sqrt(finite_truncation*(1-finite_truncation)/samples)
        assert abs(observed-finite_truncation) < 5*se
        row = dict(p=p,vertices=len(vertices),edges=len(explicit_edges),ancestor_levels=n,
                   side_branch_depth=depth,samples=samples,seed=159100+i,
                   pair='two tree children of w',formula=infinite_cone,
                   finite_truncation_formula=finite_truncation,monte_carlo=observed,
                   standard_error=se,z=(observed-finite_truncation)/se,
                   omitted_ancestor_upper_bound=ancestor_bound,
                   side_branch_bias=bottom_bias,
                   full_probability_interval=[infinite_cone,infinite_cone+ancestor_bound])
        rows.append(row)
        print(json.dumps(row),flush=True)
    resources = dict(elapsed_seconds=time.monotonic()-begin,
                     peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                     nice=os.getpriority(os.PRIO_PROCESS,0),threads=1,
                     code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (ROOT/'data'/'full_graph_checks.json').write_text(json.dumps(dict(rows=rows,resources=resources),indent=2)+'\n')
    print(json.dumps(resources),flush=True)

if __name__ == '__main__': main()
