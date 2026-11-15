"""Independent trace replay using Python tuples and a dictionary of departure counts."""
import collections
import csv
import math
import subprocess
from pathlib import Path

root=Path(__file__).resolve().parents[1]
for d1 in (1,2):
    trace=root/'data'/f'verify_{d1}.txt'
    csv=root/'data'/f'verify_{d1}.csv'
    subprocess.run([str(root/'code/simulate'),str(d1),'20000','3','987',str(csv),str(trace)],check=True)
    import csv as csv_module
    records={(int(r['seed']),int(r['n'])):r for r in csv_module.DictReader(csv.open())}
    departure=collections.Counter()
    oldseed=None
    for line in trace.open():
        seed,t,x,y,z,fresh,axis,sign=map(int,line.split())
        if seed!=oldseed:
            departure.clear(); position=[0,0,0]; oldseed=seed
            first=returns=last=entries=successes=zeroq=0
            qsum=0.; active=hit=False; column=set(); cumulative={0:0}
        assert position==[x,y,z]
        assert bool(fresh)==(departure[tuple(position)]==0)
        assert (axis<d1 if fresh else axis==d1)
        if fresh:
            first+=1
            if all(v==0 for v in position[:d1]):
                column.add(position[d1])
                if active: successes+=hit
                active=hit=False
        departure[tuple(position)]+=1
        position[axis]+=sign
        if fresh and all(v==0 for v in position[:d1]):
            y=position[d1];entries+=1;active=True;hit=y==0
            lo=hi=0
            while lo-1 in column: lo-=1
            while hi+1 in column: hi+=1
            q=1. if y==0 else (0. if not lo<=y<=hi else
                             ((hi+1-y)/(hi+1) if y>0 else (y-lo+1)/(1-lo)))
            zeroq+=q==0;qsum+=q
        if not any(position): returns+=1;last=t+1
        if active and not any(position): hit=True
        n=t+1;cumulative[n]=returns
        if (seed,n) in records:
            r=records[seed,n]
            checks=dict(range=len(departure)+(tuple(position) not in departure),
                        first_departures=first,revisit_departures=n-first,
                        origin_returns=returns,last_origin=last,
                        window_visits=returns-cumulative[n//2],window_hit=int(last>n//2),
                        endpoint_origin=int(not any(position)),column_entries=entries,
                        column_successes=successes,column_zero_q=zeroq,column_sites=len(column))
            for name,value in checks.items(): assert int(r[name])==value,(d1,seed,n,name)
            assert math.isclose(float(r['column_q_sum']),qsum,abs_tol=1e-10)
    trace.unlink()
print('Independent replay passed: 120000 transitions, clock/range/return aggregates and column probabilities.')

# A reachable column can have a hole, invalidating an interval assumption.
path=[(0,0),(1,0),(2,0),(1,0),(1,1),(2,1),(3,1),(2,1),(2,2),(1,2),(0,2)]
dep=collections.Counter()
for a,b in zip(path,path[1:]):
    fresh=dep[a]==0
    delta=(b[0]-a[0],b[1]-a[1])
    assert delta in ((1,0),(-1,0)) if fresh else delta in ((0,1),(0,-1))
    dep[a]+=1
assert {y for x,y in path if x==0}=={0,2}
print('Reachable noninterval column example verified (10 steps, probability 2^-10).')
