"""Replay random parameter draws to classify all rejected mixed candidates."""
import random,math,json,time,resource
from pathlib import Path
import mpmath as mp
from mp_core import mixed,strict

def main():
    start=time.monotonic();rng=random.Random(33505)
    for L in (20,60,150,400,1000):
        for j in range(120):
            for _ in range(9):rng.gauss(0,1)
            rng.uniform(.01,.9)
    for L in (20,60,150,400):
        for j in range(650):
            for _ in range(3):rng.uniform(0,math.pi/2) if j%3==0 else rng.uniform(-.75,.75)
            if j%4:rng.uniform(-math.pi,math.pi)
            for _ in range(2):rng.uniform(-.8,.8)
            rng.uniform(-.85,.85)
    rows=[]
    for L in (20,60,150,400):
        mp.mp.dps=120+int(5*L/math.log(10));rejected=0
        for j in range(400):
            a=mp.mpf(str(rng.uniform(.15,2.5)));b=mp.mpf(str(rng.uniform(.15,2.5)))
            eta=max(a,b)/2+mp.mpf(str(rng.uniform(.1,2.5)));ratio=mp.mpf(str(rng.uniform(.1,2)))
            phase=mp.mpf(0) if j%2==0 else mp.mpf(str(rng.uniform(-math.pi,math.pi)))
            if not strict(mixed(mp.exp(-L),a,b,eta,ratio,phase)):rejected+=1
        rows.append(dict(L=L,strictness_rejections=rejected))
    search=json.load(open('data/search_mp.json'))
    assert sum(r['strictness_rejections'] for r in rows)==sum(g['attempts']-g['accepted'] for g in search['groups'].values())
    for r in rows:assert r['strictness_rejections']==search['groups']['mixed_'+str(r['L'])]['attempts']-search['groups']['mixed_'+str(r['L'])]['accepted']
    out=dict(rows=rows,all_constructed_rejections_are_non_strict=True,seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
    Path('data/input_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':main()
