import itertools
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

ROOT = Path(__file__).resolve().parent
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
offsets = [(1, 0), (2, 0), (1, 1)]
ak = [1, 4 - 8 / math.pi, 4 / math.pi]
hist = {h: Counter() for h in offsets}
killed_hist = {h: Counter() for h in offsets}
total = 4**8
for moves in itertools.product(steps, repeat=8):
    path = [(0, 0)]
    for dx, dy in moves:
        x, y = path[-1]
        path.append((x + dx, y + dy))
    counts = Counter(path)
    for h in offsets:
        eligible = [v for (x, y), v in counts.items() if (x+h[0], y+h[1]) not in counts]
        hist[h][max(eligible, default=0)] += 1
        hit = next((j for j, z in enumerate(path) if z == h), len(path))
        killed_hist[h][sum(z == (0, 0) for z in path[:hit])] += 1
    assert all((x+9, y) not in counts for x, y in counts)
tail_results = []
for h, a in zip(offsets, ak):
    p = 1 - 1/(2*a)
    for k in range(1, 10):
        mtail = sum(v for value, v in hist[h].items() if value >= k)/total
        ntail = sum(v for value, v in killed_hist[h].items() if value >= k)/total
        assert mtail <= 9*p**(k-1) + 1e-14
        assert ntail <= p**(k-1) + 1e-14
        tail_results.append({'h': h, 'k': k, 'M_tail': mtail, 'killed_tail': ntail})

green_results = []
for radius in [4, 9, 17]:
    sites = [(x,y) for x in range(-radius,radius+1) for y in range(-radius,radius+1) if x*x+y*y<=radius*radius]
    index = {z:i for i,z in enumerate(sites)}
    matrix = lil_matrix((len(sites),len(sites)))
    for z,i in index.items():
        matrix[i,i] = 1
        for dx,dy in steps:
            j = index.get((z[0]+dx,z[1]+dy))
            if j is not None:
                matrix[i,j] = -0.25
    matrix = matrix.tocsc()
    zero = index[(0,0)]
    rhs = np.zeros(len(sites)); rhs[zero] = 1
    g0 = spsolve(matrix,rhs)
    for h in [(1,0),(2,1),(3,0)]:
        trap = index[h]
        rhsh = np.zeros(len(sites)); rhsh[trap] = 1
        gh = spsolve(matrix,rhsh)
        predicted = g0[zero] - gh[zero]*g0[trap]/gh[trap]
        keep = np.array([i for i in range(len(sites)) if i!=trap])
        direct = spsolve(matrix[keep][:,keep],rhs[keep])[int(np.where(keep==zero)[0][0])]
        error = abs(predicted-direct)
        assert error < 1e-10
        assert abs(gh[zero]-g0[trap]) < 1e-10
        green_results.append({'R':radius,'h':h,'predicted':predicted,'direct':float(direct),'error':error})

geometry_results = []
for alpha in [0.26,0.375,0.45]:
    for N in [512,4096,32768]:
        r = N**alpha
        L = 2**alpha; c = (L+2)/2; d = (2-L)/4
        assert abs(c-d-L-d) < 1e-14
        assert abs(2-c-d-d) < 1e-14
        bound = math.ceil(2*r)
        ann = sorted((x,y) for x in range(-bound,bound+1) for y in range(-bound,bound+1) if (2*N)**(2*alpha)<x*x+y*y<=4*r*r)
        fits = len(ann)<=N
        if fits:
            for i,(x,y) in enumerate(ann):
                t=N+i
                assert t**(2*alpha)<x*x+y*y<=4*t**(2*alpha)
        q = math.floor(c*r)
        contained = [(x,y) for x in range(q-math.ceil(d*r),q+math.ceil(d*r)+1) for y in range(-math.ceil(d*r),math.ceil(d*r)+1) if (x-q)**2+y*y<=d*d*r*r]
        if d*r>1:
            assert all((2*N)**(2*alpha)<x*x+y*y<=4*r*r for x,y in contained)
        geometry_results.append({'alpha':alpha,'N':N,'offset_count':len(ann),'scan_fits':fits,'disc_points':len(contained)})

walk_results = []
N = 4096; alpha = 0.375; limit = math.ceil(2*N**alpha)
ann = sorted((x,y) for x in range(-limit,limit+1) for y in range(-limit,limit+1) if (2*N)**(2*alpha)<x*x+y*y<=4*N**(2*alpha))
assert len(ann)<N
for seed in range(12):
    rng = np.random.default_rng(seed+701)
    moves = np.array(steps)[rng.integers(0,4,2*N)]
    path = np.vstack((np.zeros((1,2),dtype=int),np.cumsum(moves,axis=0)))
    start_counts = Counter(map(tuple,path[:N+1]))
    favorite,local = max(start_counts.items(),key=lambda z:z[1])
    full = set(map(tuple,path))
    i = next((i for i,h in enumerate(ann) if (favorite[0]+h[0],favorite[1]+h[1]) not in full),None)
    if i is not None:
        t = N+i; h=ann[i]; prefix=Counter(map(tuple,path[:t+1]))
        assert (favorite[0]+h[0],favorite[1]+h[1]) not in prefix
        assert prefix[favorite]>=local
    walk_results.append({'seed':seed+701,'hole_index':i,'start_local':local})

result = {'enumerated_paths':total,'finite_tails':tail_results,'green':green_results,'geometry':geometry_results,'walk_implication':walk_results,'alpha_3_8_g_pi':4*(3/8)*(1-3/8)}
(ROOT/'referee_verify_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'paths':total,'tail_checks':len(tail_results),'green_checks':len(green_results),'maximum_green_error':max(e['error'] for e in green_results),'geometry':geometry_results,'walk_checks':len(walk_results),'walk_holes':sum(e['hole_index'] is not None for e in walk_results),'g_pi_at_3_8':result['alpha_3_8_g_pi']},indent=2))
