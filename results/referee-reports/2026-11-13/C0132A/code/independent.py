"""Separate Python implementation, using MT19937 and an ordinary set of tuples."""
import csv
import os
from pathlib import Path
import random

root=Path(__file__).resolve().parents[1]
assert os.getpriority(os.PRIO_PROCESS,0)>=10
with (root/'data/independent.csv').open('w') as f:
    out=csv.writer(f)
    out.writerow(['d1','d2','seed','n','range','origin_returns','window_hit'])
    for d1 in (1,2):
        for seed in range(16):
            rng=random.Random(100000+seed)
            position=[0]*(d1+1)
            departed=set()
            returns=last=0
            for t in range(1000000):
                p=tuple(position)
                if p not in departed:
                    departed.add(p)
                    axis=rng.randrange(d1)
                else:
                    axis=d1
                position[axis]+=1 if rng.getrandbits(1) else -1
                if not any(position):
                    returns+=1;last=t+1
                if t+1 in (10000,100000,1000000):
                    out.writerow([d1,1,seed,t+1,len(departed)+(tuple(position) not in departed),returns,int(last>(t+1)//2)])
            f.flush()
print('Independent MT19937 simulator completed: 16 seeds per case, 10^6 steps each.')
