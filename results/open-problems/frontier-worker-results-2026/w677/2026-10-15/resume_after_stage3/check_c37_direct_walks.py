"""Independent finite-block Monte Carlo control. Standard errors are descriptive."""
import random, json, math, time
from pathlib import Path
from collections import deque
from datetime import datetime

root=Path(__file__).resolve().parent
rng=random.Random(37720261015)
d=4
neighbors={0:[-1]+list(range(1,d+1))}
for i in range(1,d+1):
    children=list(range(d+1+(i-1)*d,d+1+i*d))
    neighbors[i]=[0]+children
    for v in children: neighbors[v]=[i]+[-2]*d
leaf=d+1
N=1+d+d*d
results=[]
start=time.monotonic()
for mode in ('top','bottom','root'):
    sums=[0.0]*4; squares=[0.0]*4
    trials=12000
    for _ in range(trials):
        awake={0} if mode=='top' else {0,1,leaf}
        queue=deque([0,0] if mode=='top' else [leaf])
        ups=downs=0
        while queue:
            v=queue.popleft()
            steps=0
            while v>=0:
                choices=neighbors[v]
                if mode=='root' and v==0: choices=choices[1:]
                v=rng.choice(choices)
                if v>=0 and v not in awake:
                    awake.add(v); queue.append(v)
                steps+=1
                assert steps<10000,'Censored walk; no control result permitted'
            if v==-1: ups+=1
            else: downs+=1
        cold=awake-({0} if mode=='top' else {0,1,leaf})
        values=[ups,downs,sum(1<=v<=d for v in cold),sum(v>d for v in cold)]
        for i,x in enumerate(values): sums[i]+=x; squares[i]+=x*x
    means=[v/trials for v in sums]
    errors=[math.sqrt(max(0,(squares[i]/trials-means[i]**2)/(trials-1))) for i in range(4)]
    reference=json.loads((root/'C37_SHARED_BLOCK_SCREEN_60.json').read_text())['results'][0][mode]
    target=[float(reference[k]) for k in ('up','down','expected_cold_children','expected_cold_leaves')]
    z=[(means[i]-target[i])/errors[i] if errors[i] else 0 for i in range(4)]
    results.append(dict(mode=mode,trials=trials,fields=['up','down','cold_children','cold_leaves'],means=means,standard_errors=errors,formula_values=target,z_scores=z))
    (root/'C37_DIRECT_CONTROL.json').write_text(json.dumps(dict(at=datetime.now().astimezone().isoformat(),seconds=time.monotonic()-start,scope='Independent Monte Carlo control only; no rigorous bound',results=results),indent=2)+'\n',encoding='utf-8')
    print(mode,'max_abs_z',max(map(abs,z)),flush=True)
